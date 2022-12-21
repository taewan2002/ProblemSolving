package OOP22_Ch2;
import java.util.Scanner;

public class EX2_1b {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Input a degree in Fahrenheit:");
        double fahrenheit = keyboard.nextDouble();
        double celsius = (5 * (fahrenheit - 32.0)) / 9.0;

        System.out.println(fahrenheit + " degree in Fahrenheit is equal to " + celsius + " in Celsius.");
    }
}
