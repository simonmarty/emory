import java.util.Scanner;

public class StackOfStrings {

    private String[] items;
    private int size;

    public StackOfStrings(int capacity) {
        items = new String[capacity];
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == items.length;
    }

    public static void main(String[] args) {
        System.out.println("Enter a sequence of words and/or dashes separated by spaces.");
        System.out.println("Words will be pushed to an initially empty stack with capacity 5.");
        System.out.println("Dashes will result in popping the stack and printing the result.");
        Scanner scanner = new Scanner(System.in);
        String userInputStr = scanner.nextLine();
        scanner.close();
        String[] userInputs = userInputStr.split(" ");
        StackOfStrings stack = new StackOfStrings(5);
        for (int i = 0; i < userInputs.length; i++) {
            if (userInputs[i].equals("-"))
                System.out.println(stack.pop());
            else
                stack.push(userInputs[i]);
        }
    }

    public void push(String s) {
        if (this.isFull()) {
            expand();
        }
        items[size++] = s;
    }

    public String pop() {
        if (size != 0) {
            String currentVal = this.items[size];
            this.items[size--] = null;
            return currentVal;
        } else throw new RuntimeException("Stack Underflow");
    }

    private void expand() {
        throw new RuntimeException("Stack Overflow");
    }
}
