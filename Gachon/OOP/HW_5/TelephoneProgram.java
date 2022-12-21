package HW_5;
import java.io.*;
import java.util.*;

public class TelephoneProgram {
    public static void main(String[] args) {

        Scanner keyboard = new Scanner(System.in);

        /** write the data in "numbers.bin" */
        PrintWriter outputStream = null;
        try {
            outputStream = new PrintWriter("numbers.bin");
        } 
        catch (FileNotFoundException e) {
            System.out.println("Error opening the file numbers.bin for writing");
            System.exit(0);
        }

        // Write back the array
        while(true){
            String telNumberString = keyboard.nextLine();
            System.out.println(telNumberString.length());
            if(telNumberString.length() != 13) break;
            outputStream.println(telNumberString);
        }
        outputStream.close();

        /** file open and read */
        Scanner inputFile = null;
        try {
            inputFile = new Scanner(new File("numbers.bin"));
        } 
        catch (FileNotFoundException ex) {
            System.out.println("Error opening the file numbers.bin for reading");
            System.exit(0);
        }

        // See how many numbers are in the file
        int count = 0;
        while (inputFile.hasNext()) {
            String telNumberString = inputFile.next();
            TelephoneNumber t = null;
            try {
                System.out.println(telNumberString);
                t = new TelephoneNumber(telNumberString);
                count++;
            } 
            catch (InvalidTelephoneFormatException ex) {
                System.out.println("Bad telephone number format " + ex.getMessage());
            }
            // System.out.println("Read the number " + t);
        }
        inputFile.close();
        
        // // Create an array and then reread the file and put in the phone numbers;
        // TelephoneNumber numbers[] = new TelephoneNumber[count];

        // try {
        //     inputFile = new Scanner(new File("numbers.bin"));
        // } catch (FileNotFoundException ex) {
        //     System.out.println("Error opening the file numbers.txt for reading");
        //     System.exit(0);
        // }

        // count = 0;
        // while (inputFile.hasNext()) {
        //     String telNumberString = inputFile.next();
        //     TelephoneNumber t = null;
        //     try {
        //         t = new TelephoneNumber(telNumberString);
        //         numbers[count] = t;
        //         System.out.println("Number " + count + " is " + t);
        //         count++;
        //     } catch (InvalidTelephoneFormatException ex) {
        //     }
        // }
        // inputFile.close();

        // TelephoneNumber newNumber = null;

        // System.out.println("Change a number (c) or add a number (a)");
        // String response = keyboard.next().toLowerCase();
        // if (response.equals("c")) {
        //     System.out.println("Which number do you want to change (enter the index)");
        //     int index = keyboard.nextInt();
        //     System.out.println("Enter the phone number");
        //     String phone = keyboard.next();

        //     try {

        //         newNumber = new TelephoneNumber(phone);
        //     } catch (InvalidTelephoneFormatException ex) {
        //         System.out.println("Sorry, bad format for the number" + ex.getMessage());
        //     }

        //     if (newNumber != null)
        //         numbers[index] = newNumber;
        // } else if (response.equals("a")) {
        //     System.out.println("Enter the phone number to add");
        //     String phone = keyboard.next();

        //     try {

        //         newNumber = new TelephoneNumber(phone);
        //     } catch (InvalidTelephoneFormatException ex) {
        //         System.out.println("Sorry, bad format for the number" + ex.getMessage());
        //     }

        // }

        
    }

}
