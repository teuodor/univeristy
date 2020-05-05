import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;


public abstract class AbstractServer {
    private int port;
    private ServerSocket server = null;

    public AbstractServer(int port) {
        this.port = port;
    }

    public void start() throws ServerException{
        try{
            server = new ServerSocket(port);
            while (true){
                System.out.println("Waiting for clients...");
                Socket client = server.accept();
                System.out.println("Client accepted...");
                processRequest(client);
            }

        }
        catch (IOException ex){
            throw new ServerException("Unable to start server", ex);
        }
        finally {
            stop();
        }
    }

    protected abstract void processRequest(Socket client);

    protected void stop() throws ServerException{
        try{
            server.close();
        }
        catch (IOException ex){
            throw new ServerException("Unable to close server...", ex);
        }
    }
}
