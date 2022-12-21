package OOP22_Ch6;
import java.util.Scanner;

public class PetDemo{
    public static void main(String[] args){
        Pet3 yourPet = new Pet3("Jane Doe");
        System.out.println("My records on your pet are inaccurate."); 
        System.out.println("Here is what they currently say:"); 
        yourPet.writeOutput();

        Scanner keyboard = new Scanner(System.in);
        System.out.println("Please enter the correct pet name:");
        String correctName = keyboard.nextLine();
        yourPet.setName(correctName);

        System.out.println("Please enter the correct pet age:"); 
        int correctAge = keyboard.nextInt(); 
        yourPet.setAge(correctAge);
        
        System.out.println("Please enter the correct pet weight:"); 
        double correctWeight = keyboard.nextDouble(); 
        yourPet.setWeight(correctWeight);
        System.out.println("My updated records now say:");
        yourPet.writeOutput();
    }
}
