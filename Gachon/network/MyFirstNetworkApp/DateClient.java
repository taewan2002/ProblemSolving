package MyFirstNetworkApp;
import java.util.Scanner;
import java.net.Socket;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class DateClient {
    public static void main(String[] args) throws IOException{

        Socket socket = new Socket("127.0.0.1", 59090);

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        System.out.println("Server response: " + in.readLine());
        socket.close();
    }
}

