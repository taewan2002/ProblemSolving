package OOP22_Ch7;

public class Bicycle {
    public int cadence, gear, speed;

    public Bicycle(int startCadence, int startSpeed, int startGear){
        gear = startGear;
        cadence = startCadence;
        speed = startSpeed;
    }

    public void setCadence(int newValue){
        cadence = newValue;
    }

    public void setGear(int newValue){
        gear = newValue;
    }

    public void applyBrake(int decrement){
        speed -= decrement;
    }

    public void speedUp(int increment){
        speed += increment;
    }
}
