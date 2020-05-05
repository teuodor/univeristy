
import javafx.util.Pair;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.Socket;
import java.util.List;

public class CompetitorClientRpcReflectionWorker implements Runnable,  EventObserver{

    private CompetitorServices server;
    private Socket connection;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private volatile boolean connected;
    private static Response okResponse = new Response.Builder().type(ResponseType.OK).build();

    public CompetitorClientRpcReflectionWorker(CompetitorServices server, Socket connection) {
        this.server = server;
        this.connection = connection;
        try{
            output = new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input = new ObjectInputStream(connection.getInputStream());
            connected = true;
        }
        catch (IOException ex){
            ex.printStackTrace();
        }
    }

    @Override
    public void newCompetitorUpdate(Integer eventID) throws Exception {
        System.out.println("Employee newCompetitorUpdate");
        Response response = new Response.Builder().type(ResponseType.UPDATE).data(eventID).build();
        try{
            sendResponse(response);
            System.out.println("Finish response");
        }
        catch (Exception ex){
            throw ex;
        }
    }

    @Override
    public void run() {
        while (connected){
            try{
                Object request = input.readObject();
                Response response = handleRequest((Request) request);
                if (response != null) {
                    sendResponse(response);
                }
            }
            catch (IOException | ClassNotFoundException ex){
                ex.printStackTrace();
            }

            try{
                Thread.sleep(1000);
            }
            catch (InterruptedException ex){
                ex.printStackTrace();
            }

        }
        try{
            input.close();
            output.close();
            connection.close();
        }
        catch (IOException ex){
            ex.printStackTrace();
        }
    }

    private void sendResponse(Response response) throws IOException{
        System.out.println("sending response " + response);
        output.writeObject(response);
        System.out.println("Write object!");
        output.flush();
        System.out.println("Flush!");
    }

    private Response handleRequest(Request request) {
        Response response = null;
        String handlerName = "handle" + request.type();
        System.out.println("HandlerName" + handlerName);
        try{
            Method method = this.getClass().getDeclaredMethod(handlerName, Request.class);
            response=(Response)method.invoke(this,request);
            System.out.println("Method" + handlerName + " invoked");
        }
        catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException ex){
            ex.printStackTrace();
        }

        return response;

    }

    private Response handleLOGIN(Request request){
        System.out.println("Login request..." + request.type());
        Employee employee = (Employee) request.data();

        try{
            server.tryLogin(employee.getUsername(),employee.getPassword(), this);
            return okResponse;
        }
        catch (Exception e){
            connected = false;
            return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
        }
    }

    private Response handleLOGOUT(Request request){
        System.out.println("Logout request...");

        Employee employee = (Employee)request.data();
        try {
            server.logout(employee, this);
            connected = false;
            return okResponse;
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }

    private Response handleADD_COMPETITOR(Request request){
        System.out.println("Add Competitor Request...");
        CompetitorDTO competitor = (CompetitorDTO)request.data();

        try {
            server.addCompetitor(competitor.getName(),competitor.getTeam(),competitor.getEngineCapacity());
            return okResponse;
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }

    private Response handleGET_EVENTS(Request request){
        System.out.println("Get all events request...");
        try{
            Iterable<Event> events = server.findAllEvents();
            return new Response.Builder().type(ResponseType.OK).data(events).build();
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }

    private Response handleGET_COMPETITORS_BY_TEAM(Request request){
        System.out.println("Get competitors by team...");
        try{
            String team = (String)request.data();
            Iterable<Competitor> competitors = server.findByTeam(team);
            return new Response.Builder().type(ResponseType.OK).data(competitors).build();
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }

    private Response handleUPDATE(Request request){
        System.out.println("Update" + request);
        try{
            return new Response.Builder().type(ResponseType.OK).data("update").build();
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }

    private Response handleNUMBER_OF_COMPETITORS(Request request){
        System.out.println("Get all events number of competitors request...");
        try{
            Iterable<Integer> events = server.numberOfCompetitorsEvents();
            return new Response.Builder().type(ResponseType.OK).data(events).build();
        }
        catch (Exception ex){
            return new Response.Builder().type(ResponseType.ERROR).data(ex.getMessage()).build();
        }
    }
}
