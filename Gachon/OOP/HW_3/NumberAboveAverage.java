package HW_3;
import java.util.Scanner;

public class NumberAboveAverage {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        /** make new array */
        float[] temp = new float[10];
        float total = 0;

        System.out.println("Enter the temperature of 10 days: ");

        /** Input data in array */
        for(int i=0; i < temp.length; i++){
            temp[i] = keyboard.nextFloat();
            /** sum all the data */
            total += temp[i];
        }

        for(int i=0; i < temp.length; i++){
            /** total / temp.length is average */
            if (total / temp.length < temp[i])
                System.out.println("Over average temperature is " + temp[i]);
        }
    }
}
