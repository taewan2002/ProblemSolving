package MyFirstNetworkApp;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.*;

public class qwer {

	public static void main(String[] args) {
		// OutputStream : 바이트 스트림의 최상위 부모 클래스
		// 파일로 저장하는 역할 (저장=쓰기=출력)
		
		InputStream is = System.in;
		OutputStream os = null;
		String path = "server_info.dat";
		byte buffer[] = new byte[1024];
       

		try {
			// System.out.println(">저장할 문자열 입력 ? ");
			// int n = is.read(buffer); //read로 키보드로 입력받아 buffer에 저장
			// os = new FileOutputStream(path); //현위치에 path명으로 파일 생성
			// os.write(buffer, 0, n); //파일에 buffer의 모든 내용 출력
            
            // // String 문자열을 FileOutputStream 바이트스트림을 사용해서 저장
            // //	String -> byte로 변환을 시켜야 os.write() 사용 가능
			
			
			// os.flush();
			// os.close();
            FileInputStream File = new FileInputStream(path);
            InputStreamReader in = new InputStreamReader(File);

            int c;
            String str = new String();
            while((c=in.read()) != -1){
                // System.out.print((char)c);
                str = str + (char)c;
            }
            System.out.println(str);
		} catch (IOException e) {
			e.printStackTrace();
		}
		

	}

}
