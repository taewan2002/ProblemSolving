import java.net.*;
import java.io.*;

public class UdpServer {
	public static void main(String args[]) {
		try {
			DatagramSocket ds = new DatagramSocket(9999);
			byte[] bf = new byte[300];
			DatagramPacket dp = new DatagramPacket(bf,  bf.length);
			
			while(true)	{
				System.out.println("Waiting for a packet reception..");				
				ds.receive(dp);
				
				System.out.println("A new message has been received:");
				String rs1 = new String(bf);
				String rs2 = rs1.trim();

				System.out.println("IP:" + dp.getAddress() + "  Port#:"+ dp.getPort());
				System.out.println("message: " + rs1);

			}
		} catch(IOException e) {}
	}
}


