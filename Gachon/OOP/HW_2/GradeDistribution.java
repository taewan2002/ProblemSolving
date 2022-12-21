package HW_2;
import java.util.Scanner;

public class GradeDistribution {
    private int A = 0;
    private int B = 0;
    private int C = 0;
    private int D = 0;
    private int F = 0;
    private float n;

    void Read_data(){
        Scanner keyboard = new Scanner(System.in);

        /** Read A count */
        System.out.print("Enter the A count: ");
        A = keyboard.nextInt();

        /** Read B count */
        System.out.print("Enter the B count: ");
        B = keyboard.nextInt();

        /** Read C count */
        System.out.print("Enter the C count: ");
        C = keyboard.nextInt();

        /** Read D count */
        System.out.print("Enter the D count: ");
        D = keyboard.nextInt();
        
        /** Read F count */
        System.out.print("Enter the F count: ");
        F = keyboard.nextInt();
    }

    void writeOutput(){
        Ratio();
        Graph();
    }

    void Ratio(){
        n = 100 / getTotalCount();
        System.out.println();
        /** print each Ratio */
        // n개의 퍼센트값
        // n * 등급 = 각 등급의 퍼센트
        System.out.println(String.format("A ratio is %.0f", getAcount() * n) + "%");
        System.out.println(String.format("B ratio is %.0f", getBcount() * n) + "%");
        System.out.println(String.format("C ratio is %.0f", getCcount() * n) + "%");
        System.out.println(String.format("D ratio is %.0f", getDcount() * n) + "%");
        System.out.println(String.format("F ratio is %.0f", getFcount() * n) + "%");
        System.out.println();
    }

    void Graph(){
        /** print each graph */
        System.out.print("A: ");
        for(int i=0; i < Math.round((getAcount() * n )/ 2); i++){
            System.out.print("*");
        }
        System.out.print("\nB: ");
        for(int i=0; i < Math.round((getBcount() * n )/ 2); i++){
            System.out.print("*");
        }
        System.out.print("\nC: ");
        for(int i=0; i < Math.round((getCcount() * n )/ 2); i++){
            System.out.print("*");
        }
        System.out.print("\nD: ");
        for(int i=0; i < Math.round((getDcount() * n )/ 2); i++){
            System.out.print("*");
        }
        System.out.print("\nF: ");
        for(int i=0; i < Math.round((getFcount() * n )/ 2); i++){
            System.out.print("*");
        }
        System.out.println();
    }

    float getAcount(){
        /** return A data */
        return A;
    }
    float getBcount(){
        /** return B data */
        return B;
    }
    float getCcount(){
        /** return C data */
        return C;
    }
    float getDcount(){
        /** return D data */
        return D;
    }
    float getFcount(){
        /** return F data */
        return F;
    }
    float getTotalCount(){
        /** return total count data */
        return A + B + C + D + F;
    }
    public static void main(String[] args){
        GradeDistribution Grade = new GradeDistribution();
        Grade.Read_data();
        Grade.writeOutput();
    }
}
