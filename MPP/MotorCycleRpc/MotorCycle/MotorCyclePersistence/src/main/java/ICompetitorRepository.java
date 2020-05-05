public interface ICompetitorRepository {
    void save(Competitor competitor);
    Iterable<Competitor> findByTeam(String team);
}
