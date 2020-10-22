// SUBMITTED BY: Simon Marty
import java.security.InvalidParameterException;
import java.util.Scanner;
import java.util.Stack;


public class ShuntingYard {

    final private String[][] OPS_BY_PRECEDENCE = {{"+", "-"}, {"*", "/"}, {"^"}};
    final private String[] RIGHT_ASSOCIATIVE_OPS = {"^"};

    public static void main(String[] args) {

        ShuntingYard sy = new ShuntingYard();
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter an infix expression");
        String expression = scan.nextLine();
        System.out.println(sy.toPreFix(expression));
        scan.close();
    }

    public String toPostFix(String input) {
        Stack<String> operators = new Stack<>();
        StringBuilder output = new StringBuilder();
        String[] terms = input.split(" ");


        for (String term : terms) {
            if (term.equals("(")) {
                operators.push(term);
            } else if (term.equals(")")) {
                while (!operators.peek().equals("(")) {
                    output.append(operators.pop()).append(" ");
                }
                operators.pop(); //get rid of left paren
            } else if (!isOperator(term)) {
                output.append(term).append(" ");
            } else {
                boolean operatorProcessed = false;
                while (!operatorProcessed) {
                    if (operators.isEmpty() || operators.peek().equals("(")) {
                        operators.push(term);
                        operatorProcessed = true;
                    } else {
                        String topOperator = operators.peek();
                        int precedTerm = getPrecedence(term);
                        int precedTop = getPrecedence(topOperator);

                        if (precedTerm > precedTop ||
                                (precedTop == precedTerm && isRightAssociative(term))) {
                            operators.push(term);
                            operatorProcessed = true;
                        } else {
                            output.append(operators.pop()).append(" ");
                        }
                    }
                }
            }
        }
        while (!operators.isEmpty()) {
            output.append(operators.pop()).append(" ");
        }
        return output.toString();
    }

    public String toPreFix(String inputStr) {
        inputStr = toPostFix(inputStr);
        Scanner scan = new Scanner(inputStr);
        Stack<String> operands = new Stack<>();

        while (scan.hasNext()) {
            String next = scan.next();
            if (!isOperator(next)){
                operands.push(next);
            } else {
                String n2 = operands.pop();
                String n1 = operands.pop();

                switch (next) {
                    case "+":
                        operands.push("( + " + n1 + " " + n2 + " ) ");
                        break;
                    case "-":
                        operands.push("( - " + n1 + " " + n2 + " ) ");
                        break;
                    case "*":
                        operands.push("( * " + n1 + " " + n2 + " ) ");
                        break;
                    case "/":
                        operands.push("( / " + n1 + " " + n2 + " ) ");
                        break;
                    case "^":
                        operands.push("( ^ " + n1 + " " + n2 + " ) ");
                        break;
                    default:
                        throw new IllegalArgumentException("The expression you entered " +
                                "contains non-postfix math characters");
                }

            }
        }
        scan.close();
        return operands.pop();
    }

    private boolean isOperator(String s) {
        for (String[] array : OPS_BY_PRECEDENCE) {
            for (String op : array) {
                if (op.equals(s)) return true;
            }
        }
        return false;
    }

    private boolean isRightAssociative(String s) {
        for (String op : RIGHT_ASSOCIATIVE_OPS) {
            if (s.equals(op)) return true;
        }
        return false;
    }

    private int getPrecedence(String op) throws InvalidParameterException {
        for (int i = 0; i < OPS_BY_PRECEDENCE.length; i++) {
            for (int j = 0; j < OPS_BY_PRECEDENCE[i].length; j++) {
                if (OPS_BY_PRECEDENCE[i][j].equals(op)) return i;
            }

        }
        throw new InvalidParameterException("Invalid operator specified: " + op);
    }
}
