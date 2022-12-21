package OOP22_Ch12;

import java.util.HashMap;
public class HashMapDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> mountains = new HashMap<String, Integer>();

        mountains.put("Everest",29029); 
        mountains.put("K2",28251); 
        mountains.put("Kangchenjunga",28169); 
        mountains.put("Denali",20335); 
        printMap(mountains);

        System.out.println("Denali in the map: " + mountains.containsKey("Denali")); 
        System.out.println();
        System.out.println("Changing height of Denali."); 
        mountains.put("Denali", 20320); // Overwrites old value for Denali printMap(mountains);

        System.out.println("Removing Kangchenjunga."); 
        mountains.remove("Kangchenjunga"); 
        printMap(mountains);
    }

    public static void printMap(HashMap<String, Integer> map){
        System.out.println("Map contains:");
        for (String keyMountainName : map.keySet()){
            Integer height = map.get(keyMountainName);
            System.out.println(keyMountainName + " --> " + height.intValue() + " feet.");
        }
        System.out.println(); 
    }
}

