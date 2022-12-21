package OOP22_Ch2.Problems;
import java.util.Scanner;

public class ex5678 {
    public static void main(String[] args){
        /* 
        5. Write some java statements that use the String methods indexOf and substring to find the first word in a string.
        We define word to be a string of characters that does not include whitespace. For example, the first word of the string
        " Hello, my good friend!" is the string "Hello," and the second word is the string "my".
        */
        // Exercise 5
        String sentence = "  Hello, my good friend!";
        
        sentence = sentence.trim(); // 양쪽 끝 공백 제거
        int space = sentence.indexOf(" "); // 첫번째 공백의 인덱스를 반환
        String word = sentence.substring(0, space); // 첫번째 인덱스부터 공백까지 문자열 분리
        
        System.out.println("The first word is: " + word);

        // Exercise 5-2
        String rest = sentence.substring(space).trim();
        space = rest.indexOf(" ");
        String secondWord = rest.substring(0, space);
        
        System.out.println("The second word is: " + secondWord);

        // Exercise 6
        System.out.println("\"\tTest\\\\\rIt\'"); 
        System.out.println("\"\tTest\\\\\nIt\'");
        
        
        // Exercise 7
        System.out.println("one\ntwo\nthree");
        

        // Exercise 8
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter a string.");
        int n = keyboard.nextInt();
        String s = keyboard.next();
        System.out.println("n is " + n);
        System.out.println("s is " + s);
    }
}
