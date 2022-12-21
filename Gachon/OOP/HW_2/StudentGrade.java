package HW_2;
import java.util.Scanner;

public class StudentGrade {
    /** set variable */
    private float quiz1, quiz2, quiz3;
    private float midtermTest;
    private float finalTest;
    private float total_score_for_the_course;
    private String final_letter_grade;

    public void Input(){
        Scanner keyboard = new Scanner(System.in);
        
        /* Input quizzes score */
        System.out.println("Test score is 1 ~ 10");
        System.out.print("Enter the first quizz score: ");
        quiz1 = keyboard.nextFloat();
        System.out.print("Enter the second quizz score: ");
        quiz2 = keyboard.nextFloat();
        System.out.print("Enter the third quizz score: ");
        quiz3 = keyboard.nextFloat();

        /* Input midtermTest score */
        System.out.print("Enter the midterm test score: ");
        midtermTest = keyboard.nextFloat();

        /* Input finalTest score */
        System.out.print("Enter the final test score: ");
        finalTest = keyboard.nextFloat();
    }

    public void Output(){
        /* Calculate data */
        overall_numeric_score();
        final_letter_grade();

        /* Print Quiz Score */
        System.out.println("First quiz score is " + getQuiz1());
        System.out.println("Second quiz score is " + getQuiz2());
        System.out.println("Third quiz score is " + getQuiz3());

        /* Print Test Score */
        System.out.println("Midterm test score is " + getMidtermScore());
        System.out.println("Final test score is " + getFinalScore());

        /* Print total score */
        System.out.println("Total score is " + total_score_for_the_course);

        /* Print final_letter_grade */
        System.out.println("Final letter grade is " + final_letter_grade);
    }

    public void final_letter_grade(){
        /** Change to the letter grade */
        if (total_score_for_the_course>=90){
            final_letter_grade = "A";
        }
        else if (total_score_for_the_course>=80 && total_score_for_the_course<90){
            final_letter_grade = "B";
        }
        else if (total_score_for_the_course>=70 && total_score_for_the_course<80){
            final_letter_grade = "C";
        }
        else if (total_score_for_the_course>=60 && total_score_for_the_course<70){
            final_letter_grade = "D";
        }
        else{
            final_letter_grade = "F";
        }
    }

    public void overall_numeric_score(){
        /** total score */
        float quizzes = quiz1 + quiz2 + quiz3;
        total_score_for_the_course = (float)(quizzes + (midtermTest*0.3) + (finalTest*0.4));
    }

    /** get return data */
    public float getQuiz1(){
        return quiz1;
    }

    public float getQuiz2(){
        return quiz2;
    }

    public float getQuiz3(){
        return quiz3;
    }

    public float getMidtermScore(){
        return midtermTest;
    }

    public float getFinalScore(){
        return finalTest;
    }

    /** main code */
    public void Grade(){
        Input();
        Output();
    }

    public static void main(String[] args){
        StudentGrade myGrade = new StudentGrade();
        myGrade.Grade();
    }
}
