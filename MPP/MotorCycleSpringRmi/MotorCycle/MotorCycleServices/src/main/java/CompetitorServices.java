import java.rmi.Remote;

public interface CompetitorServices extends Remote {
    void tryLogin(String username, String password, EventObserver eventObserver) throws Exception;

    Iterable<Competitor> findByTeam(String team) throws Exception;

    Iterable<Event> findAllEvents() throws Exception;

    Iterable<Integer> numberOfCompetitorsEvents() throws Exception;

    void addCompetitor(String name, String team, Integer engineCapacity) throws Exception;

    void logout(Employee employee, EventObserver eventObserver) throws Exception;

}
