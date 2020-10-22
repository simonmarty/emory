import java.util.Scanner;

public class ZeroAndNines {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Find the smallest multiple (with digits only zero and nine) of what value?");
        System.out.println(smallestMultiple(scan.nextInt()));
        scan.close();
    }

    public static long smallestMultiple(int n) {
        QueueArray<String> queue = new QueueArray<>();
        long value;
        queue.enqueue("9"); // no need to enqueue 0
        do {
            String front = queue.dequeue();
            value = Long.parseLong(front);

            queue.enqueue(front + "0");
            queue.enqueue(front + "9");
        } while (value % n != 0);

        return value;
    }
}
