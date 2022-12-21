package OOP22_Ch6.problem;

public class RoomOccupancy {
    
    /** the total number of people in 
        all rooms as a static variable */
    private static int totalNumber = 0;
    /** the number of people in a room */
    private int numberInRoom;
    
    public RoomOccupancy() {
        numberInRoom = 0;
    }
    
    public void addOneToRoom(){
        /** adds a person to the room and 
            increases the value of totalNumber */
        numberInRoom++;
        totalNumber++;
    }
    
    public void removeOneFromRoom(){
        /** removes a person from the room, 
            ensuring that numberInRoom does not 
            go below zero, and decreases the value 
            of totalNumber as needed */
        if(numberInRoom>0){
            numberInRoom--;
            totalNumber--;
        }
    }
    
    public int getNumber(){
        /** returns the number of people in the room */
        return numberInRoom;
    }

    public static int getTotal(){
        /** a static method that returns the total number of people */
        return totalNumber;
    }
    
    public static void main(String[] args) {
        RoomOccupancy roomA = new RoomOccupancy();
        RoomOccupancy roomB = new RoomOccupancy();
        
        System.out.println("Add one to room a and three to room b.");
        roomB.addOneToRoom();
        roomA.addOneToRoom();
        roomB.addOneToRoom();
        roomB.addOneToRoom();
        
        System.out.println("Room a holds " + roomA.getNumber());
        System.out.println("Room b holds " + roomB.getNumber());
        System.out.println("Total in all rooms is " + RoomOccupancy.getTotal());
        
        System.out.println("Remove one from both rooms.");
        roomA.removeOneFromRoom();
        roomB.removeOneFromRoom();
        
        System.out.println("Room a holds " + roomA.getNumber());
        System.out.println("Room b holds " + roomB.getNumber());
        System.out.println("Total in all rooms is " + RoomOccupancy.getTotal());
        
        System.out.println("Remove two from room a (should not change the values)");
        roomA.removeOneFromRoom();
        roomA.removeOneFromRoom();
        System.out.println("Room a holds " + roomA.getNumber());
        System.out.println("Room b holds " + roomB.getNumber());
        System.out.println("Total in all rooms is " + RoomOccupancy.getTotal());
        
        System.out.println("Create room c and add three to it.");
        
        RoomOccupancy roomC = new RoomOccupancy();
        roomC.addOneToRoom();
        roomC.addOneToRoom();
        roomC.addOneToRoom();
        System.out.println("Room a holds " + roomA.getNumber());
        System.out.println("Room b holds " + roomB.getNumber());
        System.out.println("Room c holds " + roomC.getNumber());
        System.out.println("Total in all rooms is " + RoomOccupancy.getTotal());  
    }  
}
