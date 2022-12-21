package OOP22_Ch12;

public class LinkedList2Demo{
    public static void main(String[] args){
        LinkedList2<String> stringList = new LinkedList2<String>( ); 
        stringList.addANodeToStart("Hello"); 
        stringList.addANodeToStart("Good-bye"); 
        stringList.showList();
        LinkedList2<Integer> numberList = new LinkedList2<Integer>( ); 
        for (int i = 0; i < 5; i++)
            numberList.addANodeToStart(i);
        numberList.deleteHeadNode();
        numberList.showList( );
    }  
}