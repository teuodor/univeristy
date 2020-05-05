package GUI;

import Config.Config;
import Domain.Competitor;
import Domain.Event;
import Repository.CompetitorRepository;
import Repository.EmployeeRepository;
import Repository.EventRepository;
import Service.CompetitorService;
import Service.EmployeeService;
import Service.EventService;
import javafx.beans.property.ReadOnlyObjectWrapper;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.stage.Stage;
import javafx.util.converter.IntegerStringConverter;

import java.io.FileReader;
import java.util.Properties;


public class ApplicationController {

    @FXML
    private TextField teamSearchField;

    @FXML
    private TableColumn<Event, Integer> engineCapacityColumn;

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
    private TableColumn<Event, Integer> idEventColumn;

    @FXML
    private TableColumn<Competitor, String> nameColumn;

    @FXML
    private TableColumn<Event, Integer> numberCompetitorsColumn;

    @FXML
    private TableColumn<Competitor, String> teamColumn;

    @FXML
    private TableView<Competitor> competitorView;

    @FXML
    private TableColumn<Competitor, Integer> idCompetitorColumn;

    @FXML
    private TextField teamField;

    @FXML
    private TableView<Event> eventView;

    private EventService eventService;
    private CompetitorService competitorService;

    private ObservableList<Event> events;
    private ObservableList<Competitor> competitors;
    private Stage loginStage;

    public ApplicationController(Stage stage){
        this.loginStage = stage;
    }

    @FXML
    private void initialize() throws Exception{
        EventRepository eventRepository = new EventRepository(Config.getProperties());
        eventService = new EventService(eventRepository);

        CompetitorRepository competitorRepository = new CompetitorRepository((Config.getProperties()));
        competitorService = new CompetitorService(competitorRepository, eventRepository);

        events = FXCollections.observableArrayList();
        competitors = FXCollections.observableArrayList();
        loadEvents();

        idCompetitorColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        teamColumn.setCellValueFactory(new PropertyValueFactory<>("team"));

        idEventColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        engineCapacityColumn.setCellValueFactory(new PropertyValueFactory<>("engineCapacity"));
        numberCompetitorsColumn.setCellValueFactory(cellData -> new ReadOnlyObjectWrapper<>(numberParticipants(cellData.getValue())));

        idEventColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        numberCompetitorsColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        engineCapacityColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));

        idCompetitorColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        nameColumn.setCellFactory(TextFieldTableCell.forTableColumn());
        teamColumn.setCellFactory(TextFieldTableCell.forTableColumn());

        ObservableList<Integer> engineList = FXCollections.observableArrayList();

        for(Event event : events){
            engineList.add(event.getEngineCapacity());
        }

        engineBox.setItems(engineList);

        eventView.setItems(events);

    }
    @FXML
    private void searchClick(ActionEvent event) {
        try{
            String team = teamSearchField.getText();
            if(team.compareTo("") == 0)
                throw new Exception("Team can't be null");
            loadCompetitors(team);
            competitorView.setItems(competitors);
        }
        catch (Exception exception){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setContentText(exception.getMessage());
            alert.showAndWait();
            System.out.println(exception.toString());
        }
    }

    @FXML
    private void addClick(ActionEvent event) {
        try{
            String name = nameField.getText();
            String team = teamField.getText();
            Integer engineCapacity = engineBox.getSelectionModel().getSelectedItem();

            competitorService.addCompetitor(name, team, engineCapacity);

            loadCompetitors(team);
            competitorView.setItems(competitors);
            loadEvents();
            eventView.setItems(events);

        }
        catch (Exception exception){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setContentText(exception.getMessage());
            alert.showAndWait();
            System.out.println(exception.toString());
        }
    }

    @FXML
    private void logOut(ActionEvent event) {
        Stage stage = (Stage) logoutButton.getScene().getWindow();
        stage.close();
        loginStage.show();
    }

    private void loadCompetitors(String team){
        competitors.clear();
        for(Competitor competitor : competitorService.findByTeam(team))
            competitors.add(competitor);
    }

    private void loadEvents(){
        events.clear();
        for(Event event : eventService.findAll())
            events.add(event);
    }

    private Integer numberParticipants(Event event){
        Integer tmp = 0;
        for(Competitor competitor : competitorService.findAll()){
            if(competitor.getEventList().size() > 0)
            for(Event event1 : competitor.getEventList()){
                if(event1.getEngineCapacity().equals(event.getEngineCapacity()))
                    tmp++;
            }

        }

        return tmp;
    }

}
