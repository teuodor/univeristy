import javafx.util.Pair;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

import java.net.SocketException;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class CompetitorServicesRpcProxy implements CompetitorServices {
    private String host;
    private int port;

    private EventObserver client;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private Socket connection;

    private BlockingQueue<Response> qResponse;
    private volatile boolean finished;

    public CompetitorServicesRpcProxy(String host, int port) {
        this.host = host;
        this.port = port;
        qResponse = new LinkedBlockingQueue<Response>();
    }

    @Override
    public void tryLogin(String username, String password, EventObserver eventObserver) throws Exception {
        initializeConnection();
        Employee employee = new Employee(1, username, password);
        Request request = new Request.Builder().type(RequestType.LOGIN).data(employee).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.OK){
            this.client = eventObserver;
            return;
        }
        else {
            String err = response.data().toString();
            closeConnection();
            throw new Exception(err);        }
    }

    @Override
    public Iterable<Competitor> findByTeam(String team) throws Exception {
        Iterable<Competitor> competitors = null;
        Request request = new Request.Builder().type(RequestType.GET_COMPETITORS_BY_TEAM).data(team).build();
        sendRequest(request);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR){
            String ex = response.data().toString();
            throw new Exception(ex);
        }
        competitors = (Iterable<Competitor>) response.data();
        return competitors;
    }

    @Override
    public Iterable<Event> findAllEvents() throws Exception {
        Iterable<Event> events = null;
        Request request = new Request.Builder().type(RequestType.GET_EVENTS).data("events").build();
        sendRequest(request);
        Response response = readResponse();
        if(response.type() == ResponseType.ERROR){
            String ex = response.data().toString();
            throw new Exception(ex);
        }

        events = (Iterable<Event>) response.data();
        return events;
    }

    @Override
    public Iterable<Integer> numberOfCompetitorsEvents() throws Exception {
        Iterable<Integer> events = null;
        Request request = new Request.Builder().type(RequestType.NUMBER_OF_COMPETITORS).data("number").build();
        sendRequest(request);
        Response response = readResponse();
        if(response.type() == ResponseType.ERROR){
            String ex = response.data().toString();
            throw new Exception(ex);
        }

        events = (Iterable<Integer>) response.data();
        return events;
    }

    @Override
    public void addCompetitor(String name, String team, Integer engineCapacity) throws Exception {
        System.out.println("add competitor" + name + " " + team + " " + engineCapacity.toString());
        CompetitorDTO competitor = new CompetitorDTO(name, team, engineCapacity);
        Request request = new Request.Builder().type(RequestType.ADD_COMPETITOR).data(competitor).build();
        sendRequest(request);
        Response response = readResponse();

        if (response.type() == ResponseType.ERROR){
            String ex = response.data().toString();
            throw new Exception(ex);
        }
        System.out.println("finish add competitor");
    }

    @Override
    public void logout(Employee employee, EventObserver eventObserver) throws Exception {
        Request request = new Request.Builder().type(RequestType.LOGOUT).data(employee).build();
        sendRequest(request);
        Response response = readResponse();
        closeConnection();
        if (response.type() == ResponseType.ERROR) {
            String ex = response.data().toString();
            throw new Exception(ex);
        }
    }

    private void sendRequest(Request request) throws Exception {
        try{
            output.writeObject(request);
            output.flush();
        }
        catch (Exception ex){
            throw new Exception("Error sending request");
        }
    }

    private void initializeConnection(){
        try {
            connection = new Socket(host, port);
            output = new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input = new ObjectInputStream(connection.getInputStream());
            finished = false;
            startReader();
        }
        catch (IOException ex){
            ex.printStackTrace();
        }
    }
    private void closeConnection(){
        finished = true;
        try {
            input.close();
            output.close();
            connection.close();
            client = null;
        }
        catch (Exception ex){
            ex.printStackTrace();
        }
    }

    private Response readResponse(){
        Response response = null;
        try{

            response = qResponse.take();
//            response =(Response) input.readObject();
        }

        catch (InterruptedException ex){
            ex.printStackTrace();
        }
        return response;
    }

    private void startReader() {
        Thread thread = new Thread(new ReaderThread());
        thread.start();
    }

    private boolean isUpdate(Response response){
        return response.type() == ResponseType.UPDATE;
    }

    private class ReaderThread implements Runnable {
        @Override
        public void run() {
            while (!finished){
                try{
                    System.out.println("readerThread");
                    Object response = input.readObject();
                    System.out.println("response received");
                    if(isUpdate((Response) response)){
                        handleUpdate((Response) response);
                    }
                    else {
                        try{
                            qResponse.put((Response) response);
                        }
                        catch (InterruptedException ex){
                            ex.printStackTrace();
                        }
                    }
                }
                catch (SocketException ex){
                    System.out.println("Socket closed");
                }
                catch (Exception ex){
                    ex.printStackTrace();
                }
            }
        }
    }

    private void handleUpdate(Response response) {
        if(response.type() == ResponseType.UPDATE){
            try{
                System.out.println("handleUpdate in");
                Integer eventId = (Integer) response.data();
                client.newCompetitorUpdate(eventId);
                System.out.println("handleUpdate out");
            }
            catch (Exception ex){
                ex.printStackTrace();
            }
        }

    }
}
