package OOP22_Ch2;

import java.util.Scanner;

public class EggBasket2 {

    public static void main(String[] args){
        int numberOfBaskets;
        int eggsPerBasket;
        int totalEggs;

        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter the number of eggs in each basket:");
        eggsPerBasket = keyboard.nextInt();
        System.out.println("Enter the number of baskets:");
        numberOfBaskets = keyboard.nextInt();

        System.out.println("If you have");
        System.out.println(eggsPerBasket + " eggs per basket and");
        System.out.println(numberOfBaskets + " baskets, then");
        totalEggs = eggsPerBasket * numberOfBaskets;
        System.out.println("the total number of eggs is " + totalEggs);

        System.out.println("Now we take two eggs out of each basket.");
        eggsPerBasket -= 2;
        System.out.println("You now have");
        System.out.println(eggsPerBasket + " eggs per basket and");
        System.out.println(numberOfBaskets + " basket");
        totalEggs = eggsPerBasket * numberOfBaskets;
        System.out.println("The new total number of eggs is " + totalEggs);
    }
}
