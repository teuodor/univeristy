package Service;

import Domain.Event;
import Repository.EventRepository;

public class EventService {
    private EventRepository eventRepository;

    public EventService(EventRepository eventRepository) {
        this.eventRepository = eventRepository;
    }

    public Iterable<Event> findAll(){
        return eventRepository.findAll();
    }


}
