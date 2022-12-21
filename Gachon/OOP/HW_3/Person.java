package HW_3;

public class Person {
    static private String name = new String();
    static private int age;
    

    public Person(String newName, int newAge){
        /** set name and age */
        name = newName;
        age = newAge;
    }
    public Person(){
        /** default constructor */
        this("No name yet", 0);
    }

    public static Person createAdult(){
        /** set "An adult", 21 */
        Person x = new Person();
        x.setName("An adult");
        x.setAge(21);
        return x;
    }

    public static Person createToddler(){
        /** set "A toddler", 2 */
        Person x = new Person();
        x.setName("A toddler");
        x.setAge(2);
        return x;
    }

    public static Person createPreschooler(){
        /** set "A preschooler", 5 */
        Person x = new Person();
        x.setName("A preschooler");
        x.setAge(5);
        return x;
    }
    
    public static Person createAdolescent(){
        /** set "An adolescent", 9 */
        Person x = new Person();
        x.setName("An adolescent");
        x.setAge(9);
        return x;
    }

    public static Person createTeenager(){
        /** set "A teenager", 15 */
        Person x = new Person();
        x.setName("A teenager");
        x.setAge(15);
        return x;
    }

    void setName(String frist, String last){
        name = frist + " " + last;
    }

    void setName(String newName){
        name = newName;
    }

    void setAge(int newAge){
        age = newAge;
    }

    String getName(){
        return name;
    }
    int getAge(){
        return age;
    }


    public static void main(String[] args) { 
        Person y = new Person(); 
        System.out.println("Testing the default constructor"); 
        System.out.println("Oject has name " + y.getName() + " and age " + y.getAge()); 
        System.out.println("\nCreating each of the specialized instances"); 
        Person x; 
        
        x = Person.createToddler(); 
        System.out.println("Created object with name " + x.getName() + " and age " + x.getAge()); 
        
        x = Person.createPreschooler(); 
        System.out.println("Created object with name " + x.getName() + " and age " + x.getAge());

        x = Person.createAdolescent(); 
        System.out.println("Created object with name " + x.getName() + " and age " + x.getAge()); 
        
        x = Person.createTeenager(); 
        System.out.println("Created object with name " + x.getName() + " and age " + x.getAge()); 
        
        x = Person.createAdult(); 
        System.out.println("Created object with name " + x.getName() + " and age " + x.getAge()); 
        
        System.out.println("\nTesting set ‐ Name should be Bobby with age 10"); 
        x.setName("Bobby"); 
        x.setAge(10); 
        System.out.println("Oject has name " + x.getName() + " and age " + x.getAge()); 
        
        System.out.println("\nTesting the alternate set method ‐ name change to Jane Doe"); 
        x.setName("Jane", "Doe"); 
        x.setAge(10); 
        System.out.println("Oject has name " + x.getName() + " and age " + x.getAge()); 
    }
}
