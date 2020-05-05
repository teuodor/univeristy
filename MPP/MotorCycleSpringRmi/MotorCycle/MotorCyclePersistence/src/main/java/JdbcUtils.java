import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class JdbcUtils {
    private Properties jdbcProps;
    private static final Logger logger = LogManager.getLogger();
    public JdbcUtils(Properties properties) {jdbcProps = properties;}

    private Connection instance = null;

    public Connection getNewConnection(){
        logger.traceEntry();
        String url = jdbcProps.getProperty("motorcycle.jdbc.url");
        Connection con = null;
        logger.info("trying to connect to database ... {}", url);
        try{
            con = DriverManager.getConnection(url);
        }
        catch (SQLException exception){
            System.out.println(exception.getErrorCode());
        }

        return con;

    }

    public Connection getConnection(){
        logger.traceEntry();
        try{
            if(instance == null || instance.isClosed())
                instance = getNewConnection();
        } catch (SQLException exception){
            logger.error(exception);
            System.out.println(exception.toString());
        }
        logger.traceExit(instance);
        return instance;
    }

}
