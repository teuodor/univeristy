package Service;

import Domain.Competitor;
import Domain.Event;
import Repository.CompetitorRepository;
import Repository.EventRepository;

import java.util.ArrayList;
import java.util.List;

public class CompetitorService {
    private EventRepository eventRepository;
    private CompetitorRepository competitorRepository;

    public CompetitorService(CompetitorRepository competitorRepository, EventRepository eventRepository) {
        this.competitorRepository = competitorRepository;
        this.eventRepository = eventRepository;
    }

    public Iterable<Competitor> findAll(){
        return competitorRepository.findAll();
    }

    public Iterable<Competitor> findByTeam(String team){
        List<Competitor> list = new ArrayList<>();
        for(Competitor competitor : competitorRepository.findAll()){
           if (competitor.getTeam().equals(team)){
               list.add(competitor);
           }
        }
       return list;
    }

    public void addCompetitor(String name, String team, Integer engineCapacity) {
        Competitor competitor = new Competitor(1, name, team);
        boolean ok = true;
        List<Event> eventList = new ArrayList<>();


        for (Competitor competitor1 : competitorRepository.findAll())
            if (competitor1.getName().equals(name) && competitor1.getTeam().equals(team)) {
                competitorRepository.addEvent(name, team, eventRepository.findEngine(engineCapacity));
                ok = false;
            }

        if (ok) {
            for (Event event : eventRepository.findAll()) {
                if (event.getEngineCapacity().equals(engineCapacity))
                    eventList.add(event);
            }
            competitor.setEventList(eventList);

            competitorRepository.save(competitor);
        }
    }
}
