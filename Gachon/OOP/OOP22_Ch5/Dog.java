package OOP22_Ch5;

public class Dog {
    public String name; //Instance Variables 
    public String breed;
    public int age;

    public void writeOutput(){ //메서드
        System.out.println("Name: " + name);
        System.out.println("Breed: " + breed);
        System.out.println("Age in dog years: " + age);
        System.out.println("Age in human years: " + getAgeHumanYears());
    }
    public int getAgeHumanYears(){
        int humanAge = 0;
        if(age <= 2){
            humanAge = age * 11;
        }
        else{
            humanAge = 22 + (age - 2) * 5;
        }
        return humanAge;
    }
}
