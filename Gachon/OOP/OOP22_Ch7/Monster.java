package OOP22_Ch7;

public class Monster {
    private String name;
    private String type;
    private int energy;

    public Monster(String name, String type){
        this.name = name;
        this.type = type;
        energy = 100;
    }

    public String attackTo(Monster target){
        target.attackedBy(this);
        if(type.equals("Fire"))
            return attackFire();
        else if(type.equals("Water"))
            return attackWater();
        else if(type.equals("Stone"))
            return attackStone();
        return "";
    }
    
    public String attackFire(){
        return "Attack with Fire!!";
    }

    public String attackWater(){
        return "Attack with Water!!";
    }
    
    public String attackStone(){
        return "Attack with Stone!!";
    }

    public int attackedBy(Monster attacker){
        int damage = 0;
        if(type.equals("Fire"))
            if(attacker.getType().equals("Water"))
                damage = energy / 2;
            else if (attacker.getType().equals("Stone"))
                damage =(int)((float)energy / 1.5);
        else if(type.equals("Water")){

        }
        return damage;
    }

    public String getType(){
        return type;
    }
}
