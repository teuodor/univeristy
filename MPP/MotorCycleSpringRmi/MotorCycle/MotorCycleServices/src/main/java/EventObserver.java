import java.rmi.Remote;
import java.util.List;

public interface EventObserver extends Remote {
    void newCompetitorUpdate(Integer eventId) throws Exception;
}
