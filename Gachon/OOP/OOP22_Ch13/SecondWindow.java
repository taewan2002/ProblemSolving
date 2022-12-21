package OOP22_Ch13;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Color;
import java.awt.Container;

public class SecondWindow extends JFrame{
    public static final int WIDTH = 200; 
    public static final int HEIGHT = 200;
    public SecondWindow (Color customColor) {
        super ();
        setSize (WIDTH, HEIGHT);
        Container contentPane = getContentPane ();
        JLabel label = new JLabel ("Now available in color!"); 
        contentPane.add (label);
        setTitle ("Second Window");
        contentPane.setBackground (customColor); 
        addWindowListener(new WindowDestoryer());
    }
    public SecondWindow(){
        this(Color.BLUE); 
    }
}