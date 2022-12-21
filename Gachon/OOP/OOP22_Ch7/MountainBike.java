package OOP22_Ch7;

public class MountainBike extends Bicycle {

    public int seatHeight;

    public MountainBike(int startHight, int startCadence, int startSpeed, int startGear){
        super(startCadence, startSpeed, startGear);
        seatHeight = startHight;
    }

    public void setHeight(int newValue){
        seatHeight = newValue;
    }
    
}
