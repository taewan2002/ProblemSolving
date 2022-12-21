/*
3. Write a program that demonstrates the operator % (modulo) by performing the followinf task:
- Use Scanner to read a floating-point value x.
- Compute x % 2.0 and store the result in y.
- Display x and y clearly labeled.
- Type cast x to an int value and store the result in z.
- Display x, z and z % 2 clearly labeled.
*/

package OOP22_Ch2.Problems;
import java.util.Scanner;

public class ModTester {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
    
        System.out.println("Enter a floating point value.");
        double y = keyboard.nextDouble();
        
        double x = y % 2.0;
        
        System.out.println( y + " mod 2.0 is  " + x);
        
        int q = (int) y;
        int z = q % 2;
        System.out.println( q + " mod 2 is  " + z);
    }
}
