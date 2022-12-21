package HW_2;
import java.util.Scanner;
/**
Class for the purchase of one kind of item, such as 3 oranges. Prices are set supermarket style, such as 5 for $1.25.
*/
public class Purchase
{
    private String name;
    private int groupCount;
    private double groupPrice;
    private int numberBought;
    private float totalBill = 0;

    public void setName(String newName){
        name = newName;
    }
    /** Sets price to count pieces for $costForCount. */
    public void setPrice(int count, double costForCount) {
        if ((count <= 0) || (costForCount <= 0)){
            System.out.println("Error: Bad parameter in " + "setPrice.");
            System.exit(0);
        }
        else{
            groupCount = count;
            groupPrice = costForCount;
        }
    }

    public void setNumberBought(int number){
        if (number <= 0){
            System.out.println("Error: Bad parameter in " + "setNumberBought.");
            System.exit(0);
        }
        else
            numberBought = number;
    }

    /** Reads from keyboard the price and number of a purchase. */
    public void readInput(){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter name of item you are purchasing:");
        name = keyboard.nextLine();
        
        System.out.println("Enter price of item as two numbers.");
        System.out.println("For example, 3 for $2.99 is entered as");
        System.out.println("3 2.99");
        System.out.println("Enter price of item as two numbers, " + "now:");

        groupCount = keyboard.nextInt();
        groupPrice = keyboard.nextDouble();
        while ((groupCount <= 0) || (groupPrice <= 0)){ //Try again:
            System.out.println("Both numbers must " + "be positive. Try again.");
            System.out.println("Enter price of " + "item as two numbers.");
            System.out.println("For example, 3 for " + "$2.99 is entered as");
            System.out.println("3 2.99");
            System.out.println("Enter price of item as two numbers, now:");
            groupCount = keyboard.nextInt();
            groupPrice = keyboard.nextDouble();
        }

        System.out.println("Enter number of items purchased:");
        numberBought = keyboard.nextInt();
        while (numberBought <= 0) { //Try again:
            System.out.println("Number must be positive. " + "Try again.");
            System.out.println("Enter number of items purchased:");
            numberBought = keyboard.nextInt();
        }
    }
    /** Displays price and number being purchased. */
    public void writeOutput(){
        System.out.println(numberBought + " " + name);
        System.out.println("at " + groupCount + " for $" + groupPrice);
        System.out.println(String.format("Unit cost is %.2f", getUnitCost()));
        System.out.println(String.format("Total cost is %.2f",  getTotalCost()));
        totalBill += getTotalCost();
        System.out.println();
    }

    public void totalBill(){
        System.out.println(String.format("Total Bill each thing: %.2f", totalBill));
    }

    public String getName(){
        return name;
    }

    public double getTotalCost(){
        return (groupPrice / groupCount) * numberBought;
    }
    public double getUnitCost(){
        return groupPrice / groupCount;
    }

    public int getNumberBought(){
        return numberBought;
    }

    public static void main(String[] args){
        Purchase purchase = new Purchase();
        /** buy Oranges */
        purchase.setName("Oranges");
        purchase.setPrice(10, 2.99);
        purchase.setNumberBought(24);
        purchase.writeOutput();

        /** buy eggs */
        purchase.setName("Eggs");
        purchase.setPrice(12, 1.69);
        purchase.setNumberBought(36);
        purchase.writeOutput();

        /** buy apples */
        purchase.setName("Apples");
        purchase.setPrice(3, 1);
        purchase.setNumberBought(20);
        purchase.writeOutput();

        /** buy watermelons */
        purchase.setName("Watermelons");
        purchase.setPrice(1, 4.39);
        purchase.setNumberBought(2);
        purchase.writeOutput();

        /** buy bagels */
        purchase.setName("Bagels");
        purchase.setPrice(6, 3.5);
        purchase.setNumberBought(12);
        purchase.writeOutput();

        /** totalBill */
        purchase.totalBill();
    }
}
       