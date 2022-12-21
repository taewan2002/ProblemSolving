package HW_1;
import java.util.Scanner;

public class hw_3 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter the Degrees: ");
        float Degrees = keyboard.nextFloat();
        System.out.print("Enter the Type: ");
        String type = keyboard.next();

        switch (type) {
            // case of F or f
            case "F":
            case "f":
                // 소숫점 3번째 자리에서 반올림한다(정확성을 높이기 위해)
                System.out.println("Celsius is " + 
                String.format("%.2f", 5 * (Degrees-32) / 9));
                break;
            // case of C or c
            case"C":
            case"c":
                // 소숫점 3번째 자리에서 반올림한다(정확성을 높이기 위해)
                System.out.println("Fahrenheit is " + 
                String.format("%.2f", 9 * Degrees / 5 + 32));
                break;
            default:
                // print ERROR message
                System.out.println("ERROR");
        }
    }
}

