package OOP22_Ch13;

import java.awt.Color;
public class SecondWindowDemo {
/**
Creates and displays two windows of the class SecondWindow. */
public static void main (String [] args){
    SecondWindow window1 = new SecondWindow (); 
    window1.setVisible (true);
    SecondWindow window2 = new SecondWindow (Color.PINK); 
    window2.setVisible (true);
    } 
}
