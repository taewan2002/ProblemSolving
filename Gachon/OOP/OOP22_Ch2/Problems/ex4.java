package OOP22_Ch2.Problems;

public class ex4 {
    public static void main(String[] args){
        int x = 10;

        System.out.println("Test 1 " + x * 3 * 2.0);
        System.out.println("Test 2 " + x * 3 + 2.0);
        
        /*
        Why the following java statement will not compile: 
        System.out.println("Test 3" + x * 3 - 2.0);
        */
    }
}
