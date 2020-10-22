/*
THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. Simon Marty
*/



import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

public class Arithmetic {

    private static HashMap<Character, Integer> map;
    private static final char[] OPERATORS = {'+', '-', '*', '/', '%'};

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        for (; ; ) {
            System.out.println("Please enter an arithmetic problem:");
            String s = scan.nextLine();
            if (s.trim().toUpperCase().equals("Q")) break;

            System.out.println(doMath(s));
        }
    }

    private static int getOpCode(char c) {
        if (map == null) {
            map = new HashMap<>();
            for (int i = 0; i < OPERATORS.length; i++)
                map.put(OPERATORS[i], i);
        }
        return map.get(c);
    }

    public static String doMath(String a) {
        final int ADDITION = 0;
        final int SUBTRACTION = 1;
        final int MULTIPLICATION = 2;
        final int DIVISION = 3;
        final int MODULO = 4;

        String[] expression = a.split(" ");
        boolean num1IsNegative = expression[0].charAt(0) == '(';
        boolean num2isNegative = expression[2].charAt(0) == '(';

        if (num1IsNegative) {
            expression[0] = expression[0].substring(2, expression[0].length() - 1);
            expression[0] = Arithmetic.getTwosComplement(Arithmetic.toBinary(expression[0]));
        } else {
            expression[0] = Arithmetic.toBinary(expression[0]);
        }
        if (num2isNegative) {
            expression[2] = expression[2].substring(2, expression[2].length() - 1);
            expression[2] = Arithmetic.getTwosComplement(Arithmetic.toBinary(expression[2]));
        } else {
            expression[2] = Arithmetic.toBinary(expression[2]);
        }



        int opCode = getOpCode(expression[1].charAt(0));
        String binResult = "";

        switch (opCode) {
            case ADDITION:
                binResult = Arithmetic.add(expression[0], expression[2]);
                break;
            case SUBTRACTION:
                binResult = Arithmetic.subtract(expression[0], expression[2]);
                break;
            case MULTIPLICATION:
                binResult = Arithmetic.multiply(expression[0], expression[2]);
                break;
            case DIVISION:
                binResult = Arithmetic.getQuotient(expression[0], expression[2]);
                break;
            case MODULO:
                binResult = Arithmetic.getRemainder(expression[0], expression[2]);
                break;
        }

        return "Result as a hex string: " + toHex(binResult) + "\n" +
                "Result as an integer: " + toDecimal(binResult) + "\n";
    }

    static String toBinary(String s) {
        int value = parseInt(s);
        if (value < 0) {
            value *= -1;
            value = ~value + 1;
        }
        Stack<Integer> stack = new Stack<>();
        while (value > 0) {
            stack.push(value % 2);
            value /= 2;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        int len = sb.length();
        if (len < 32) {
            for (int i = 0; i < 32 - len; i++) {
                sb.insert(0, '0');
            }
        }

        return sb.toString();
    }

    static int parseInt(String s) {
        int magnitude = 1;
        int result = 0;
        boolean isNegative = false;
        if (s.charAt(0) == '-') {
            isNegative = true;
            s = s.substring(1);
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            byte digit = (byte) (s.charAt(i) - '0');
            result += digit * magnitude;
            magnitude *= 10;
        }
        if (isNegative) result *= -1;
        return result;
    }

    static int toDecimal(String s) {
        boolean isNegative = false;
        if (s.charAt(0) == '1' && s.length() >= 32) {
            isNegative = true;
            s = getTwosComplement(s);
        }
        int base = 1;
        int result = 0;
        int len = s.length();
        for (int i = len - 1; i >= 0; i--) {
            if (s.charAt(i) == '1') {
                result += base;
            }
            base *= 2;
        }
        if (isNegative) {
            result *= -1;
        }
        return result;
    }

    static String toHex(String bin) {
        HashMap<String, String> map = new HashMap<>();
        final String[] HEX_VALS = {"1010", "1011", "1100", "1101", "1110", "1111"};
        final String[] HEX_LETTERS = {"A", "B", "C", "D", "E", "F"};
        for (int i = 0; i < HEX_VALS.length; i++)
            map.put(HEX_VALS[i], HEX_LETTERS[i]);
        int len = bin.length();
        if (len < 32) {
            StringBuilder sb = new StringBuilder(bin);
            for (int i = 0; i < 32 - len; i++)
                sb.insert(0, "0");
            bin = sb.toString();
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < len - 3; i += 4) {
            String substring = bin.substring(i, i + 4);
            if (map.containsKey(substring)) result.append(map.get(substring));
            else {
                result.append(Arithmetic.toDecimal(substring));
            }
            if (i % 8 != 0) {
                result.append(" ");
            }
        }
        return result.toString();
    }

    static String getTwosComplement(String s) {
        char[] arr = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : arr) {
            if (c == '1') sb.append('0');
            else sb.append('1');
        }
        return Arithmetic.add(sb.toString(), "00000000000000000000000000000001");
    }

    static String add(String a, String b) {
        if (a.length() > b.length() && a.length() > 32) {
            a = a.substring(a.length() - 32);
        } else if (a.length() < b.length() && b.length() > 32) {
            b = b.substring(b.length() - 32);
        }
        boolean carry = false;
        char[] res = new char[a.length()];
        for (int i = a.length() - 1; i >= 0; i--) {
            if (a.charAt(i) == '1' && b.charAt(i) == '1') {
                if (!carry) {
                    res[i] = '0';
                    carry = true;
                } else {
                    res[i] = '1';
                }
            } else if (a.charAt(i) == '1' || b.charAt(i) == '1') {
                if (!carry) {
                    res[i] = '1';
                } else {
                    res[i] = '0';
                }
            } else if (carry) {
                res[i] = '1';
                carry = false;
            } else {
                res[i] = '0';
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c : res) {
            sb.append(c);
        }
        return sb.toString();
    }

    static String subtract(String a, String b) {
        String c = getTwosComplement(b);
        return Arithmetic.add(a, c);
    }

    static String multiply(String a, String b) {
        char[] arr = b.toCharArray();
        String result = String.join("", Collections.nCopies(32, "0"));
        for (int i = 0; i < b.length(); i++) {
            if (arr[arr.length - 1 - i] == '1')
                result = Arithmetic.add(a + String.join("", Collections.nCopies(i, "0")), result);
        }

        return result;
    }

    static ArrayList<String> divide(String a, String b) {

        String quotient = String.join("", Collections.nCopies(32, "0"));
        boolean negative = false;

        if(a.charAt(0) == '1') {
            a = Arithmetic.getTwosComplement(a);
            negative = true;
        }
        if(b.charAt(0) == '1') {
            b = Arithmetic.getTwosComplement(b);
            negative = !negative;
        }
        String remainder = a;

        while (subtract(remainder, b).charAt(0) != '1') {
            remainder = subtract(remainder, b);
            quotient = Arithmetic.add(quotient, String.join("", Collections.nCopies(31, "0")) + "1");
        }

        ArrayList<String> res = new ArrayList<>();
        res.add(quotient);
        res.add(remainder);

        if(negative) {
            res.set(0, Arithmetic.getTwosComplement(res.get(0)));
            res.set(1, Arithmetic.getTwosComplement(res.get(1)));
        }
        return res;
    }

    static String getQuotient(String a, String b) {
        return divide(a, b).get(0);
    }

    static String getRemainder(String a, String b) {
        return divide(a, b).get(1);
    }
}
