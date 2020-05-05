package Repository;
import Domain.Event;
import org.apache.logging.log4j.*;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class EventRepository implements IRepository<Integer, Event>{
    private JdbcUtils jdbcUtils;

    public EventRepository(Properties properties) {
        logger.info("Initializing EventRepository");
        this.jdbcUtils = new JdbcUtils(properties);
    }
    private static final Logger logger = LogManager.getLogger();


    @Override
    public int size() {
        logger.traceEntry();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select count (*) as [SIZE] from Event")){
            try(ResultSet resultSet = preStmt.executeQuery()){
                if(resultSet.next()){
                    logger.traceExit(resultSet.getInt("SIZE"));
                    return resultSet.getInt(("SIZE"));
                }
            }
        }
        catch (SQLException exception){
            System.out.println(exception.toString());
        }
        return 0;
    }

    @Override
    public void save(Event entity){
        logger.traceEntry();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into Event values(?, ?)")){
            preStmt.setInt(1,entity.getId());
            preStmt.setInt(2,entity.getEngineCapacity());
            int result = preStmt.executeUpdate();
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit();
    }

    @Override
    public void delete(Integer id){
        logger.traceEntry("deleting event with {}", id);
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from Event where ID = ?")){
            preStmt.setInt(1,id);
            int result = preStmt.executeUpdate();
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit();
    }

    @Override
    public void update(Integer id, Event event){
        logger.traceEntry("updating event with {}", id);
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update Event set Capacitate_motor = ? where ID = ?")){
            preStmt.setInt(1,event.getEngineCapacity());
            preStmt.setInt(2,event.getId());
            int result = preStmt.executeUpdate();
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit();
    }


    @Override
    public Event findOne(Integer id) {
        logger.traceEntry("finding event with id {}", id);
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Event where ID = ?")){
            preStmt.setInt(1, id);
            try(ResultSet resultSet = preStmt.executeQuery()) {
                if(resultSet.next()){
                    int engineCapacity = resultSet.getInt("Capacitate_motor");
                    Event event = new Event(id, engineCapacity);
                    logger.traceExit(event);
                    return event;
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit("no event find with id {}", id);
        return null;
    }

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
}
