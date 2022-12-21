package OOP22_Ch9;
import java.util.Scanner;

public class GotMilk {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        try{
            System.out.println("Enter number of donuts:");

            int donutCount = keyboard.nextInt(); 
            System.out.println("Enter number of glasses of milk:"); 
            
            int milkCount = keyboard.nextInt();
            
            if (milkCount < 1)
                throw new Exception("Exception: no milk!");
            double donutsPerGlass = donutCount / (double)milkCount;
            System.out.println(donutCount + " donuts."); 
            System.out.println(milkCount + " glasses of milk."); 
            System.out.println("You have " + donutsPerGlass + " donuts for each glass of milk.");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
            System.out.println("Go buy some milk.");
        }
        System.out.println("End of program.");
    }
}
