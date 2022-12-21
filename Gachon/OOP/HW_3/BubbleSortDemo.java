package HW_3;

public class BubbleSortDemo { 
     public static void main(String[] args) {
        int[] b = {7, 5, 11, 2, 16, 4, 18, 14, 12, 30}; 

        System.out.println("Array values before sorting:"); 
        int i; 
    
        for (i = 0; i < b.length; i++) 
            System.out.print(b[i] + " "); 
    
        System.out.println();

        BubbleSort.sort(b);

        System.out.println("Array values after sorting:"); 
        for (i = 0; i < b.length; i++) 
                System.out.print(b[i] + " "); 
    
        System.out.println(); 
    } 
} 
