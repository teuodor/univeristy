package Domain;

public class Event extends Entity<Integer> {
    private Integer engineCapacity;

    public Event(Integer id, Integer engineCapacity) {
        super.setId(id);
        this.engineCapacity = engineCapacity;
    }

    public Integer getEngineCapacity() {
        return engineCapacity;
    }

    public void setEngineCapacity(Integer engineCapacity) {
        this.engineCapacity = engineCapacity;
    }
}
