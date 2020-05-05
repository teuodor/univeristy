package GUI;

import Domain.Competitor;
import Domain.Event;
import Repository.CompetitorRepository;
import Repository.EmployeeRepository;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(getClass().getResource("/loginWindow.fxml"));
        loader.setController(new LoginController());

        Parent root = loader.load();
        stage.setTitle("Login Window");
        stage.setScene(new Scene(root, 600, 400));
        stage.show();
    }

    public static void main(String[] args){
        //JdbcUtils jdbcUtils = new JdbcUtils(new Properties());
        //jdbcUtils.getNewConnection();

//        List<Event> eventList = new ArrayList<>();
//        eventList.add(new Event(1, 125));
//        eventList.add(new Event(3, 175));
//        try {
//            Properties properties = new Properties();
//            properties.load(new FileReader("bd.config"));
//            CompetitorRepository competitorRepository = new CompetitorRepository(properties);
//            System.out.println(competitorRepository.size());
//            competitorRepository.save(new Competitor(4,"Sergiu", "Suzuki", eventList));
//
//            competitorRepository.update(4, new Competitor(4, "Sergiu", "Suzuki"));
//            System.out.println(competitorRepository.findOne(4).getName());
//            competitorRepository.delete(4);
//            System.out.println(competitorRepository.size());
//
//            EmployeeRepository employeeRepository = new EmployeeRepository(properties);
//            System.out.println(employeeRepository.size());
//            System.out.println(employeeRepository.size());
//
//        }
//        catch (IOException ex){
//            System.out.println("da");
//        }
//
        launch(args);
    }
}
