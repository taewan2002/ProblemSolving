package OOP22_Ch3;
import java.util.Scanner;

public class StringEqualityDemo2 {
    public static void main(String[] args){
        String s1, s2;
        System.out.println("Enter two lines of text:");

        Scanner keyboard = new Scanner(System.in);
        s1 = keyboard.nextLine();
        s2 = keyboard.nextLine();

        if (s1.compareTo(s2) < 0)
            System.out.println(s1 + " preceeds " + s2);
        else if (s1.compareTo(s2) > 0)
            System.out.println(s2 + " preceeds " + s1);
        else
            System.out.println("The two strings are equal.");
    }
}