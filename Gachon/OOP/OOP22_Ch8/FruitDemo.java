package OOP22_Ch8;
import java.util.Arrays;

public class FruitDemo{
    public static void main(String[] args){

        Fruit[] fruits = new Fruit[4];
        fruits[0] = new Fruit("Orange");
        fruits[1] = new Fruit("Apple");
        fruits[2] = new Fruit("Kiwi");
        fruits[3] = new Fruit("Durian");

        Arrays.sort(fruits);
        
         // Output the sorted array of fruits
        for (Fruit f : fruits){
            System.out.println(f.getName());
        } 
    }
}