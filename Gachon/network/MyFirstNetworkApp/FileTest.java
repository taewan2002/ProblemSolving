package MyFirstNetworkApp;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileOutputStream;
import java.io.*;

public class FileTest {
    public static void main(String[] args) throws IOException {
        // String path = FileTest.class.getResource("").getPath(); // 현재 클래스의 절대 경로를 가져온다.
        // System.out.println(path); //--> 절대 경로가 출력됨
        // File fileInSamePackage = new File(path + "serverinfo.txt"); // path 폴더 내의 test.txt 를 가리킨다.
        
        byte[] b = new byte[1024];
        FileInputStream input = new FileInputStream("/Users/taewan/Library/Application%20Support/Code/User/workspaceStorage/9bc76eb59ffb8f73d871d65eb262face/redhat.java/jdt_ws/2%ed%95%99%eb%85%84_5528179d/bin/MyFirstNetworkApp/serverinfo.txt");
        input.read(b);
        System.out.println(new String(b));  // byte 배열을 문자열로 변경하여 출력
        input.close();
    }
}
