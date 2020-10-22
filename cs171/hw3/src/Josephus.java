import java.util.Scanner;

public class Josephus {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("How many people are in the circle?");
        int numPeople = scan.nextInt();
        System.out.println("The process will kill every nth person. Enter n");
        int n = scan.nextInt();
        whoWillBeKilled(numPeople, n);
        scan.close();
    }

    public static void whoWillBeKilled(int numPeople, int n) {
        QueueArray<Integer> queue = new QueueArray<>();

        for (int i = 1; i <= numPeople; i++) {
            queue.enqueue(i);
        }
        System.out.println("Here are the people killed");
        while (!queue.isEmpty()) {
            for (int i = 0; i < n - 1; i++) {
                queue.enqueue(queue.dequeue());
            }
            System.out.print(queue.dequeue() + " ");
        }
    }
}
