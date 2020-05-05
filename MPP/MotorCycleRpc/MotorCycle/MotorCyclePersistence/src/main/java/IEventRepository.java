import java.util.List;

public interface IEventRepository {
    Iterable<Event> findAll();
    public List<Integer> numberOfCompetitors();
}
