package MyFirstNetworkApp;

import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Server {
    public static String calc(String exp){
        /* 계산 함수 */
        String[] st = exp.split(" "); // st[0] = 수식, st[1] = 숫자들
        String[] op = st[1].split(","); // ","를 기준으로 숫자를 분류
        String res = "AritmeticException"; // 반환 디폴드값
        int op1 = Integer.parseInt(op[0]); // 첫번째 숫자
        int op2 = Integer.parseInt(op[1]); // 두번째 숫자
        if(op.length != 2){ // 숫자가 2개가 아닐때 오류 발생
            return "TokenCountError";
        }
        switch(st[0]){
            case "ADD": // 더하기
                res = Integer.toString(op1 + op2);
                break;
            case "DIV": // 나누기
                if(op2 == 0) {
                    // 0으로 나눌 경우 디폴트 오류 반환
                    break;
                }
                res = Integer.toString(op1 / op2);
                System.out.println(res);
                break;
            case "MINUS": // 빼기
                res = Integer.toString(op1 - op2);
                break;
            case "MUL": // 곱하기
                res = Integer.toString(op1 * op2);
                break;
        }
        return res; // 계산결과 string으로 반환
    }

    public static void main(String[] args) throws Exception{
        ServerSocket listener = new ServerSocket(7777);
        System.out.println("The Calculate server is running...");
        /* 쓰레드 20개 발생 */
        ExecutorService pool = Executors.newFixedThreadPool(20);
        while(true){
            Socket sock = listener.accept();
            pool.execute(new Calculate(sock));
        }
    }

    private static class Calculate implements Runnable{
        private Socket socket;

        Calculate(Socket socket){
            this.socket = socket;
        }

        @Override
        public void run(){
            System.out.println("Connected: " + socket);
            try{
                var in = new Scanner(socket.getInputStream());
                var out = new PrintWriter(socket.getOutputStream(), true);
                while(in.hasNextLine()){
                    String res = calc(in.nextLine());
                    try{
                        String answer = Integer.toBinaryString(Integer.parseInt(res));
                        out.println(answer);
                    }catch(Exception e1){
                        /* 에러 발생하면 어떤 에러인지 서버와 클라이언트에 전송 */
                        String answer = res;
                        System.out.println("Error:" + answer);
                        out.println(answer);
                    }
                }
            }catch (Exception e2){
                System.out.println("Error:" + socket);
            }finally {
                try{
                    socket.close();
                } catch (IOException e){}
                System.out.println("Closed: " + socket);
            } 
        }
    }
}
