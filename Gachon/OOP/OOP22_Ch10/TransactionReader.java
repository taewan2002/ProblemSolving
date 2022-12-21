package OOP22_Ch10;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.util.Scanner;

public class TransactionReader{
    public static void main(String[] args) {
        String fileName = "Transactions.txt";
        try{
            Scanner inputStream = new Scanner(new File(fileName));
            String line = inputStream.nextLine();
            double total = 0;
            while(inputStream.hasNextLine()){
                line = inputStream.nextLine();
                String[] ary = line.split(","); // ,를 기준으로 잘라서 ary에 넣기
                String SKU = ary[0];
                int quantity = Integer.parseInt(ary[1]); // String -> int
                double price = Double.parseDouble(ary[2]); // String -> double
                String description = ary[3];
                System.out.printf("Sold %d of %s (SKU: %s) at $%1.2f each.\n", quantity, description,SKU, price);
                total += quantity * price;
            }
            System.out.printf("Total sales: $%1.2f\n", total);
            inputStream.close();
        }
        catch(FileNotFoundException e){
            System.out.println("Cannot find file " + fileName);
        }
        catch(Exception e){
            System.out.println("Problem with input from file " + fileName);
        }
    }
}
