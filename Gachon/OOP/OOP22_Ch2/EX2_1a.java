package OOP22_Ch2;
import java.util.Scanner;

public class EX2_1a {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        int n, n1, n2;

        n = keyboard.nextInt();

        n1 = n / 1000; // 1000s place
        n2 = n % 1000; // last 3 digit
        System.out.println(n1);

        n1 = n2 / 100; // 100s place
        n2 = n2 % 100; // last 2 digit
        System.out.println(n1);

        n1 = n2 / 10; // 10s place
        n2 = n2 % 10; // last 1 digit (ones place)
        System.out.println(n1);
        System.out.println(n2);
    }
}
