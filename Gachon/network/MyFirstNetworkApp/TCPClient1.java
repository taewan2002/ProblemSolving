package MyFirstNetworkApp;
import java.io.*;
import java.net.*;

public class TCPClient1 {
    public static void main(String[] args) throws Exception{
        String sentence;
        String modifiedSentence;
        String serverIP = "127.0.0.1";
        int nPort = 6789;

        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        
        Socket clientSocket = new Socket(serverIP, nPort);

        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());

        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        sentence = inFromServer.readLine();
        outToServer.writeBytes(sentence + '\n');

        modifiedSentence = inFromServer.readLine();
        System.out.println("FROM SERVER: " + modifiedSentence);

        clientSocket.close();
    }
}
