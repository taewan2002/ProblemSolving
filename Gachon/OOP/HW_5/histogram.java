package HW_5;

import java.util.HashMap;
import java.util.Scanner;

public class histogram {
   public static void main(String[] args) {
      Scanner keyboard = new Scanner(System.in);
      HashMap<Integer,Integer> list = new HashMap<Integer,Integer>();
      int num;

      System.out.println("Enter numbers(end = -1): ");
      while(true){
         num = keyboard.nextInt();
         int check = search(num,list);
         if(num<0) // input -1 
            break;
         list.put(num,check);
      }
      for(Integer number : list.keySet()){
         Integer count = list.get(number);
         /** print the histogram */
         System.out.println("The number " + number + " occurs " + count + " times");
      }   
   }
   public static int search(Integer num, HashMap<Integer,Integer> histogram){
      /** search the data count  */
      int flag=1;
      for(Integer a : histogram.keySet()){
         Integer cnt = histogram.get(a);
         flag = cnt;
         if(num == a)
            return cnt + 1;
         else
            flag = 1;
      }
      return flag;
   }
}