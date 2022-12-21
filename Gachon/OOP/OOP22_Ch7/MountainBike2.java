package OOP22_Ch7;

public class MountainBike2 {
    public int seatHeight;
    
    public Bicycle mb;

    public MountainBike2(int startHight, int startCadence, int startSpeed, int startGear){
        mb = new Bicycle(startCadence, startSpeed, startGear);
        seatHeight = startHight;
    }

    public void setGear(int newValue){
        mb.setGear(newValue);
    }

    public void applyBrake(int decrement){
        mb.speed = 0;
    }
}
