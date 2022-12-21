package OOP22_Ch13;

import javax.swing.JFrame; 
import javax.swing.JLabel; /**
A simple window class.
*/
public class FirstWindow extends JFrame {
    public static final int WIDTH = 300; 
    public static final int HEIGHT = 200; 
    public FirstWindow(){
        super();
        setSize (WIDTH, HEIGHT);
        JLabel myLabel = new JLabel ("Please dont click that button!"); 
        getContentPane().add(myLabel);
        WindowDestoryer listener = new WindowDestoryer (); 
        addWindowListener (listener);
    }
}
