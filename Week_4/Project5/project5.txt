package project5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SlopChecker {

    public static boolean isSlip(String s) {
        if (s.length() < 3) return false;
        if (s.charAt(0) != 'D' && s.charAt(0) != 'E') return false;
        if (s.charAt(1) != 'F') return false;
        
        int i = 2;
        while (i < s.length() && s.charAt(i) == 'F') i++;
        
        if (i == s.length()) return false;
        if (s.charAt(i) == 'G' && i == s.length() - 1) return true;
        return isSlip(s.substring(i));
    }

    public static boolean isSlap(String s) {
        if (s.length() < 2) return false;
        if (s.charAt(0) != 'A') return false;
        if (s.length() == 2) return s.charAt(1) == 'H';
        
        if (s.charAt(1) == 'B' && s.charAt(s.length() - 1) == 'C') {
            return isSlap(s.substring(2, s.length() - 1));
        }
        if (s.charAt(s.length() - 1) == 'C') {
            return isSlip(s.substring(1, s.length() - 1));
        }
        return false;
    }

    public static boolean isSlop(String s) {
        for (int i = 1; i < s.length(); i++) {
            if (isSlap(s.substring(0, i)) && isSlip(s.substring(i))) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("input.txt"));
        int n = Integer.parseInt(scanner.nextLine());
        
        System.out.println("SLOPS OUTPUT");
        for (int i = 0; i < n; i++) {
            String str = scanner.nextLine();
            System.out.println(isSlop(str) ? "YES" : "NO");
        }
        System.out.println("END OF OUTPUT");
        
        scanner.close();
    }
}

