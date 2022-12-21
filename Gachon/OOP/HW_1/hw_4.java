package HW_1;
import java.util.Scanner;

public class hw_4 {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter the Date 1 or more(mm/dd/yyyy): ");
        
        // 입력받은 문자열을 "/"로 쪼개서 Day인덱스에 넣는다
        String[] Day = keyboard.next().split("/");

        // 입력받은 값을 각 변수에 정수형으로 변환하여 입력
        int m = Integer.parseInt(Day[0]);
        int d = Integer.parseInt(Day[1]);
        int y = Integer.parseInt(Day[2]);

        // 일, 월이 유효값인지 확인한다
        boolean mm = true;
        boolean dd = true;

        // 월이 유효하지 않으면 mm값을 false
        if (m > 12){
            mm = false;
        }

        // 일이 유효하지 않으면 dd값을 false
        if(m==1||m==3|m==5||m==8||m==10||m==12){
            if (d > 31){
                dd = false;
            }
        }
        else if(m==4||m==6|m==9||m==11){
            if (d > 30){
                dd = false;
            }
        }
        // 윤년을 판단한다
        else if(m==2){
            if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0){
                if (d > 29){
                    dd = false;
                }
            }
            else{
                if (d > 28){
                    dd = false;
                }
            }
        }

        // 판단한 결과에 따른 값을 출력한다.
        if(mm==true && dd==true){
            System.out.println("The date is validate!!");
        }
        else if(mm==true && dd==false){
            System.out.println("The day is not validate!!");
        }
        else if(mm==false && dd==true){
            System.out.println("The month is not validate!!");
        }
        else{
            System.out.println("The day and month is not validate!!");
        }
    }
}
