import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class EmployeeRepository implements IEmployeeRepository {
    private JdbcUtils jdbcUtils;

    public EmployeeRepository(String fileName) {
        logger.info("Initializing EmployeeRepository");
        Properties properties = new Properties();
        try {
            properties.load(CompetitorRepository.class.getResourceAsStream(fileName));
        }
        catch(Exception ex){
            System.out.println(ex.getMessage());
        }
        this.jdbcUtils = new JdbcUtils(properties);
    }
    private static final Logger logger = LogManager.getLogger();


    @Override
    public boolean login(String username, String password) {
        logger.traceEntry("finding all events");
        Connection con = jdbcUtils.getConnection();
        try(PreparedStatement preparedStatement = con.prepareStatement("select count (*) as [Number] from Employee where Username = ? and Password = ?")){
            preparedStatement.setString(1,username);
            preparedStatement.setString(2,password);
            try(ResultSet resultSet = preparedStatement.executeQuery()){
                int ok = resultSet.getInt("Number");
                if(ok > 0)
                    return true;
                return false;
            }
        }
        catch (SQLException ex){
            logger.error(ex.getMessage());
        }
        return false;
    }
}
