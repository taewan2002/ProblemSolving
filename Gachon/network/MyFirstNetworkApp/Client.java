package MyFirstNetworkApp;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws Exception{
        String path = "server_info.dat";
        String host = "127.0.0.1"; // host 디폴트값
        int port = 1234; // port 디폴드값

		try { // server_info.dat 파일 읽기
            FileInputStream File = new FileInputStream(path);
            InputStreamReader inflie = new InputStreamReader(File);

            int c;
            String str = new String();
            while((c=inflie.read()) != -1){
                str = str + (char)c;
            }
            String[] result = str.split("\n");
            host = result[0];
            port = Integer.parseInt(result[1]);
		} catch (IOException e) {
            // 파일을 읽을 수 없다면 디폴드값으로 서버 연결
            System.out.println("Error: Can't open \"server_info.dat\"");
        }
        // var socket = new Socket(host, port); 에러 해결 못함
        var socket = new Socket("127.0.0.1", port);
        System.out.println("Enter lines of text then Ctrl+D or Ctrl+C to quit");
        System.out.print("계산식, ADD 24,42) >> "); //프롬프트
        var scanner = new Scanner(System.in);
        var in = new Scanner(socket.getInputStream());
        var out = new PrintWriter(socket.getOutputStream(), true);

        while (scanner.hasNextLine()){
            out.println(scanner.nextLine());
            String answer = in.nextLine();
            if(answer.compareTo("AritmeticException") == 0){
                // 0으로 나눴을 때의 오류
                System.out.println("Error: divided by zero");
            }
            else if(answer.compareTo("TokenCountError") == 0){
                // 입력 형식이 잘못됐을 때의 오류
                System.out.println("Error: too many arguments");
            }
            else{
                System.out.println(Integer.parseInt(answer, 2));
            }
            System.out.print("계산식, ADD 24,42) >> "); //프롬프트
        }
    }
}
