package OOP22_Ch13;
import javax.swing.*;

public class HelloSwing {
    public static void main(String[] args){
        JFrame f = new JFrame("Hello");
        JPanel p = new JPanel();
        JButton b = new JButton("Fuck Me");

        f.setSize(400, 400);
        f.setContentPane(p); // add panel to frame
        p.add(b);            // add button to panel
        f.setVisible(true);
    }
    
}
