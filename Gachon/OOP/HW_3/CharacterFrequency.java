package HW_3;
import java.util.Scanner;

public class CharacterFrequency {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String phonenum = new String();
        /** make new array */
        int[] number = new int[10];

        /** Input the data */
        System.out.print("Enter the phone number(non blank): ");
        phonenum = keyboard.next();

        for(int i=0; i<phonenum.length(); i++){
            /** each index's number add number array */
            /** Character.getNumbericValuse is change char to int */
            number[Character.getNumericValue(phonenum.charAt(i))]++;
        }

        for(int i=0; i<number.length; i++){
            /** print number array's data */
            System.out.println(i + " is " + number[i] + " amount in the array.");
        }
    }
}
