package HW_4;

public class Faculty extends Employee{
    public String title;

    public Faculty(){
        super();
        title = "";
    }
    
    public Faculty(String newName, String newDepartment, int newId, String newTitle){
        super(newName, newDepartment, newId);
        title = newTitle;
    }

    public void reset(String t){
        /** reset */
        title = t;
    }

    public void setTitle(String t){
        /** set title */
        title = t;
    }

    public String getTitle(){
        /** get title */
        return title;
    }
    
    public void writeOutput(){
        super.writeOutput(); // print name, department, id
        System.out.println("Title: " + getTitle());
    }
}
