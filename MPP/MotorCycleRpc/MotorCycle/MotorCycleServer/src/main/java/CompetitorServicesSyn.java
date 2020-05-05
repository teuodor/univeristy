import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CompetitorServicesSyn implements CompetitorServices{
    private EmployeeRepository employeeRepository;
    private CompetitorRepository competitorRepository;
    private EventRepository eventRepository;
    private Map<String, EventObserver> loggedEmployees;

    public CompetitorServicesSyn(EmployeeRepository employeeRepository, CompetitorRepository competitorRepository, EventRepository eventRepository) {
        this.employeeRepository = employeeRepository;
        this.competitorRepository = competitorRepository;
        this.eventRepository = eventRepository;
        loggedEmployees = new ConcurrentHashMap<>();
    }

    @Override
    public synchronized void tryLogin(String username, String password, EventObserver eventObserver) throws Exception {
        if(employeeRepository.login(username, password)){
            if(loggedEmployees.get(username) != null){
                throw new Exception("User already logged in!");
            }
            loggedEmployees.put(username, eventObserver);
        }
        else {
            throw new Exception("Authentification failed!!!");
        }
    }

    @Override
    public Iterable<Competitor> findByTeam(String team) throws Exception {
        return competitorRepository.findByTeam(team);
    }

    @Override
    public Iterable<Event> findAllEvents() throws Exception {
        return eventRepository.findAll();
    }

    @Override
    public Iterable<Integer> numberOfCompetitorsEvents() throws Exception {
        return eventRepository.numberOfCompetitors();
    }

    @Override
    public synchronized void addCompetitor(String name, String team, Integer engineCapacity) throws Exception {
        System.out.println("Add competitor" + name + " " + team + " " + engineCapacity.toString());
        Event event = eventRepository.findEngine(engineCapacity);

        if(competitorRepository.findByNameTeam(name, team) != null) {
            if(event != null)
                competitorRepository.addEvent(name, team,event);
            else
                throw new Exception("Not such event!");
        }
        else {
            List<Event> eventList = new ArrayList<>();
            if (event != null)
                eventList.add(event);
            else
                throw new Exception("Not such event!");
            Competitor competitor = new Competitor(1, name, team, eventList);
            competitorRepository.save(competitor);
        }
        notifyAllLoggedEmployees(eventRepository.findEngine(engineCapacity).getId());
    }

    @Override
    public synchronized void logout(Employee employee, EventObserver eventObserver) throws Exception {
        EventObserver localClient = this.loggedEmployees.remove(employee.getUsername());
        if (localClient == null)
            throw new Exception("Error logout!");
    }


    private void notifyAllLoggedEmployees(Integer eventId){
        final int threadsNo = 10;
        List<Event> list = (List<Event>) eventRepository.findAll();
        System.out.println("Notify all users!");
        ExecutorService executor = Executors.newFixedThreadPool(threadsNo);

        for (Entry<String, EventObserver> pair : loggedEmployees.entrySet()) {
            System.out.println(pair.getKey() + " = " + pair.getValue());
            EventObserver eventObserver = loggedEmployees.get(pair.getKey());
            executor.execute(() -> {
                try {
                    eventObserver.newCompetitorUpdate(eventId);
                } catch (Exception ex) {
                    System.err.println(ex.toString());
                }
            });
        }

        executor.shutdown();
    }
}
