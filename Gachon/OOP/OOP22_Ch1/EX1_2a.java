package OOP22_Ch1;
import java.util.Scanner;

public class EX1_2a {
    public static void main(String[] args){
        System.out.print("Enter your birth year : ");
        
        int by;

        Scanner keyboard = new Scanner(System.in);
        by = keyboard.nextInt();

        System.out.print("Your age is ");
        System.out.println(2022 - by + 1);
    }
}
