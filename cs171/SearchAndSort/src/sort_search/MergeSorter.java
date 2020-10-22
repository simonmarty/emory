import java.util.Arrays;

public class MergeSorter<Item extends Comparable<Item>> implements Sorter<Item> {

    Item[] a;
    Item[] aux;

    public static void main(String[] args) {
        Character[] a = {'K', 'R', 'A', 'T', 'E', 'L', 'E', 'P', 'U', 'I', 'M', 'Q', 'C', 'X', 'O', 'S'};
        MergeSorter<Character> mergeSorter = new MergeSorter<Character>();
        mergeSorter.sort(a);
        System.out.println(Arrays.toString(a));
    }

    private boolean less(Item v, Item w) {
        return (v.compareTo(w) < 0);
    }

    public void sort(Item[] a) {
        this.a = a;
        this.aux = (Item[]) (new Comparable[a.length]);  // <-- no support for generic array creation
        mergeSort(0, a.length - 1);
    }

    private void mergeSort(int lo, int hi) {
        if (hi <= lo) return;
        int mid = lo + (hi - lo) / 2;

        mergeSort(lo, mid);
        mergeSort(mid + 1, hi);

        if (!less(a[mid + 1], a[mid])) return;  // don't waste time with a merge
        // if a[] is already in order

        merge(lo, mid, hi);
    }

    private void merge(int lo, int mid, int hi) {
        //copy to auxiliary array...
        if (hi + 1 - lo >= 0) System.arraycopy(a, lo, aux, lo, hi + 1 - lo);

        //merge...
        int i = lo;
        int j = mid + 1;
        for (int k = lo; k <= hi; k++) {
            if (i > mid) a[k] = aux[j++];
            else if (j > hi) a[k] = aux[i++];
            else if (less(aux[j], aux[i])) a[k] = aux[j++];
            else a[k] = aux[i++];
        }
    }
}
