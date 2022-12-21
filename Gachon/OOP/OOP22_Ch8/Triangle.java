package OOP22_Ch8;

public class Triangle extends ShapeBasics implements TriangleInterface{
    private int base;
    public Triangle(){
        super();
        base = 0; 
    }
    public Triangle(int theOffset, int theBase){
        super(theOffset);
        base = theBase;
    }
    /** Precondition: newBase is odd. */
    public void set(int newBase){
        base = newBase;
    }
    public void drawHere(){
        drawTop();
        drawBase();
    }
    private void drawBase(){
        skipSpaces(getOffset());
        for (int count = 0; count < base; count++)
            System.out.print('*');
        System.out.println();
    }
    private void drawTop(){
        int startOfLine = getOffset() + base / 2; 
        skipSpaces(startOfLine); 
        System.out.println('*');
        int lineCount = base / 2 - 1;
        int insideWidth = 1;
        for (int count = 0; count < lineCount; count++){
            startOfLine --;
            skipSpaces(startOfLine); 
            System.out.print('*'); 
            skipSpaces(insideWidth); 
            System.out.println('*');
            insideWidth = insideWidth + 2;
        }
    }
    private static void skipSpaces(int number){
        for (int count = 0; count < number; count++)
            System.out.print(' ');
    }
}