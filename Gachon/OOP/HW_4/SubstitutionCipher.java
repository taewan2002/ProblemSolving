package HW_4;

public class SubstitutionCipher implements MessageDecoder, MessageEncoder {
    public static int shift;

    public SubstitutionCipher(int s){
        shift = s;
    }

    public String encode(String message){
        char[] str = new char[message.length()];
        str = message.toCharArray();
        for(int i=0; i<message.length(); i++){
            /** shift string to + */
            str[i] += shift;
        }
        String newMessage = new String(str); 
        return newMessage;
    }

    public String decode(String message){
        char[] str = new char[message.length()];
        str = message.toCharArray();
        for(int i=0; i<message.length(); i++){
            /** shift string to - */
            str[i] -= shift;
        }
        String newMessage = new String(str); 
        return newMessage;
    }
}
