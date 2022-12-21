package HW_1;
import java.util.Scanner;

public class hw_1 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String s1 = keyboard.next();
        String s2 = keyboard.next();
        String s3 = keyboard.next();

        if (s1.compareTo(s2) <= 0){
            if (s1.compareTo(s3) <= 0){
                if (s2.compareTo(s3) <= 0)
                    // if s1 <= s2 <= s3
                    System.out.println(s2);
                else
                    // if s1 <= s3 < s2
                    System.out.println(s3);
            }
            else
                // if s3 <= s1 < s2
                System.out.println(s1);
        }
        else if (s2.compareTo(s1) < 0){
            if (s2.compareTo(s3) <= 0){
                if (s1.compareTo(s3) <= 0)
                    // if s2 < s1 <= s3
                    System.out.println(s1);
                else
                    // if s2 <= s3 < s1
                    System.out.println(s3);
            }
            else
                // if s3 < s2 < s1
                System.out.println(s2);
        }
    }
}
