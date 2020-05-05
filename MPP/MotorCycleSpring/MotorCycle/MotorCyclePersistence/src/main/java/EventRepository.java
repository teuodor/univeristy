

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class EventRepository implements IEventRepository{
    private JdbcUtils jdbcUtils;

    public EventRepository(String filename) {
        logger.info("Initializing EventRepository");
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



    public Iterable<Event> findAll() {
        logger.traceEntry("finding all events");
        Connection con = jdbcUtils.getConnection();
        List<Event> eventList = new ArrayList<>();

        try (PreparedStatement preStmt = con.prepareStatement("select * from Event")){
            try (ResultSet resultSet = preStmt.executeQuery()){
                while(resultSet.next()){
                    int id = resultSet.getInt("ID");
                    int engineCapacity = resultSet.getInt("Capacitate_motor");
                    Event event = new Event(id, engineCapacity);
                    eventList.add(event);
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
        }
        logger.traceExit(eventList);
        return eventList;
    }

    public Event findEngine(Integer engineCapacity) {
        try(PreparedStatement preparedStatement = jdbcUtils.getConnection().prepareStatement("select * from Event where Capacitate_motor = ?")){
            preparedStatement.setInt(1, engineCapacity);
            try(ResultSet resultSet = preparedStatement.executeQuery()) {
                while (resultSet.next()){
                    Integer id = resultSet.getInt("ID");
                    Integer engine = resultSet.getInt("Capacitate_motor");
                    return new Event(id, engine);
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
        }
        return null;
    }

    @Override
    public List<Integer> numberOfCompetitors(){
        List<Integer> toReturn = new ArrayList<>();
        try(PreparedStatement preparedStatement = jdbcUtils.getConnection().prepareStatement("select count(*) as [Number] from CompetitorEvent group by ID_Event")){
            try(ResultSet resultSet = preparedStatement.executeQuery()){
                while (resultSet.next()){
                    int nr = resultSet.getInt("Number");
                    toReturn.add(nr);
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex.getMessage());
        }

        return toReturn;
    }
}
