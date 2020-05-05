import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.Properties;

public class StartRpcClient extends Application {
    private static int port = 5555;
    private static String server = "localhost";

    @Override
    public void start(Stage stage) throws Exception {
        System.out.println("In start: ");
        Properties clientProps = new Properties();
        try{
            clientProps.load(StartRpcClient.class.getResourceAsStream("competitorClient.properties"));
            System.out.println("Client properties set!");
            stage.show();
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }

        String serverIP = clientProps.getProperty("motorcycle.server.host", server);
        int serverPort = port;
        try{
            serverPort = Integer.parseInt(clientProps.getProperty("motorcycle.server.port"));
        }
        catch (Exception e){
            System.out.println("Using default port");
        }

//        CompetitorServices services = new CompetitorServicesRpcProxy(serverIP,serverPort);
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:springConfig.xml");
        CompetitorServices services = (CompetitorServices) factory.getBean("competitorService");


        LoginController ctrl = new LoginController();
        ApplicationController appCtrl = new ApplicationController();

        FXMLLoader loader = new FXMLLoader(getClass().getResource("/loginWindow.fxml"));
        loader.setController(ctrl);
        Parent root = loader.load();

        ctrl.setServer(services);
        ctrl.setStage(stage);
        ctrl.setAppController(appCtrl);


        stage.setTitle("MotorCycle MPP");
        stage.setScene(new Scene(root));
        stage.show();


        appCtrl.setServer(services);
    }

}
