package HW_3;
import java.util.Scanner;

public class hw_5 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        double total = 0;
        double ratio;

        System.out.println("How many numbers will you enter?");
        int n = keyboard.nextInt();

        /** make new array size n */
        int[] num = new int[n];

        /** input the data n */
        System.out.println("Enter " + n + " integers, one per line:");
        for(int i=0; i<num.length; i++){
            num[i] = keyboard.nextInt();
            total += num[i];
        }

        /** print sum and ratio */
        System.out.println("The sum is " + (int)total);
        System.out.println("The numbers are: ");
        for(int i=0; i<num.length; i++){
            /** Math.floor(double) to int value remove under 0 */
            ratio = Math.floor(num[i]/total*100*10000) / 10000;
            System.out.println(num[i] + ", which is "+ ratio + "% of the sum.");
        }
    }
}
