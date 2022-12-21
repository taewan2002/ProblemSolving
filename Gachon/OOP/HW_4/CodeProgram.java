package HW_4;
import java.util.Scanner;

public class CodeProgram {
    public static void main(String[] args){
        System.out.println("Welcome to the Cipher program");

        Scanner reader = new Scanner(System.in);

        System.out.println("What is the key (shift amount) for your code?"); 
        int shift = reader.nextInt();
        SubstitutionCipher coder = new SubstitutionCipher(shift); 
        
        boolean done = false;

        while(!done){
            // Make sure the return is used up
            String rest = reader.nextLine();
            System.out.println("Enter a message to be encoded or decoded."); 
            String message = reader.nextLine();

            System.out.println("Encode (E) or Decode (D)");
            String response = reader.next(); 
            response = response.toLowerCase(); 
            if(response.equals("e"))
                System.out.println("Encodes to: " + coder.encode(message));
            else if(response.equals("d"))
                System.out.println("Decodes to: " + coder.decode(message));

            System.out.println("Do you want to do another message (Y)"); 
            response = reader.next();
            response = response.toLowerCase();
            if(!response.equals("y"))
                done = true;
        }
    }
}