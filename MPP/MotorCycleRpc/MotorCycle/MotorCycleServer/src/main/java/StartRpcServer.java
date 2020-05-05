import java.io.IOException;
import java.util.Properties;

public class StartRpcServer {
    private static int port = 5555;
    public static void main(String[] args){
        Properties serverProps = new Properties();
        try{
            serverProps.load(StartRpcServer.class.getResourceAsStream("competitor.server.properties"));
            System.out.println("Server properties are set!");
            serverProps.list(System.out);
        }
        catch (IOException ex){
            System.err.println("Cannot find competitorserver.properties!");
            return;
        }

        EmployeeRepository employeeRepository = new EmployeeRepository(serverProps);
        EventRepository eventRepository = new EventRepository(serverProps);
        CompetitorRepository competitorRepository = new CompetitorRepository(serverProps);

        CompetitorServices services = new CompetitorServicesSyn(employeeRepository,competitorRepository,eventRepository);

        int competitorPort = port;

        try{
            competitorPort = Integer.parseInt(serverProps.getProperty("motorcycle.server.port"));
        }
        catch (NumberFormatException ex){
            System.err.println("Wrong Port number!");
            System.err.println("Using default port number!" + port);
        }

        System.out.println("Starting server on port: " + competitorPort);
        AbstractServer server = new CompetitorRpcConcurrentServer(competitorPort, services);
        try{
            server.start();
        }
        catch (ServerException ex){
            System.err.println("Error starting the server");
        }finally {
            try{
                server.stop();
            }
            catch (ServerException ex){
                System.err.println("Error stopping the server!");
            }
        }
    }
}
