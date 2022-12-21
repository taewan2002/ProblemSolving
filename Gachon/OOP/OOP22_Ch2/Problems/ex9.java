package OOP22_Ch2.Problems;

public class ex9 {
    public static void main(String[] args){
    }

    /*
    Many sports have constants embedded in their rules. For example, baseball has 9 innings, 3 outs per inning,
    3 strikes in an out, and 4 balls per walk, we might encode the constants for a program involving baseball as follows:
    - Basketball
    - American football
    - Soccer
    - Cricket
    - Bowling
    */

    // Basketball
    public static final int QUARTERS = 4;
    public static final int POINTS_PER_REGULAR_SHOT = 2;
    public static final int FOULS_PER_GAME = 5;
    
    // American football
    public static final int MINUTES_PER_QUARTER = 15;
    public static final int DOWNS = 4;
    public static final int YARDS_TO_FIRST_DOWN = 9;
    public static final int POINTS_FOR_TD = 6;
    public static final int POINTS_FOR_FIELDGOAL = 3;
    
    // Soccer
    public static final int PLAYERS_PER_SIDE = 11;
    public static final int MINUTES_PER_HALF = 45;
    public static final int BREAK_TIME = 15;
    
    // Cricket
    public static final int PLAYERS_PER_TEAM = 11;
    public static final int PITCH_LENGTH = 66;
    public static final int PITCH_WIDTH = 10;
    
    // Bowling
    public static final int NUMBER_OF_PINS = 10;
    public static final int FRAMES = 10;
    public static final int PERFECT_GAME = 300;
}
