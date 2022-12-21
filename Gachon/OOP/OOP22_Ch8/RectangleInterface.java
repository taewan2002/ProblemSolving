package OOP22_Ch8;

// ShapeInterface를 상속해서 만든 RectangleInterface

public interface RectangleInterface extends ShapeInterface {
    public void set(int newHeight, int newWidth);
}