package HW_3;
import java.util.Scanner;

public class Characteristic{
    private String description;
    private int rating;

    public Characteristic(String desc) {
        /** sets the description of the characteristic to a given string and 
            sets the rating to zero to indicate that it has not yet been determined. */
        description = desc;
        rating = 0;
    }

    private boolean isValid(int aRating){
        /** Write a private method isValid(aRating) that returns true 
            if the given rating is valid, that is, is between 1 and 10. */
        return(aRating>=1 && aRating<=10);
    }

    public void setRating(int aRating){
        /** Write a method setRating(aRating) that sets the rating to aRating 
            if it is valid. */
        if(isValid(aRating))
            rating = aRating;
    }

    public void setRating(){
        /** Write a method setRating that reads a rating from the keyboard, 
            insisting that the rating supplied by the user be valid. */
        System.out.println("What is your rating for " + description + "?");
        System.out.println("Please enter an integer from 1 to 10");

        Scanner reader = new Scanner(System.in);
        int data = -1;
        boolean needTheRating = true;

        while(needTheRating){
            data = reader.nextInt();
            if(isValid(data)){
                needTheRating = false;
            } else {
                System.out.println("Sorry, that rating is out of range.");
                System.out.println("Please enter an integer from 1 to 10");
            }
        }
        setRating(data);
    }

    public String toString(){
        return description + " is rated as " + rating;
    }

    public String getDescription(){
        /** returns the description of this characteristic */
        return description;
    }

    public int getRating(){
        /** returns the rating of this characteristic */
        return rating;
    }

    public double getCompatibility(Characteristic otherRating){
        /** returns the compatibility measure of two matching characteristics, 
            or zero if the descriptions do not match */
        if(!isMatch(otherRating))
            return 0.0;
        else
            return getCompatibilityMeasure(otherRating);
    }

    private boolean isMatch(Characteristic otherRating){
        /** returns true if the descriptions match */
        return description.equals(otherRating.getDescription());
    }

    private double getCompatibilityMeasure(Characteristic otherRating){
        /** returns a compatibility measure as a double value using the formula */
        int r1 = rating;
        int r2 = otherRating.getRating();

        if(r1==0 || r2==0){
            return 0.0;
        } else {
            return (1.0 - (r1 - r2)*(r1 - r2)/81.0);
        }
    }

    public static void main(String[] args) { 
        Characteristic likesSports = new Characteristic("likes sports"); 
        Characteristic likesBeaches = new Characteristic("likes beaches"); 

        likesSports.setRating();
        System.out.println("Displaying the rating we got: " + likesSports.getRating()); 
        System.out.println(); 

        likesBeaches.setRating(); 
        System.out.println("Displaying the rating we got: " + likesBeaches.getRating()); 
        System.out.println(); 

        Characteristic sueLikesFishing = new Characteristic("likes fishing"); 
        sueLikesFishing.setRating(6); 
        Characteristic bobLikesFishing = new Characteristic("likes fishing"); 
        bobLikesFishing.setRating(6); 

        System.out.println("Compatibility measure should be 1"); 
        System.out.println("\t" + sueLikesFishing.getCompatibility(bobLikesFishing)); 

        System.out.println("Compatibility measure should be 0"); 
        System.out.println("\t" + sueLikesFishing.getCompatibility(likesSports)); 

        sueLikesFishing.setRating(1); 
        bobLikesFishing.setRating(9); 
        System.out.println("Compatibility measure should be 0.209"); 
        System.out.println("\t" + sueLikesFishing.getCompatibility(bobLikesFishing));

        sueLikesFishing.setRating(2); 
        bobLikesFishing.setRating(9); 
        System.out.println("Compatibility measure should be about 0.395"); 
        System.out.println("\t" + sueLikesFishing.getCompatibility(bobLikesFishing)); 
    }
}
