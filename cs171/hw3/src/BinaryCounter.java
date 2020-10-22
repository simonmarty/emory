import java.util.Scanner;

public class BinaryCounter {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("What number do you want to count to in binary?");
        countTo(scan.nextInt());
        scan.close();
    }

    public static void countTo(int n) {
        QueueArray<String> queue = new QueueArray<>();
        queue.enqueue("1");
        for (int i = 0; i < n; i++) {
            String front = queue.dequeue();
            System.out.println(front);
            queue.enqueue(front + "0");
            queue.enqueue(front + "1");
        }
    }


}
