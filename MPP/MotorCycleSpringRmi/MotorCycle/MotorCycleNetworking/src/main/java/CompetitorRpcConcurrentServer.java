import java.net.Socket;

public class CompetitorRpcConcurrentServer extends AbstractConcurrentServer{
    private CompetitorServices competitorServices;
    public CompetitorRpcConcurrentServer(int port, CompetitorServices competitorServices){
        super(port);
        this.competitorServices = competitorServices;
        System.out.println("Competitor - ChatRpcConcurrentServer");
    }

    @Override
    protected Thread createWorker(Socket client) {
        CompetitorClientRpcReflectionWorker worker = new CompetitorClientRpcReflectionWorker(competitorServices, client);

        Thread thread = new Thread(worker);
        return thread;
    }

    @Override
    public void stop() {
        System.out.println("Stopping services...");
    }
}
