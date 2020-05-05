import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

public class LoginController {
    private Stage stageParent;
    private CompetitorServices services;
    private ApplicationController appCtrl;

    @FXML
    private Button loginButton;

    @FXML
    private TextField userField;

    @FXML
    private PasswordField passwordField;

    public LoginController(){}

    public void setAppController(ApplicationController appCtrl) {
        this.appCtrl = appCtrl;
    }


    public void setStage(Stage stage) {
        this.stageParent = stage;
    }

    public void setServer(CompetitorServices services) {
        this.services = services;
    }

    @FXML
    public void login(ActionEvent actionEvent) {
        try {
            services.tryLogin(userField.getText(), passwordField.getText(),appCtrl);

            FXMLLoader cLoader = new FXMLLoader(getClass().getResource("/applicationWindow.fxml"));
            cLoader.setController(appCtrl);
            Parent cRoot = cLoader.load();

            Stage stage = new Stage();
            stage.setTitle("MotorCycle Menu" + userField.getText());
            stage.setScene(new Scene(cRoot));

            stage.setOnCloseRequest(new EventHandler<WindowEvent>() {
                @Override
                public void handle(WindowEvent windowEvent) {
                    appCtrl.logout();
                    System.exit(0);
                }
            });

            stage.show();

            Employee employee = new Employee(null, userField.getText(), passwordField.getText());
            appCtrl.initModel();
            appCtrl.setUser(employee);
            appCtrl.setStage(stage);
            appCtrl.setLoginStage(stageParent);

            stageParent.hide();

        }
        catch (Exception ex){
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Informare");
            alert.setContentText("Already logged in!!!");
            alert.showAndWait();
        }
    }
}
