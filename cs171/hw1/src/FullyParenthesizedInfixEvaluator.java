import java.util.Scanner;
import java.util.Stack;

public class FullyParenthesizedInfixEvaluator {

    private static String convertToInfix(String expression) {

        try (Scanner scan = new Scanner(expression)) {
            Stack<String> operators = new Stack<>();
            Stack<Double> operands = new Stack<>();

            while (scan.hasNext()) {
            }
            return "";
        } catch (Exception e) {
            throw new NumberFormatException("The expression you entered " +
                    "contains non-postfix math characters");
        }


    }

    public static void main(String[] args) {
        System.out.println("Enter a fully parenthesized infix expression");

        try (Scanner scan = new Scanner(System.in)) {
            String expression = scan.next();
            expression = FullyParenthesizedInfixEvaluator.convertToInfix(expression);
            double result = PostFixEvaluator.evaluate(expression);
            System.out.println(result);
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
    }
}
