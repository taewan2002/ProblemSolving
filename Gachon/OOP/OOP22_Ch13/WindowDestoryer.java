package OOP22_Ch13;

import java.awt.event.*; 
import javax.swing.*;
/**
If you register an object of this class as a listener to any object of the class JFrame, the object will end the program and close the JFrame if the user clicks the JFrame's close-window button.
*/
public class WindowDestoryer extends WindowAdapter { 
    @Override
    public void windowClosing(WindowEvent e) { 
    JOptionPane.showMessageDialog(null, "Window is closing", "Message", JOptionPane.INFORMATION_MESSAGE); 
    super.windowClosing(e);
    } 
}