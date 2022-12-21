package OOP22_Ch5;

public class SpeciesFirstTryDemo {
    public static void main(String[] args){
        SpeciesFirstTry speciesOfTheMonth = new SpeciesFirstTry();
        System.out.println("Enter data on the Species of " + "the Month");
        speciesOfTheMonth.readInput();
        speciesOfTheMonth.writeOutput();

        int futurePopulation = speciesOfTheMonth.getPopulationIn10();
        System.out.println("In ten years the population will be " + futurePopulation);
        // Chage the species th show how to change
        // the values of instance variable
        speciesOfTheMonth.name = "Klingon ox";
        speciesOfTheMonth.population = 10;
        speciesOfTheMonth.growthRate = 15;
        System.out.println("The new Species of the Month:");
        speciesOfTheMonth.writeOutput();
        System.out.println("In the years the population will be " + speciesOfTheMonth.getPopulationIn10());
    }
}
