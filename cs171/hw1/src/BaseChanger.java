//SUBMITTED BY: Simon Marty

import java.util.Scanner;
import java.util.Stack;

public class BaseChanger {

    public static void main(String[] args) {
        System.out.println("Enter a number to convert and the base to convert it to, separated by a space");

        Scanner scanner = new Scanner(System.in);
        String[] inputs = scanner.nextLine().split(" ");
        scanner.close();

        int n = Integer.parseInt(inputs[0]);
        int base = Integer.parseInt(inputs[1]);

        BaseChanger baseChanger = new BaseChanger();
        try {
            System.out.println(baseChanger.convert(n, base));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    /**
     * @param n    the number to be converted
     * @param base the new base
     * @return int n converted to base
     */
    private String convert(int n, int base) throws NumberFormatException {

        if (base <= 10 && base >= 2) {
            Stack<Integer> stack = new Stack<>();
            // Constructs the return string
            // Used instead of concatenation within loop
            // For increased efficiency
            StringBuilder builder = new StringBuilder();
            int rem;

            do {
                rem = n % base;
                n = n / base;
                stack.push(rem);
            } while (n != 0);

            while (!stack.isEmpty()) { // iterate
                builder.append(stack.pop().toString());
            }
            return String.valueOf(builder.toString());
        } else
            throw new NumberFormatException("This program does not handle bases larger than 10 or smaller than 2");
    }
}

