package HW_4;

public class Employee extends Person {
    public int id;
    public String department;

    public Employee(){
        id = 0;
        department = "";
    }

    public Employee(int newId){
        id = newId;
        department = "";
    }

    public Employee(String newDepartment){
        id = 0;
        department = newDepartment;
    }

    public Employee(String newName, String newDepartment, int newId){
        super(newName);
        department = newDepartment;
        id = newId;
    }

    public void reset(String newString, int newId){
        id = newId;
        department = newString;
    }

    public void setId(int newId){
        /** set ID */
        id = newId;
    }

    public void setDepartment(String newDepartment){
        /** set Department */
        department = newDepartment;
    }

    public int getId(){
        /** get ID */
        return id;
    }

    public String getDepartment(){
        /** get Department */
        return department;
    }
    
    public void writeOutput(){
        super.writeOutput(); // print Name:
        System.out.println("ID: " + getId());
        System.out.println("Department: " + getDepartment());
    }
}