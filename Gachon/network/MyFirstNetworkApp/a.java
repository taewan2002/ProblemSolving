package MyFirstNetworkApp;
import java.io.*;

public class a
{
  public static void main(String [] args)
  {
    try{
      //String filename = args[0];
      //String filename = "c:/test.dat";
      String filename = "server_info.dat";
      // FileOutputStream out = new FileOutputStream(filename);
      FileInputStream File = new FileInputStream(filename);
      InputStreamReader in = new InputStreamReader(File);
     
    //   for(byte i = 1; i<=10; i++){
    //     out.write(i);
    //   }
      //1부터 10까지 byte 코드로 쓴다. 파일이 없는경우 자동 생성한다.
     
      int c;
      String str = new String();
      while((c=in.read()) != -1){
       System.out.println(c + " ");
       str = str + c;
      }
      //파일의 내용을 읽어서 화면에 출력한다.(바이트 스트림을 문자 스트림으로 변환한 값을 출력)
      System.out.println(str);
     
      in.close();
      //out.close();
     
    }catch(IOException ie){
      System.out.println("파일이 존재하지 않습니다.");
    }catch(Exception e){
      System.out.println(e);
    }
  }
}
