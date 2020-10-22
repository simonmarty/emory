public class BubbleSorter<Item extends Comparable<Item>> implements Sorter<Item> {

    private void swap(Item[] a, int i, int j) {
        Item temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    private boolean less(Item v, Item w) {
        return v.compareTo(w) < 0;
    }

    @Override
    public void sort(Item[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            for (int j = 0; j < a.length - 1 - i; j++) {
                if (less(a[j], a[j]))
                    swap(a, i, j);
            }
        }
    }
}