package GUI;

import Config.Config;
import Repository.EmployeeRepository;
import Service.EmployeeService;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.util.Properties;

public class LoginController {

    private EmployeeService employeeService;

    @FXML
    private Button loginButton;

    @FXML
    private TextField userField;

    @FXML
    private PasswordField passwordField;

    public LoginController() throws IOException {
        EmployeeRepository employeeRepository = new EmployeeRepository(Config.getProperties());
        employeeService = new EmployeeService(employeeRepository);
    }

    @FXML
    private void login(ActionEvent event) throws Exception{
        String username = userField.getText();
        String password = passwordField.getText();

        if(employeeService.login(username, password)){
            FXMLLoader fxmlLoader = new FXMLLoader();
            fxmlLoader.setLocation(getClass().getResource("/applicationWindow.fxml"));
            Stage stage = (Stage) loginButton.getScene().getWindow();
            fxmlLoader.setController(new ApplicationController(stage));

            Parent root = fxmlLoader.load();
            Stage applicationStage = new Stage();

            applicationStage.setTitle("Application Window");
            applicationStage.setScene(new Scene(root, 1113, 711));
            stage.hide();
            applicationStage.show();

        }
        else{
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setContentText("Wrong Login Credentials");
            alert.showAndWait();
        }

    }

}
