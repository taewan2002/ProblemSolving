package OOP22_Ch12;

import java.util.HashSet;
public class HashSetDemo{
    public static void main(String[] args){
        HashSet<Integer> intSet = new HashSet<Integer>();
        intSet.add(2);
        intSet.add(7);
        intSet.add(7);
        intSet.add(3);
        printSet(intSet);

        intSet.remove(3);
        printSet(intSet);

        System.out.println("Set contains 2: " + intSet.contains(2));
        System.out.println("Set contains 3: " + intSet.contains(3));
    }

    public static void printSet(HashSet<Integer> intSet){
        System.out.println("The set contains:");
        for (Object obj : intSet.toArray()){ // intSet의 요소를 하나씩 obj에 넣음
            Integer num = (Integer)obj;
            System.out.println(num.intValue());
        }
    } 
}