package OOP22_Ch8;

public class TreeDemo{
    public static final int INDENT = 5;
    public static final int TREE_TOP_WIDTH = 21;// must be odd
    public static final int TREE_BOTTOM_WIDTH = 4;
    public static final int TREE_BOTTOM_HEIGHT = 4;
    public static void main(String[] args){
        drawTree(TREE_TOP_WIDTH, TREE_BOTTOM_WIDTH, TREE_BOTTOM_HEIGHT);
    }
    public static void drawTree(int topWidth, int bottomWidth, int bottomHeight){
        System.out.println(" Save the Redwoods!"); 
        TriangleInterface treeTop = new Triangle(INDENT, topWidth); 
        drawTop(treeTop);
        RectangleInterface treeTrunk = new Rectangle(INDENT + (topWidth / 2) - (bottomWidth / 2), bottomHeight, bottomWidth);
        drawTrunk(treeTrunk);
    }
    private static void drawTop(TriangleInterface treeTop){
        treeTop.drawAt(1);
    }
    private static void drawTrunk(RectangleInterface treeTrunk){
        treeTrunk.drawHere(); // or treeTrunk.drawAt(0);
    }
}