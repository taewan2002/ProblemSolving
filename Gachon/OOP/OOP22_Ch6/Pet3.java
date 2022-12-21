package OOP22_Ch6;

public class Pet3 {
    private String name;
    private int age; //in years 
    private double weight; //in pounds

    public Pet3(String initialName, int initialAge, double initialWeight){
        set(initialName, initialAge, initialWeight);
    }

    public Pet3(String initialName){
        this(initialName, 0, 0);
    }

    public Pet3(int initialAge){
        this("No name yet.", initialAge, 0);
    }
    
    public Pet3(double initialWeight){
        this("No name yet.", 0, initialWeight);
    }

    public Pet3(){
        this("No name yet.", 0, 0);
    }

    public void setPet(String newName, int newAge, double newWeight){
        set(newName, newAge, newWeight);
    }
    
    public void setName(String newName){
        set(newName, age, weight); //age and weight unchanged 
    }
    
    public void setAge(int newAge){
        set(name, newAge, weight); //name and weight unchanged 
    }
    
    public void setWeight(double newWeight){
        set(name, age, newWeight); //name and age unchanged 
    }
    
    private void set(String newName, int newAge, double newWeight){
        name = newName;
        if ((newAge < 0) || (newWeight < 0)){
            System.out.println("Error: Negative age or weight.");
            System.exit(0);
        }
        else{
            age = newAge;
            weight = newWeight;
        }
    }

    public String getName(){
        return name;
    }

    public int getAge(){
        return age; 
    }

    public double getWeight(){
        return weight;
    }

    public void writeOutput(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age + " years");
        System.out.println("Weight: " + weight + " pounds");
    }
}
