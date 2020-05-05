import javafx.beans.property.ReadOnlyObjectWrapper;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.stage.Stage;
import javafx.util.Pair;
import javafx.util.converter.IntegerStringConverter;

import java.io.Serializable;
import java.rmi.RemoteException;
import java.rmi.server.RMIClientSocketFactory;
import java.rmi.server.RMIServerSocketFactory;
import java.rmi.server.UnicastRemoteObject;
import java.util.List;

public class ApplicationController extends UnicastRemoteObject implements EventObserver, Serializable {
    @FXML
    private TextField teamSearchField;

    @FXML
    private TableColumn<Pair<Event, Integer>, Integer> engineCapacityColumn;

    @FXML
    private Button searchButton;

    @FXML
    private ComboBox<Integer> engineBox;

    @FXML
    private TextField nameField;

    @FXML
    private Button addButton;

    @FXML
    private Button logoutButton;

    @FXML
    private TableColumn<Pair<Event, Integer>, Integer> idEventColumn;

    @FXML
    private TableColumn<Competitor, String> nameColumn;

    @FXML
    private TableColumn<Pair<Event, Integer>, Integer> numberCompetitorsColumn;

    @FXML
    private TableColumn<Competitor, String> teamColumn;

    @FXML
    private TableView<Competitor> competitorView;

    @FXML
    private TableColumn<Competitor, Integer> idCompetitorColumn;

    @FXML
    private TextField teamField;

    @FXML
    private TableView<Pair<Event, Integer>> eventView;

    CompetitorServices services;

    Employee user;

    Stage stage;

    Stage loginStage;

    ObservableList<Competitor> competitors;
    ObservableList<Pair<Event, Integer>> events;

    public ApplicationController() throws RemoteException {
        super();
    }

    public ApplicationController(int port) throws RemoteException {
        super(port);
    }

    public ApplicationController(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException {
        super(port, csf, ssf);
    }

    public void setServer(CompetitorServices services) {
        this.services = services;
    }

    public void setLoginStage(Stage stage){ this.loginStage = stage; }

    @FXML
    public void addClick(ActionEvent actionEvent) {
        try{
            int engineCapcity = engineBox.getSelectionModel().getSelectedItem();
            String name = nameField.getText();
            String team = teamField.getText();


            services.addCompetitor(name,team,engineCapcity);
            initCompetitor(team);

        }
        catch (Exception ex){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setContentText(ex.getMessage());
            alert.showAndWait();
        }
    }

    @FXML
    public void logOut(ActionEvent actionEvent) {
        logout();
        stage.close();
        loginStage.show();
    }
    @FXML
    public void searchClick(ActionEvent actionEvent) {
        try{
            initCompetitor(teamSearchField.getText());
        }
        catch (Exception ex){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setContentText(ex.getMessage());
            alert.showAndWait();
        }
    }



    public void logout() {
        try {
            this.services.logout(user, this);
        }
        catch (Exception e){
            System.out.println("Logout error" + e.getMessage());
        }
    }

    public void setUser(Employee employee) throws Exception{
        this.user = employee;
        initModel();
    }

    public void initModel() throws Exception {
        events.clear();
        List<Event> eventList = (List<Event>) services.findAllEvents();
        List<Integer> numberList = (List<Integer>) services.numberOfCompetitorsEvents();
        for(int i = 0; i < eventList.size(); i++){
            events.add(new Pair<>(eventList.get(i), numberList.get(i)));
        }
        eventView.setItems(events);
    }

    public void setStage(Stage stage) {
        this.stage = stage;
    }

    @FXML
    private void initialize() throws Exception{
        events = FXCollections.observableArrayList();
        competitors = FXCollections.observableArrayList();

        idCompetitorColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        teamColumn.setCellValueFactory(new PropertyValueFactory<>("team"));

        idEventColumn.setCellValueFactory(cellData->new ReadOnlyObjectWrapper<>(cellData.getValue().getKey().getId()));
        engineCapacityColumn.setCellValueFactory(cellData->new ReadOnlyObjectWrapper<>(cellData.getValue().getKey().getEngineCapacity()));
        numberCompetitorsColumn.setCellValueFactory(cellData -> new ReadOnlyObjectWrapper<>(cellData.getValue().getValue()));

        idEventColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        numberCompetitorsColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        engineCapacityColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));

        idCompetitorColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        nameColumn.setCellFactory(TextFieldTableCell.forTableColumn());
        teamColumn.setCellFactory(TextFieldTableCell.forTableColumn());

        ObservableList<Integer> engineList = FXCollections.observableArrayList();

        for(Event event : services.findAllEvents()){
            engineList.add(event.getEngineCapacity());
        }

        engineBox.setItems(engineList);

    }

    private void initCompetitor(String team) throws Exception{
        competitors.clear();
        for(Competitor competitor : services.findByTeam(team)){
            competitors.add(competitor);
        }
        competitorView.setItems(competitors);
    }


    @Override
    public void newCompetitorUpdate(Integer eventID) throws Exception {
        System.out.println("MotorCycle update");
        for(int i = 0; i < events.size(); i++){
            if(events.get(i).getKey().getId().equals(eventID)){
                Pair<Event,Integer> pair = new Pair<>(events.get(i).getKey(), events.get(i).getValue() + 1);
                events.set(i, pair);
            }
        }
        eventView.refresh();
    }
}
