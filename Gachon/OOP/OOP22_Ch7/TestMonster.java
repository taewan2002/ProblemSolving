package OOP22_Ch7;

public class TestMonster {
    public static void main(String[] args){

        Monster m1 = new Monster("r2u2", "Frie");
        Monster m2 = new Monster("u2r2", "Water");
        Monster m3 = new Monster("r2r2", "Stone");

        System.out.println(m1.attackTo(m2));
        System.out.println(m2.attackTo(m3));
        System.out.println(m3.attackTo(m1));
    }
}
