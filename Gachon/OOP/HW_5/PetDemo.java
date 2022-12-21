package HW_5;

import java.io.*;
import java.util.Scanner;

public class PetDemo {
    public static void main(String[] args) {
        String file;
        String type;

        String name;
        int age;
        int weight;

        Scanner keyboard = new Scanner(System.in);

        try {
            do {
                System.out.println("Enter file name");
                file = keyboard.nextLine();
                System.out.println("write or read(W/R): ");
                type = keyboard.next();
                keyboard.nextLine();
                if(type.equalsIgnoreCase("w")) {
                    /** write data */
                    ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(file));
                    do {
                        System.out.println("Enter name: ");
                        name = keyboard.nextLine();
                        System.out.println("Enter age: ");
                        age = keyboard.nextInt();
                        System.out.println("Enter weight: ");
                        weight = keyboard.nextInt();
                        keyboard.nextLine();
                        Pet write = new Pet(name,age,weight);
                        outputStream.writeObject(write);
                        System.out.println("Enter the more data? (Y/N): ");
                        type = keyboard.nextLine();
                    }while(type.equalsIgnoreCase("y"));
                    outputStream.close();
                }
                else {
                    /** read data */
                    ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(file));
                    Pet read = null;
                    while(true) {
                        read = (Pet)inputStream.readObject();
                        read.writeOutput();
                    }
                }
                System.out.println("more read write?(Y/N): ");
                type = keyboard.nextLine();
            }while(type.equalsIgnoreCase("y"));
        }
        catch(FileNotFoundException e) {
            System.out.println("FileNotFoundException ERROR\n");
            System.exit(0);
        }
        catch(EOFException e){
            System.out.println("EOFException ERROR\n");
            System.exit(0);
        }
        catch(IOException e){
            System.out.println("IOException ERROR\n");
            System.exit(0);
        }
        catch(Exception e) {
            System.out.println("Exception ERROR\n");
            System.exit(0);
        }
    }
}