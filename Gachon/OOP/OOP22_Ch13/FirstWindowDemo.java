package OOP22_Ch13;

/**
A simple demonstration of using a window class. To see
both windows, you will probably have to move the top window. */
public class FirstWindowDemo{
    public static void main (String [] args) {
        FirstWindow window1 = new FirstWindow (); 
        window1.setVisible (true);
        FirstWindow window2 = new FirstWindow (); 
        window2.setVisible (true);
    }
}