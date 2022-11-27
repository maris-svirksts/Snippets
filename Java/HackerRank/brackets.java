import java.util.*;
import java.util.Scanner;

// Write your code here. DO NOT use an access modifier in your class declaration.
class Parser{
    static String isBalanced(String s) 
    {
        while(true){
            int initial_lenght = s.length();
            s = s.replace("()", "");
            s = s.replace("[]", "");
            s = s.replace("{}", "");
            if( s.length() == initial_lenght ){
                break;
            }
        }
        
        if(s.length() == 0){
            return "true";
        } else {
            return "false";
        }
    }
}

class Solution {
	
	public static void main(String[] args) {
		Parser parser = new Parser();
        
		Scanner in = new Scanner(System.in);

		while (in.hasNext()) {
			System.out.println(parser.isBalanced(in.next()));
		}
        
		in.close();
	}
}
