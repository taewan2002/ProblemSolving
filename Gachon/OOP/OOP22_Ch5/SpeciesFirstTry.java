package OOP22_Ch5;

import java.util.Scanner;

public class SpeciesFirstTry {
    public String name;
    public int population;
    public double growthRate;

    public void readInput(){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("What is the species' name?");
        name = keyboard.nextLine();
        System.out.println("What is the population of the " + 
                            "species?");
        population = keyboard.nextInt();
        System.out.println("Enter growth rate " + 
                            "(% increase per year):");
        growthRate = keyboard.nextDouble();
    }
    public void writeOutput(){
        System.out.println("Name = " + name);
        System.out.println("Population = " + population);
        System.out.println("Growth rate = " + growthRate + "%");
    }
    public int getPopulationIn10(){
        int result = 0;
        double populationAmount = population;
        int count = 10;
        while ((count > 0) && (populationAmount > 0)){
            populationAmount = populationAmount +
                                (growthRate / 100) *
                                populationAmount;
            count--;
        }
        if (populationAmount > 0)
            result = (int)populationAmount;
        return result;
    }
}
