import java.net.Socket;

public abstract class AbstractConcurrentServer extends AbstractServer{
    public AbstractConcurrentServer(int port){
        super(port);
        System.out.println("Concurrent Abstract Server");
    }

    protected void processRequest(Socket client){
        Thread thread = createWorker(client);
        thread.start();
    }
    protected abstract Thread createWorker(Socket client);
}
