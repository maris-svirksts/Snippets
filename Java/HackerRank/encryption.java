import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'decryptMessage' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING encryptedMessage as parameter.
     */

    public static String decryptMessage(String encryptedMessage) {
        for(int i = 0; i < encryptedMessage.length(); i++) {
            if( Character.isDigit(encryptedMessage.charAt(i)) ) {
                int N            = Character.getNumericValue(encryptedMessage.charAt(i)) - 1;
                char[] charArray = new char[N];

                for (int y = 0; y < N; y++) {
                    charArray[y] = encryptedMessage.charAt(i - 1);
                }

                String newString = new String(charArray);

                encryptedMessage = encryptedMessage.substring(0, i) + newString + encryptedMessage.substring(i + 1);
            }
        }

        List<String> messageAsList = new ArrayList<String>(Arrays.asList(encryptedMessage.split(" ")));
        Collections.reverse(messageAsList);



        return String.join(" ", messageAsList);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String encryptedMessage = bufferedReader.readLine();

        String result = Result.decryptMessage(encryptedMessage);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}