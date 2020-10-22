// SUBMITTED BY: Simon Marty

public class MergeSorterNR<T extends Comparable<T>> implements Sorter<T> {

    private T[] a;
    private T[] aux;

    @SuppressWarnings("unchecked")
    public void sort(T a[]) {
        this.a = a;
        this.aux = (T[]) new Comparable[a.length];
        int n = a.length;

        // int size: the size of the subarrays
        // int l: the index of the left subarray to be merged
        // int mid: the index of the right subarray to be merged
        // int h: the last index of my second subarray, where h + 1 is the l of the next pair
        for (int size = 1; size < n; size *= 2) {
            for (int l = 0; l < n - size; l += 2 * size) {
                int mid = size + l - 1;
                int h = Math.min(l + 2 * size - 1, n - 1);
                if (a[mid].compareTo(a[mid + 1]) > 0)
                    merge(l, mid, h);
            }
        }
    }

    private boolean less(T v, T w) {
        return v.compareTo(w) < 0;
    }

    private void merge(int l, int mid, int h) {

        System.arraycopy(a, l, aux, l, h + 1 - l);

        int i = l;
        int j = mid + 1;

        for (int k = l; k <= h; k++) {
            if (i > mid)
                a[k] = aux[j++];
            else if (j > h)
                a[k] = aux[i++];
            else if (less(aux[j], aux[i]))
                a[k] = aux[j++];
            else
                a[k] = aux[i++];
        }

    }
}