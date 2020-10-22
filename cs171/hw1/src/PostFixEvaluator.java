import java.util.Scanner;
import java.util.Stack;

public class PostFixEvaluator {

    public static double evaluate(String expression) throws NumberFormatException {
        Stack<Double> operands = new Stack<>();
        Scanner scan = new Scanner(expression);

        while (scan.hasNext()) {
            if (scan.hasNextDouble()) {
                operands.push(scan.nextDouble());
            } else {
                String operator = scan.next();
                try {
                    double n2 = operands.pop();
                    double n1 = operands.pop();

                    switch (operator) {
                        case "+":
                            operands.push(n1 + n2);
                            break;
                        case "-":
                            operands.push(n1 - n2);
                            break;
                        case "*":
                            operands.push(n1 * n2);
                            break;
                        case "/":
                            operands.push(n1 / n2);
                            break;
                        case "^":
                            operands.push(Math.pow(n1, n2));
                            break;
                        default:
                            throw new IllegalArgumentException();
                    }
                } catch (Exception e) {
                    throw new NumberFormatException("The expression you entered " +
                            "contains non-postfix math characters");
                }
            }
        }

        scan.close();

        double result = operands.pop();
        int resultInt = (int) result;
        if (resultInt == result) {
            return resultInt;
        } else {
            return operands.pop();
        }

    }

    public static void main(String[] args) {

        double result;
        String expression;

        System.out.println("Enter a postfix expression");
        System.out.println("Separate every term and operator with a space");

        try (Scanner scan = new Scanner(System.in)) {
            expression = scan.nextLine();
            result = PostFixEvaluator.evaluate(expression);
            System.out.println(expression + " = " + result);
        } catch (NumberFormatException ex) {
            ex.printStackTrace();
        }
    }
}