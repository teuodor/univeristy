import java.util.List;

public interface EventObserver {
    void newCompetitorUpdate(Integer eventId) throws Exception;
}
