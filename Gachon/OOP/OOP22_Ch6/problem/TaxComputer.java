package OOP22_Ch6.problem;

public class TaxComputer {
    /** the basic tax rate as a static double 
        variable that starts at 4 percent */
    private static double basicRate = 4.0;
    /** he luxury tax rate as a static double 
        variable that starts at 10 percent */
    private static double luxuryRate = 10.0;
    
    public static void changeBasicRateTo(double newRate){
        /** a static method that changes the basic tax rate. */
        basicRate = newRate;
    }
    
    public static void changeLuxuryRateTo(double newRate){
        /** a static method that changes the luxury tax rate. */
        luxuryRate = newRate;
    }
    
    public static double computeCostBasic(double price){
        /** a static method that returns the given price plus 
            the basic tax, rounded to the nearest penny. */
        double tax = price * basicRate / 100;
        price = price + tax;
        return roundToNearestPenny(price);
    }
    
    public static double computeCostLuxury(double price){
        /** a static method that returns the given price plus 
            the luxury tax, rounded to the nearest penny. */
        double tax = price * luxuryRate / 100;
        price = price + tax;
        return roundToNearestPenny(price);
    }
    
    private static double roundToNearestPenny(double price){
        /** a private static method that returns the given price 
            rounded to the nearest penny. For example, if 
            the price is 12.567, the method will return 12.57. */
        price = price * 100;
        price = java.lang.Math.round(price);
        return price/100;
    }
    
    public static void main(String[] args) {
        
        System.out.println("Testing the basic rate computation.");
        System.out.println("   Item price no tax: 10.00");
        System.out.println("    cost with 4% tax: "+ TaxComputer.computeCostBasic(10.00));
        
        System.out.println("Testing the basic rate computation.");
        TaxComputer.changeBasicRateTo(7.5);
        System.out.println("   Item price no tax: 10.00");
        System.out.println("    cost with 7.5% tax: "+ TaxComputer.computeCostBasic(10.00));
        
        
        System.out.println("Testing the luxury rate computation.");
        System.out.println("   Item price no tax: 2019.25");
        System.out.println("    cost with 10% tax: "+ TaxComputer.computeCostLuxury(2019.25));
        
        System.out.println("Testing the luxury rate computation.");
        TaxComputer.changeLuxuryRateTo(20.0);
        System.out.println("   Item price no tax: 2019.25");
        System.out.println("    cost with 20% tax: "+ TaxComputer.computeCostLuxury(2019.25));
        
        System.out.println("Testing the basic rate again, should still be 7.5%.");
        System.out.println("   Item price no tax: 210.99");
        System.out.println("    cost with 7.5% tax: "+ TaxComputer.computeCostBasic(210.99));
    }
}
