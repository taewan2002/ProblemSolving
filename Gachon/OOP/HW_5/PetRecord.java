package HW_5;

import java.io.*;
import java.util.*;

/**
 Class for basic pet records: name, age, and weight.

 Same as PetRecord, Listing 6.1 except:
 1. It implements Serializable.
 2. It has a readInput() method, similar to Species, Listing 5.19
 3. It has a toString() method similar to Species, Listing 10.9
*/

public class PetRecord implements Serializable
{
    private String name;
    private int age;       // in years
    private double weight; //in pounds

    public void readInput()
    {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter pet's name:");
        name = keyboard.nextLine();
        System.out.println("Enter pet's age:");
        age = keyboard.nextInt();
        if(age < 0)
        {
            System.out.println("Error: Age cannot be negative.");
            System.exit(0);
        }
        System.out.println("Enter pet's weight:");
        weight = keyboard.nextDouble();
        if(weight < 0)
        {
            System.out.println("Error: Weight cannot be negative.");
            System.exit(0);
        }
    }

    public String toString()
    {
        return ("Name = " + name + "\n" + "Age = " + age + "\n"
                    + "Weight = " + weight + "\n");
    }

    public void writeOutput()
    {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age + " years");
        System.out.println("Weight: " + weight + " pounds");
    }

    public PetRecord(
                String initialName, int initialAge, double initialWeight)
    {
        name = initialName;
        if ((initialAge < 0) || (initialWeight < 0))
        {
            System.out.println("Error: Negative age or weight.");
            System.exit(0);
        }
        else
        {
            age = initialAge;
            weight = initialWeight;
        }
    }

    public void set(String newName, int newAge, double newWeight)
    {
        name = newName;
        if ((newAge < 0) || (newWeight < 0))
        {
            System.out.println("Error: Negative age or weight.");
            System.exit(0);
        }
        else
        {
            age = newAge;
            weight = newWeight;
        }
    }

    public PetRecord(String initialName)
    {
        name = initialName;
        age = 0;
        weight = 0;
    }

    public void set(String newName)
    {
        name = newName; // age and weight are unchanged.
    }

    public PetRecord(int initialAge)
    {
        name = "No name yet.";
        weight = 0;
        if (initialAge < 0)
        {
            System.out.println("Error: Negative age.");
            System.exit(0);
        }
        else
            age = initialAge;
    }

    public void set(int newAge)
    {
        if (newAge < 0)
        {
            System.out.println("Error: Negative age.");
            System.exit(0);
        }
        else
            age = newAge; // name and weight are unchanged.
    }

    public PetRecord(double initialWeight)
    {
        name = "No name yet";
        age = 0;
        if (initialWeight < 0)
        {
            System.out.println("Error: Negative weight.");
            System.exit(0);
        }
        else
            weight = initialWeight;
    }

    public void set(double newWeight)
    {
        if (newWeight < 0)
        {
            System.out.println("Error: Negative weight.");
            System.exit(0);
        }
        else
            weight = newWeight; // name and age are unchanged.
    }

    public PetRecord()
    {
        name = "No name yet.";
        age = 0;
        weight = 0;
    }

    public String getName()
    {
        return name;
    }

    public int getAge()
    {
        return age;
    }

    public double getWeight()
    {
        return weight;
    }
}
