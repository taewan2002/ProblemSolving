package HW_1;
import java.util.Scanner;

public class hw_2 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        
        String s = keyboard.nextLine();

        // "?"는 아스키코드 63, "!"는 아스키코드 33
        if (s.length() % 2 == 0 && s.charAt(s.length() - 1) == 63){
            System.out.println("Yes");
        }
        else if (s.length() % 2 != 0 && s.charAt(s.length() - 1) == 63){
            System.out.println("No");
        }
        else if (s.charAt(s.length() - 1) == 33){
            System.out.println("Wow");
        }
        else{
            System.out.println("\"" + s + "\"");
        }
    }
}
