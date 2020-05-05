
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class CompetitorRepository implements ICompetitorRepository {
    private JdbcUtils jdbcUtils;

    public CompetitorRepository(String filename) {
        logger.info("Initializing CompetitorRepository");
        Properties properties = new Properties();
        try {
            properties.load(CompetitorRepository.class.getResourceAsStream(filename));
        }
        catch(Exception ex){
            System.out.println(ex.getMessage());
        }
        this.jdbcUtils = new JdbcUtils(properties);
    }
    private static final Logger logger = LogManager.getLogger();


    @Override
    public void save(Competitor entity){
        logger.traceEntry();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into Competitor values ((select max (ID) from Competitor) + 1, ?, ?)")){
            preStmt.setString(1,entity.getName());
            preStmt.setString(2, entity.getTeam());
            try(PreparedStatement preStmt2 = con.prepareStatement("insert into CompetitorEvent values ((select max(ID) from Competitor), ?)")){
                for(Event event : entity.getEventList()){
                    preStmt2.setInt(1,event.getId());
                    int result = preStmt.executeUpdate();
                    int result1 = preStmt2.executeUpdate();
                }
            }

        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit();
    }

    @Override
    public Iterable<Competitor> findByTeam(String team) {
        List<Competitor> competitors = new ArrayList<>();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preparedStatement = con.prepareStatement("select * from Competitor where Team = ?")){
            preparedStatement.setString(1,team);
            try(ResultSet resultSet = preparedStatement.executeQuery()){
                while (resultSet.next()){
                    int id = resultSet.getInt("ID");
                    String name = resultSet.getString("Name");
                    competitors.add(new Competitor(id, name, team));
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
        }

        return competitors;
    }


    public Iterable<Competitor> findAll(){
        logger.traceEntry("finding all competitors");
        Connection con = jdbcUtils.getConnection();
        List<Competitor> competitorList = new ArrayList<>();

        try (PreparedStatement preStmt = con.prepareStatement("select * from Competitor")) {
            try (ResultSet resultSet = preStmt.executeQuery()) {
                while (resultSet.next()) {
                    Integer id = resultSet.getInt("ID");
                    String name = resultSet.getString("Name");
                    String team = resultSet.getString("Team");
                    Competitor competitor = new Competitor(id, name, team);
                    try (PreparedStatement preparedStatement = con.prepareStatement("select * from Event E " +
                            "inner join CompetitorEvent CE on E.ID = CE.ID_Event " +
                            "inner join  Competitor C on CE.ID_Competitor = C.ID " +
                            "where C.ID = ?")) {
                        List<Event> eventList = new ArrayList<>();
                        preparedStatement.setInt(1, id);
                        try(ResultSet resultSet1 = preparedStatement.executeQuery()){
                            while(resultSet1.next()){
                                Integer id_Event = resultSet1.getInt("ID_Event");
                                Integer engineCapacity = resultSet1.getInt("Capacitate_motor");
                                Event event = new Event(id_Event,engineCapacity);
                                eventList.add(event);
                            }
                            competitor.setEventList(eventList);
                            competitorList.add(competitor);
                        }
                    }
                }
            }

        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit(competitorList);
        return competitorList;
    }

    private List<Event> getEvents(Integer id){
        List<Event> eventList = new ArrayList<>();
        try(PreparedStatement preparedStatement = jdbcUtils.getConnection().prepareStatement("select E.id, capacitate_motor from Event E\n" +
                "inner join CompetitorEvent CE on CE.ID_Event = E.ID\n" +
                "inner join Competitor C on CE.ID_Competitor = C.ID\n" +
                "where C.ID = ?")){
            try(ResultSet resultSet = preparedStatement.executeQuery()){
                while(resultSet.next()){
                    Integer eventId = resultSet.getInt("id");
                    Integer engineCapacity = resultSet.getInt("capacitate_motor");
                    Event event = new Event(eventId, engineCapacity);
                    eventList.add(event);
                }
            }

        }
        catch (SQLException ex){
            logger.error(ex);
        }

        return eventList;
    }

    public Competitor findByNameTeam(String name, String team){
        try(PreparedStatement preparedStatement = jdbcUtils.getConnection().prepareStatement("select * from Competitor where Name = ? and Team = ?")){
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, team);
            try(ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()){
                    Integer id = resultSet.getInt("ID");
                    return new Competitor(id, name, team);
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
        }
        return null;
    }

    public void addEvent(String name, String team, Event event) {
        Competitor competitor = findByNameTeam(name,team);
        try(PreparedStatement preparedStatement = jdbcUtils.getConnection().prepareStatement("insert into CompetitorEvent values (?,?)")){
            preparedStatement.setInt(1,competitor.getId());
            preparedStatement.setInt(2, event.getId());
            preparedStatement.executeUpdate();
        }
        catch (SQLException ex){
            logger.error(ex);
        }
    }

}
