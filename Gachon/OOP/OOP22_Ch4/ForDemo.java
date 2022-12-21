package OOP22_Ch4;
import java.util.Scanner;

public class ForDemo {
    public static void main(String[] args){
        int countDown;
        for (countDown = 3; countDown >= 0; countDown--){
            System.out.println(countDown);
            System.out.println("and counting.");
        }
        System.out.println("Blast off!");
    }
}
