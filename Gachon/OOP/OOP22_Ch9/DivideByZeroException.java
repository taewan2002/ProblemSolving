package OOP22_Ch9;

public class DivideByZeroException extends Exception{
    public DivideByZeroException(){
        super("Dividing by Zero!");
    }
    public DivideByZeroException(String message){
        super(message);
    }
}
