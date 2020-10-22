/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class HeapComparisonTest {
    // I made these fields static for the sake of convenience, since this is a test class
    private static int ARRAY_LENGTH = 10000000;
    private static final int REMOVE_ELEMENT_COUNT = 10000000;
    private static final int NUM_ELEMENTS_TO_REMOVE = Math.min(REMOVE_ELEMENT_COUNT, ARRAY_LENGTH);
    private static Integer[] keys;
    private static Integer[] values;

    public static void main(String[] args) {
        createEntries();
        double time1 = ArrayHeapPQTest();
            System.out.println("\nThe array implementation took " +
                    time1 + "s to sort " + ARRAY_LENGTH + " elements");

            double time2 = LinkedHeapPQTest();
            System.out.println("\nThe tree implementation took " +
                    time2 + "s to add " + ARRAY_LENGTH + " elements");
    }

    private static double ArrayHeapPQTest() {
        ArrayList<Entry<Integer, Integer>> result = new ArrayList<>();

        // ---------- TIMING BLOCK -----------------
        long startTime = System.currentTimeMillis();

        PriorityQueue<Integer, Integer> priorityQueue = new ArrayHeapPQ<>(keys, values);
        for (int i = 0; i <= ARRAY_LENGTH; i++) {
            result.add(priorityQueue.removeMin());
        }

        long totalTime = System.currentTimeMillis() - startTime;
        // ---------- END TIMING BLOCK --------------

        /*System.out.println("Head of sorted result using array implementation, first " + NUM_ELEMENTS_TO_REMOVE + " elements:");
        for (int i = 0; i < Math.min(NUM_ELEMENTS_TO_REMOVE, result.size()); i++) {
            System.out.print(result.get(i).getKey() + " ");
        }*/
        return (double) totalTime / 1000.0;
    }

    private static double LinkedHeapPQTest() {
        ArrayList<Entry<Integer, Integer>> result = new ArrayList<>();

        // ---------- TIMING BLOCK -----------------
        long startTime = System.currentTimeMillis();

        PriorityQueue<Integer, Integer> priorityQueue = new LinkedHeapPQ<>(keys, values);
        for (int i = 0; i <= NUM_ELEMENTS_TO_REMOVE; i++) {
            result.add(priorityQueue.removeMin());
        }

        long totalTime = System.currentTimeMillis() - startTime;
        // ---------- END TIMING BLOCK --------------

        /*System.out.println("Head of sorted result using linked tree implementation, first " + NUM_ELEMENTS_TO_REMOVE + " elements:");
        for (int i = 0; i < Math.min(NUM_ELEMENTS_TO_REMOVE, result.size()); i++) {
            System.out.print(result.get(i).getKey() + " ");
        }*/
        return (double) totalTime / 1000.0;
    }

    /**
     * Fills my two arrays with random integers > 0, not timed.
     * I'm keeping the numbers pretty small so it's easy to quickly tell which are bigger.
     * This test works with any integer.
     */
    private static void createEntries() {
        keys = new Integer[ARRAY_LENGTH];
        values = new Integer[ARRAY_LENGTH];

        for (int i = 0; i < ARRAY_LENGTH; i++) {
            keys[i] = ThreadLocalRandom.current().nextInt(133713);
            values[i] = i + 1;
        } // filling this with random values
    }
}
