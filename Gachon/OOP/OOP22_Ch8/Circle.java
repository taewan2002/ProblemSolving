package OOP22_Ch8;

public class Circle implements Measurable {
    private double myRadius;

    public Circle(double radius){
        myRadius = radius; 
    }

    public double getPerimeter(){
        return 2 * Math.PI * myRadius; 
    }

    public double getCircumference(){
        return getPerimeter(); 
    }   

    public double getArea(){
        return Math.PI * myRadius * myRadius; 
    }
}