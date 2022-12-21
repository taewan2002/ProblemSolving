package OOP22_Ch1;
import java.util.Scanner;

public class EX1_2b {
    public static void main(String[] args){
        System.out.print("Enter two integers : ");
        
        int n1, n2;

        Scanner keyboard = new Scanner(System.in);
        n1 = keyboard.nextInt();
        n2 = keyboard.nextInt();

        System.out.print("There is ");
        System.out.print(n2 - n1 + 1);
        System.out.print("integers between them");
    }
}
