package HW_5;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

public class PetSort extends PetRecord{
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        String name;
        int age;
        double weight;

        /** temp data */
        String tname;
        int tage;
        double tweight;
        

        /** make ArrayList */
        ArrayList<PetRecord> PetList = new ArrayList<PetRecord>();

        /** Input data */
        String type;
        do{
            System.out.print("Enter pet name : ");
            name = keyboard.next();
            System.out.print("Enter pet age : ");
            age = keyboard.nextInt();
            System.out.print("Enter pet weight : ");
            weight = keyboard.nextDouble();

            if(age<=0 || weight <= 0){
                System.out.println("ERROR");
                System.exit(0);
            }

            PetRecord PetRecord = new PetRecord(name, age, weight);

            PetList.add(PetRecord);
            System.out.print("Enter the more data? (Y/N): ");
            type = keyboard.next();
        }while(type.equalsIgnoreCase("y"));

        /** Bubble Sort */
        for (int index = 0; index < PetList.size(); index++){
            for (int i=PetList.size()-1; i>index; i--){
                if(PetList.get(i-1).getName().compareTo(PetList.get(i).getName())>0){
                    tname = PetList.get(i-1).getName();
                    tage = PetList.get(i-1).getAge();
                    tweight = PetList.get(i-1).getAge();

                    PetList.get(i-1).set(PetList.get(i).getName());
                    PetList.get(i-1).set(PetList.get(i).getAge());
                    PetList.get(i-1).set(PetList.get(i).getWeight());

                    PetList.get(i).set(tname);
                    PetList.get(i).set(tage);
                    PetList.get(i).set(tweight);
                }
            }   
        }
        /** print data */
        System.out.print("\nPrint PetList: \n\n");
        for(int i=0; i<PetList.size(); i++){
            System.out.println(PetList.get(i));
        }
    }
}
