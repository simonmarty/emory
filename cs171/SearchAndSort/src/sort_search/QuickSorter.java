import java.util.Arrays;
import java.util.Random;

public class QuickSorter<Item extends Comparable<Item>> implements Sorter<Item> {

    Item[] a;

    public static void main(String[] args) {
        Character[] a = {'K', 'R', 'A', 'T', 'E', 'L', 'E', 'P', 'U', 'I', 'M', 'Q', 'C', 'X', 'O', 'S'};
        QuickSorter<Character> quickSorter = new QuickSorter<Character>();
        quickSorter.sort(a);
        System.out.println(Arrays.toString(a));
    }

    private boolean less(Item v, Item w) {
        return (v.compareTo(w) < 0);
    }

    private void exch(int i, int j) {
        Item temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // needed for performance guarantee (using the quicksort algorithm
    // sorted lists take O(n^2) time, whereas random lists take
    // O(n ln n) time
    private void shuffle() {
        // take elements i = 0..(n-1) in turn and swap them randomly
        // with some position >= i
        Random random = new Random();
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int r = i + random.nextInt(n - i);     // between i and N-1
            exch(i, r);
        }
    }

    private int partition(int lo, int hi) {
        int i = lo;
        int j = hi + 1;
        while (true) {

            while (less(a[++i], a[lo]))   //find item on left to swap
                if (i == hi) break;

            while (less(a[lo], a[--j]))   //find item on right to swap
                if (j == lo) break;

            if (i >= j) break;            //check if pointers cross and we are
            //ready for final exchange

            exch(i, j);                   //swap
        }

        exch(lo, j);     // final exchange (with pivot)

        return j;        // return index of item now known to be in place
    }

    private void sort(int lo, int hi) {
        if (hi <= lo) return;   // base case of one element
        int j = partition(lo, hi);
        sort(lo, j - 1);
        sort(j + 1, hi);
    }

    public void sort(Item[] a) {
        this.a = a;

        //Shuffle array a (needed for performance guarantee)
        shuffle();
        sort(0, a.length - 1);
    }
}
