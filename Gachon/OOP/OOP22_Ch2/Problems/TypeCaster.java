/*
2. Write a program that demonstrates type casting of double values by performing the following task:
- Use Scanner to read a floating-point(double) value x.
- Type cast x to an int value and store the result in y.
- Display x and y clearly labeled.
- Type cast x to a byte value and store the result in z.
- Display x and z clearly labeled.
*/

package OOP22_Ch2.Problems;
import java.util.Scanner;

public class TypeCaster {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Enter a floating point value.");
        double y = keyboard.nextDouble();
        
        int x = (int) y;
        
        System.out.println("The floating value " + y + " type casts to the integer value " + x);
        
        byte z = (byte) y;
        System.out.println("The floating value " + y + " type casts to the byte value " + z);
        
    }
}
