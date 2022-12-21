package OOP22_Ch8;

// 추상 메서드를 implements 해서 @Override로 구체화 시킴
public class ShapeBasics implements ShapeInterface{
    private int offset;
    
    public ShapeBasics(){
        offset = 0;
    }
    public ShapeBasics(int theOffset){
        offset = theOffset;
    }
    
    @Override
    public void setOffset(int newOffset){
        offset = newOffset;
    }
    @Override
    public int getOffset(){
        return offset;
    }
    @Override
    public void drawAt(int lineNumber){
        for (int count = 0; count < lineNumber; count++)
            System.out.println();
        drawHere();
    }
    @Override
    public void drawHere(){
        for (int count = 0; count < offset; count++)
            System.out.print(' ');
        System.out.println('*');
    }
}
