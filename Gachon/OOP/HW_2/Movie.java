package HW_2;
import java.util.Scanner;

public class Movie {
    private String name;
    private float num = 0;
    private String MPAA_Rating; // G, PG, PG-13, R
    private int rating;
    private int Terrible = 0; // 1
    private int Bad = 0; // 2
    private int Ok = 0; // 3
    private int Good = 0; // 4
    private int Great = 0; // 5

    void addRating(){
        Scanner keyboard = new Scanner(System.in);
        
        /** Input the movie name */
        System.out.print("Enter the Movie name: ");
        name = keyboard.nextLine();

        /** Input the movie's MPAA rating */
        System.out.print("Enter the Movie's MPAA rating: ");
        MPAA_Rating = keyboard.nextLine();

        /** Input the movie's Rating */
        while(true){
            System.out.print("Enter the Movie's rating(end = -1): ");
            rating = keyboard.nextInt();
            if(rating == -1) break;
            else if(rating >=1 && rating <= 5){
                num++;
                if (rating == 1) Terrible++;
                else if (rating == 2) Bad++;
                else if (rating == 3) Ok++;
                else if (rating == 4) Good++;
                else if (rating == 5) Great++;
            }
        }
    }

    void writeOutput(){
        System.out.println("The movie name is " + name);
        System.out.println("The MPAA rating is " + MPAA_Rating);
        System.out.println(String.format("The average rating is %.2f", getAverage()));
        System.out.println();

        /** clear the data */
        num = 0; 
        Terrible = 0;
        Bad = 0;
        Ok = 0;
        Good = 0;
        Great = 0;
    }

    float getAverage(){
        return (float)(Terrible*1 + Bad*2 + Ok*3 + Good*4 + Great*5) / num;
    }

    public static void main(String[] args){
        Movie movie = new Movie();
        /** first movie */
        movie.addRating();
        movie.writeOutput();

        /** second movie */
        movie.addRating();
        movie.writeOutput();
    }
}
