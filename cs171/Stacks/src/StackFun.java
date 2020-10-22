import java.util.Stack;

public class StackFun {

    public static void main(String[] args) {

        Stack<String> stack = new Stack<>();
        stack.push("A");
        stack.push("B");
        stack.push("C");

        System.out.println(stack.size());

        stack.insertElementAt("Fred", 2); // Not stack-like characteristic

        System.out.println(stack.pop());
        System.out.println(stack.peek());
        System.out.println(stack.pop());

        while(! stack.isEmpty()) {
            System.out.println(stack.pop());
        }
    }
}