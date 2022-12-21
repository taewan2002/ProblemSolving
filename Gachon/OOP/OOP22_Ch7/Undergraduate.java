package OOP22_Ch7;

public class Undergraduate extends Student{
    private int level;
    /** 1. freshman, 2. sophomore,
        3. junior, 4. senior */
    
    public Undergraduate(){
        super();
        level = 1;
    }

    public Undergraduate(String initialName, int initialStudentNumber, int initialLevel){
        super(initialName, initialStudentNumber);
        setLevel(initialLevel);
    }

    public int getLevel(){
        return level;
    }

    public void setLevel(int newLevel){
        if((1<= newLevel) && (newLevel <= 4))
            level = newLevel;
        else{
            System.out.println("Illegal level!");
            System.exit(0);
        }
    }

    public void reset(String newName, int newStudentNumber, int newLevel){
        reset(newName, newStudentNumber); // overload
        setLevel(newLevel);
    }

    public void writeOutput(){
        super.writeOutput(); // override
        System.out.println("Student Level: " + level);
    }

    public boolean equals(Undergraduate otherUndergraduate){
        return equals((Student)otherUndergraduate) && (this.level == otherUndergraduate.level);
    }

}
