
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class StartRmiServer {
    public static void main(String[] args){
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:springConfig.xml");
        System.out.println("Started server...");
    }
}

