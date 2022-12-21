package HW_5;

import java.io.*;
import java.util.*;

public class abbreviation {
   public static void main(String[] args) {
      String text = "abbreviations.txt";
      /** How are u today? Iirc, this is your first free day. Hope you are having fun! :) , text file */
      String input = "input.txt";
      /** we will write text file  */
      String output = "output.txt";

      Scanner textfile = null;
      
      int index1=0;
      int index2=0;
      int check=0;
      int i=0,j=0;
      
      String ch[], word[];
      
      /** read the data, "abbreviations.txt" */
      try{
         textfile = new Scanner(new File(text));
         while(textfile.hasNext()){
            textfile.next();
            index1++;
         }
         textfile = new Scanner(new File(text));
      }
      catch(FileNotFoundException e){
         System.out.println("ERROR" + text);
         e.printStackTrace();
      }
      ch = new String[index1];
      
      while(textfile.hasNext()){
         ch[i] = new String();
         ch[i] = textfile.next();
         i++;
      }
      textfile.close();

      /** read the data, "input.txt" */
      try{
         textfile = new Scanner(new File(input));
         while(textfile.hasNext()){
            textfile.next();
            index2++;
         }
         textfile = new Scanner(new File(input));
      }
      catch(FileNotFoundException e){
         System.out.println("ERROR" + input);
         e.printStackTrace();
      }
      
      word = new String[index2];
      while(textfile.hasNext()){
         word[j] = new String();
         word[j] = textfile.next();
         j++;
      }
      textfile.close();
      
      PrintWriter writefile = null;

      /** read the data, "output.txt" */
      try{
         writefile = new PrintWriter(output);
      }
      catch(FileNotFoundException e){
         System.out.println("ERROR" + output);
         e.printStackTrace();
      }

      /** write the changed data and print the data */
      for(i=0;i<index2;i++){
         check=0;
         for(j=0;j<index1;j++){
            if(ch[j].equalsIgnoreCase(word[i])){
               writefile.print(" <"+ word[i] + ">");
               System.out.print(" <"+ word[i] + ">");
               check = 1;
               break;
            }
            else if (65 > (word[i].charAt(word[i].length()-1)) || (word[i].charAt(word[i].length()-1)) > 90){
               if(97 > (word[i].charAt(word[i].length()-1)) || (word[i].charAt(word[i].length()-1)) > 122){
                  if(ch[j].equalsIgnoreCase(word[i].substring(0, word[i].length()-1))){
                     writefile.print(" <"+ word[i].substring(0, word[i].length()-1) + ">" + word[i].substring(word[i].length()-1));
                     System.out.print(" <"+ word[i].substring(0, word[i].length()-1) + ">" + word[i].substring(word[i].length()-1));
                     check = 1;
                     break;
                  }
               }
            }
         }
         if(check==0){
            writefile.print(" " + word[i]);
            System.out.print(" " + word[i]);
         }
      }
      System.out.print("\n");
      writefile.close();
   }
}