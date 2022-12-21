package OOP22_Ch13;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class LabelDemo extends JFrame implements ActionListener {
    
    public static final int WIDTH = 300; 
    public static final int HEIGHT = 200; 
    private JTextField name;
    public LabelDemo (){
        setTitle ("Name Tester");
        setSize (WIDTH, HEIGHT);
        //addWindowListener (new WindowDestroyer ());
        Container content = getContentPane (); content.setLayout (new GridLayout (2, 1));
        JPanel namePanel = new JPanel ();
        namePanel.setLayout (new BorderLayout ()); 
        namePanel.setBackground (Color.LIGHT_GRAY);
        name = new JTextField (20);
        namePanel.add (name, BorderLayout.SOUTH);
        JLabel nameLabel = new JLabel ("Enter your name here:"); 
        namePanel.add (nameLabel, BorderLayout.CENTER); 
        content.add (namePanel);
        JPanel buttonPanel = new JPanel (); 
        buttonPanel.setLayout (new FlowLayout ());
        JButton b = new JButton ("Test");
        b.addActionListener (this);
        buttonPanel.add (b);
        b = new JButton ("Clear");
        b.addActionListener (this);
        buttonPanel.add (b);
        content.add (buttonPanel);
    }
    public void actionPerformed (ActionEvent e) {
        if (e.getActionCommand ().equals ("Test")) 
            name.setText ("A very good name!");
        else if (e.getActionCommand ().equals ("Clear")) 
            name.setText ("");
        else
            name.setText ("Error in window interface.");
    }
    public static void main (String [] args) {
        LabelDemo w = new LabelDemo ();
        w.setVisible (true); 
    }
}