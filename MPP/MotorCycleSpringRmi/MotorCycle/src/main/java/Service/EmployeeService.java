package Service;

import Domain.Employee;
import Repository.EmployeeRepository;

public class EmployeeService {
    private EmployeeRepository employeeRepository;

    public EmployeeService(EmployeeRepository repository) {
        employeeRepository = repository;
    }

    public Boolean login(String username, String password){

        for(Employee employee : employeeRepository.findAll()){
            if (employee.getUsername().equals(username))
                return employee.getPassword().equals(password);
        }
        return false;
    }
}
