package OOP22_Ch2;

import java.util.Scanner;

public class EggBaskets{
    public static void main(String[] args){
        int numberOfBaskets, eggPerBasket, totalEggs;

        Scanner keyborard = new Scanner(System.in);

        System.out.print("Enter the number of baskets: ");
        numberOfBaskets = keyborard.nextInt();

        System.out.print("Enter the egg per baskets: ");
        eggPerBasket = keyborard.nextInt();

        totalEggs = numberOfBaskets * eggPerBasket;

        System.out.println("If you have");
        System.out.println(eggPerBasket + " eggs per basket and");
        System.out.println(numberOfBaskets + " baskets, then");
        System.out.println("the total nuber of eggs is " + totalEggs);
    }
}