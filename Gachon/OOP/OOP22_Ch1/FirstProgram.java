package OOP22_Ch1;
import java.util.Scanner;

public class FirstProgram{
    public static void main(String[] args){
        System.out.println("Hello out there.");
        System.out.println("I will add two number for you.");
        System.out.println("Enter two whole numbers on a line:");
        
        int n1, n2;

        Scanner keyborard = new Scanner(System.in);
        n1 = keyborard.nextInt();
        n2 = keyborard.nextInt();

        System.out.println("The sum of those two numbers is");
        System.out.println(n1 + n2);
    }
}