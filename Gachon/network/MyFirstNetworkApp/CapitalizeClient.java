package MyFirstNetworkApp;
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class CapitalizeClient {
    public static void main(String[] args) throws Exception{

        var socket = new Socket("localhost", 7777);
        System.out.println("Enter lines of text then Ctrl+D or Ctrl+C to quit");
        var scanner = new Scanner(System.in);
        var in = new Scanner(socket.getInputStream());
        var out = new PrintWriter(socket.getOutputStream(), true);
        
        while (scanner.hasNextLine()){
            out.println(scanner.nextLine());
            System.out.println(in.nextLine());
        }
    }
}
