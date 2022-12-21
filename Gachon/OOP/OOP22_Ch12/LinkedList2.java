package OOP22_Ch12;

import java.util.ArrayList;
public class LinkedList2<E>{
    private ListNode head;
    public LinkedList2(){
        head = null;
    }
    public void showList(){
        ListNode position = head;
        while (position != null){
            System.out.println(position.getData());
            position = position.getLink();
        }
    }
    public int length(){
        int count = 0;
        ListNode position = head;
        while (position != null){
            count++;
            position = position.getLink( );
        }
        return count;
    }
    public void addANodeToStart(E addData){
        head = new ListNode(addData, head);
    }
    public void deleteHeadNode(){
        if (head != null){
            head = head.getLink();
        }
        else{
            System.out.println("Deleting from an empty list.");
            System.exit(0);
        } 
    }
    public boolean onList(E target){
        return find(target) != null;
    }
    private ListNode find(E target){
        boolean found = false;
        ListNode position = head;
        while (position != null){
            E dataAtPosition = position.getData();
            if (dataAtPosition.equals(target))
                found = true;
            else
                position = position.getLink();
        }
        return position;
    }
    private ArrayList<E> toArrayList(){
        ArrayList<E> list = new ArrayList<E>(length());
        ListNode position = head;
        while (position != null){
            list.add(position.data);
            position = position.link;
        }
        return list;
    }
    private class ListNode{
        private E data;
        private ListNode link;
        public ListNode(){
            link = null;
            data = null; 
        }
        public ListNode(E newData, ListNode linkValue){
            data = newData;
            link = linkValue;
        }
        public E getData(){
            return data;
        }
        public ListNode getLink(){
            return link;
        }
    } 
}