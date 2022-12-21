package OOP22_Ch13;

import java.awt.event.ActionEvent; 
import java.awt.event.ActionListener; 
import javax.swing.JButton;
import javax.swing.JFrame;

public class ButtonAction{
    public static void main(String[] args) {
        JFrame frame1 = new JFrame("JAVA");
        JButton button = new JButton("Press Me"); //Add action listener to button 
        button.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                //Execute when button is pressed
                System.out.println("You clicked the button"); 
            }
        });
        frame1.getContentPane().add(button); 
        frame1.pack(); 
        frame1.setVisible(true);
    }
}