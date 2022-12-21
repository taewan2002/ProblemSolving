package MyFirstNetworkApp;
import java.net.*;
import java.io.*;
import java.lang.invoke.TypeDescriptor;

public class UdpClient {
    public static void main(String[] args){
        try{
            DatagramSocket ds = new DatagramSocket();
            InetAddress ia = InetAddress.getByName("localhost");
            String msg = "Hello World";
            byte[] bf = msg.getBytes();
            DatagramPacket dp = new DatagramPacket(bf, bf.length, ia, 9999);
            ds.send(dp);
        } catch(IOException e) {}
    }
}
