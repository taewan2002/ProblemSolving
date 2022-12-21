package HW_3;
import java.util.Scanner;

public class hw_6 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String data = new String();
        int[] arr = new int[26];

        /** while if input nothing or non period */
        System.out.println("Enter the data next line, if end the program enter nothing or non period");
        while(true){
            System.out.println("Enter the line of text ends with a period: ");
            /** get data end change UpperCase */
            data = keyboard.nextLine();
            data = data.toUpperCase();
            if (data.indexOf(".") == -1){
                System.out.println("End the program");
                break;
            }
            /** Add the data to array */
            for(int i=0; i<data.indexOf("."); i++){
                /** if data is ' ', continue */
                if(data.charAt(i) == ' ') continue;
                arr[(int)data.charAt(i)-65]++;
            }
            /** print each alphabet data  */
            for(int i=0; i<arr.length; i++){
                System.out.println((char)(i+65) + " is " + arr[i] + " in the text line.");
            }
        }
    }
}
