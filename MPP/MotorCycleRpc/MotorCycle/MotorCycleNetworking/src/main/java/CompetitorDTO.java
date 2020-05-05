import java.io.Serializable;

public class CompetitorDTO implements Serializable {
    private String name;
    private String team;
    private Integer engineCapacity;

    public CompetitorDTO(String name, String team, Integer engineCapacity) {
        this.name = name;
        this.team = team;
        this.engineCapacity = engineCapacity;
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

    public Integer getEngineCapacity() {
        return engineCapacity;
    }

    public void setEngineCapacity(Integer engineCapacity) {
        this.engineCapacity = engineCapacity;
    }
}
