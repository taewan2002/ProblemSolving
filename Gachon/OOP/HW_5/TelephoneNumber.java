package HW_5;

/*
 * TelephoneNumber.java
 * for HW5-2
 */

import java.io.*;
import java.util.*;

public class TelephoneNumber {
    private boolean hasAreaCode;
    private int areaCode; // 010
    private int exchangeCode; // 4630
    private int number; // 6320
    
    /**
     * Creates a new instance of TelephoneNumber
     */
    public TelephoneNumber(String input)
    throws InvalidTelephoneFormatException {
        StringTokenizer scanner = new StringTokenizer(input, "-"); // 010-4630-6320-

        // split it up on hyphens, hyphen is not part of the token
        if((scanner.countTokens() != 2) && (scanner.countTokens() != 3))
            throw new InvalidTelephoneFormatException("Did not find required hyphens.");

        if(scanner.countTokens() == 3){
            String areaString = scanner.nextToken().trim();

            if(areaString.length() != 3)
                throw new InvalidTelephoneFormatException("Area code is not 3 digits");
            try {
                areaCode = Integer.parseInt(areaString);
            } 
            catch (NumberFormatException ex){
                throw new InvalidTelephoneFormatException("Area code was not an integer.");
            }
            hasAreaCode = true;
        } else
            hasAreaCode = false;
        
        String exchangeString = scanner.nextToken().trim();
            if(exchangeString.length() != 3)
                throw new InvalidTelephoneFormatException("Exchange code is not 3 digits");
            try {
                exchangeCode = Integer.parseInt(exchangeString);
            } 
            catch (NumberFormatException ex){
                throw new InvalidTelephoneFormatException("Exchange code was not an integer.");
            }

            String numberString = scanner.nextToken().trim();
            if(numberString.length() != 4)
                throw new InvalidTelephoneFormatException("Number is not 4 digits");
            try {
                number = Integer.parseInt(numberString);
            } 
            catch (NumberFormatException ex){
                throw new InvalidTelephoneFormatException("Number was not an integer.");
            }

        
    }
    
    public String toString(){
        
        String areaString = Integer.toString(areaCode);
        while(areaString.length() < 3)
            areaString = "0" + areaString;
        
        String exchangeString = Integer.toString(exchangeCode);
        while(exchangeString.length() < 3)
            exchangeString = "0" + exchangeString;

        String  numberString = Integer.toString(number);
        while(numberString.length() < 4)
            numberString = "0" + numberString;
        
        
        String result;
        
        if(hasAreaCode)
            result = areaString + "-" + exchangeString + "-" + numberString;
        else
            result =  exchangeString + "-" + numberString;
            
        return result;
    }

}
