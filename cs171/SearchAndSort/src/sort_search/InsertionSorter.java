import java.util.Arrays;

public class InsertionSorter<Item extends Comparable<Item>> implements Sorter<Item> {

    Item[] a;

    public static void main(String[] args) {
        Character[] a = {'K', 'R', 'A', 'T', 'E', 'L', 'E', 'P', 'U', 'I', 'M', 'Q', 'C', 'X', 'O', 'S'};
        InsertionSorter<Character> insertionSorter = new InsertionSorter<Character>();
        insertionSorter.sort(a);
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

    public void sort(Item[] a) {
        this.a = a;
        int n = a.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j > 0; j--) {
                if (less(a[j], a[j - 1]))
                    exch(j, j - 1);
                else
                    break;
            }
        }
    }
}

