package OOP22_Ch6.problem;
import java.util.Scanner;

public class Time {
    private int theHour;
    private int theMinute;

    public Time() {
        /** a. Write a default constructor that 
        initializes the time to 0 hours, 0 minutes. */
        theHour = 0;
        theMinute = 0;
    }

    public Time(int hour, int minute){
        setTime(hour, minute);
    }

    public Time(int hour, int minute, boolean isAM){
        setTime(hour, minute, isAM);
    }

    private boolean isValid(int hour, int minute){
        /** b. Write a private method isVlid(hour, minute) that returns true 
            if the given hour and minute values are in the appropriate range.*/
        return (hour>=0 && hour<=23) && (minute>=0 && minute<=59);
    }

    public void setTime(int hour, int minute){
        /** c. Write a method setTime(hour, minute) that sets 
            the time if the given values are valid */
        if(isValid(hour, minute)) {
            theHour = hour;
            theMinute = minute;
        }
    }

    public void setTime(int hour, int minute, boolean isAM){
        /** d. Write another method setTime(hour, minutem isAM) that sets
            the time if the given values are valid. The given hour should 
            be in the range 1 to 12. The parameter isAm is true if the time 
            is an a.m. time and false otherwise. */
        if(hour>=1 && hour<=12){
            if(isAM && hour == 12) // 12AM is 0 hours.
                hour = 0;
            else if (!isAM && hour < 12) // 8PM is 20 hours
                hour = hour + 12;
            // The remaining hours are unchanged
            // 11AM is 11 hours, 12PM is 12 hours
            if(isValid(hour, minute)) {
                theHour = hour;
                theMinute = minute;
            }
        }
    }

    public String getTime12(){
        String response = "";

        if(theHour == 0)
            response = "12";
        else if(theHour > 12)
            response = response + (theHour-12);
        else
            response = response + theHour;

        response = response + ":";

        if(theMinute < 10)
            response = response + "0" + theMinute;
        else
            response = response + theMinute;

        if(theHour>=0 && theHour<11)
            response = response + "AM";
        else
            response = response + "PM";

        return response;
    }

    public String getTime24(){
        String response = "";
        if(theHour < 10)
            response = "0" + theHour;
        else
            response = "" + theHour;

        if(theMinute < 10)
            response = response + "0" + theMinute;
        else
            response = response + theMinute;

        return response;
    }

    public String toString(){
        return "hour: " + theHour + " minute: " + theMinute;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        Time time1 = new Time();
        System.out.println("Create a default time");
        System.out.println("\t should be 0, 0:  " + time1);

        System.out.println("Set the time to 12, 12");
        time1.setTime(12, 12);
        System.out.println("\t should be 12, 12:  " + time1);

        System.out.println("Trying to set time to -1, 12");
        time1.setTime(-1, 12);
        System.out.println("\t should be 12, 12:  " + time1);

        System.out.println("Trying to set time to 12, -1");
        time1.setTime(12, -1);
        System.out.println("\t should be 12, 12:  " + time1);

        System.out.println("Trying to set time to 24, 12");
        time1.setTime(24, 12);
        System.out.println("\t should be 12, 12:  " + time1);

        System.out.println("Trying to set time to 12, 60");
        time1.setTime(12, 60);
        System.out.println("\t should be 12, 12:  " + time1);


        System.out.println("Set the time to 8, 16 am");
        time1.setTime(8, 16, true);
        System.out.println("\t should be 8, 16:  " + time1);

        System.out.println("Set the time to 8, 16 pm");
        time1.setTime(8, 16, false);
        System.out.println("\t should be 20, 16:  " + time1);

        System.out.println("Trying to set time to 0, 17 am");
        time1.setTime(0, 17, true);
        System.out.println("\t should be 20, 16:  " + time1);

        System.out.println("Trying to set time to 12, 17 am");
        time1.setTime(13, 17, true);
        System.out.println("\t should be 20, 16:  " + time1);

        System.out.println("Trying to set time to 0, 17 pm");
        time1.setTime(0, 17, false);
        System.out.println("\t should be 20, 16:  " + time1);

        System.out.println("Trying to set time to 12, 17 pm");
        time1.setTime(13, 17, false);
        System.out.println("\t should be 20, 16:  " + time1);

        System.out.println("Set the time to 12, 19 am");
        time1.setTime(12, 19, true);
        System.out.println("\t should be 0, 19:  " + time1);

        System.out.println("Set the time to 12, 19 pm");
        time1.setTime(12, 19, false);
        System.out.println("\t should be 12, 19:  " + time1);

        System.out.println("\nTesting the constructors");
        System.out.println("Create the time  12, 19");
        Time time2 = new Time(12, 19);
        System.out.println("\t should be 12:19pm:  " + time2.getTime24() + " and " + time2.getTime12());
        System.out.println("Create the time  12, 19 with the other constructor");
        time2 = new Time(12, 19, false);
        System.out.println("\t should be 12:19pm:  " + time2.getTime24() + " and " + time2.getTime12());

        System.out.println("Create the time  0, 19");
        time2 = new Time(0, 19);
        System.out.println("\t should be 12:19am:  " + time2.getTime24() + " and " + time2.getTime12());
        System.out.println("Create the time  12, 19 with the other constructor");
        time2 = new Time(12, 19, true);
        System.out.println("\t should be 12:19pm:  " + time2.getTime24() + " and " + time2.getTime12());

        System.out.println("Create the time  3, 19");
        time2 = new Time(3, 19);
        System.out.println("\t should be 3:19am:  " + time2.getTime24() + " and " + time2.getTime12());
        System.out.println("Create the time  3, 19 with the other constructor");
        time2 = new Time(3, 19, true);
        System.out.println("\t should be 3:19am:  " + time2.getTime24() + " and " + time2.getTime12());

        System.out.println("Create the time  15, 19");
        time2 = new Time(15, 19);
        System.out.println("\t should be 3:19pm:  " + time2.getTime24() + " and " + time2.getTime12());
        System.out.println("Create the time  3, 19 with the other constructor");
        time2 = new Time(3, 19, false);
        System.out.println("\t should be 3:19pm:  " + time2.getTime24() + " and " + time2.getTime12());
    }

}
