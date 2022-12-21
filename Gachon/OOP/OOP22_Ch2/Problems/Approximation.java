/*
1. Write a program that demonstrates the approximate nature of floating-point values by performing the following task:
- Use Scanner to read a  floating-point value x.
- Compute 1.0 / x and store the result in y.
- Display x, y and the procuct of x and y.
- Subtract 1 from the product of x and display the result.
*/

package OOP22_Ch2.Problems;
import java.util.Scanner;

public class Approximation {
    public static void main(String[] args) {
        
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Enter a floating point value.");
        double x = keyboard.nextDouble();
        
        double y = 1.0/x;
        
        if(x*y < 1.0)
            System.out.println("x*y < 1.0");
        else if(x*y >1.0)
            System.out.println("x*y > 1.0");
        else
            System.out.println("x*y = 1.0");
        
        System.out.println("The difference of x*y and 1 is " + (x*y - 1.0));

        
     
    }
}
