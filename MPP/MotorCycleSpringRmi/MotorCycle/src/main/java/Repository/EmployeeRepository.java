package Repository;

import Domain.Employee;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class EmployeeRepository implements IRepository<Integer, Employee> {
    private JdbcUtils jdbcUtils;

    public EmployeeRepository(Properties properties) {
        logger.info("Initializing EmployeeRepository");
        this.jdbcUtils = new JdbcUtils(properties);
    }
    private static final Logger logger = LogManager.getLogger();


    @Override
    public int size() {
        logger.traceEntry();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select count (*) as [SIZE] from Employee")){
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
    public void save(Employee entity){
        logger.traceEntry();
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into Employee values(?, ?, ?)")){
            preStmt.setString(1,entity.getUsername());
            preStmt.setString(2,entity.getPassword());
            preStmt.setInt(3,entity.getId());
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
        try(PreparedStatement preStmt = con.prepareStatement("delete from Employee where ID = ?")){
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
    public void update(Integer id, Employee employee){
        logger.traceEntry("updating event with {}", id);
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update Employee set Username = ?, Password= ? where ID = ?")){
            preStmt.setString(1,employee.getUsername());
            preStmt.setString(2,employee.getPassword());
            preStmt.setInt(3, id);
            int result = preStmt.executeUpdate();
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit();
    }


    @Override
    public Employee findOne(Integer id) {
        logger.traceEntry("finding event with id {}", id);
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Employee where ID = ?")){
            preStmt.setInt(1, id);
            try(ResultSet resultSet = preStmt.executeQuery()) {
                if(resultSet.next()){
                    String username = resultSet.getString("Username");
                    String password = resultSet.getString("Password");
                    Employee employee = new Employee(id, username, password);
                    logger.traceExit(employee);
                    return employee;
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

    public Iterable<Employee> findAll() {
        logger.traceEntry("finding all events");
        Connection con = jdbcUtils.getConnection();
        List<Employee> employeeList = new ArrayList<>();

        try (PreparedStatement preStmt = con.prepareStatement("select * from Employee")){
            try (ResultSet resultSet = preStmt.executeQuery()){
                while(resultSet.next()){
                    int id = resultSet.getInt("ID");
                    String username = resultSet.getString("Username");
                    String password = resultSet.getString("Password");
                    Employee employee = new Employee(id, username, password);
                    employeeList.add(employee);
                }
            }
        }
        catch (SQLException ex){
            logger.error(ex);
            System.out.println(ex);
        }
        logger.traceExit(employeeList);
        return employeeList;
    }
}
