package Domain;

import java.util.ArrayList;
import java.util.List;

public class Competitor extends Entity<Integer>{
    private String name;
    private String team;
    private List<Event> eventList;

    public Competitor(Integer id, String name, String team) {
        super.setId(id);
        this.name = name;
        this.team = team;
        eventList = new ArrayList<>();
    }

    public Competitor(Integer id, String name, String team, List<Event> eventList) {
        super.setId(id);
        this.name = name;
        this.team = team;
        this.eventList = eventList;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
    }

    public List<Event> getEventList() {
        return eventList;
    }

    public void setEventList(List<Event> eventList) {
        this.eventList = eventList;
    }
}
