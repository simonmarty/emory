/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;

public class ArrayHeapPQ<K, V> extends AbstractPriorityQueue<K, V> {
    private final ArrayList<PQEntry<K, V>> list = new ArrayList<>();

    public ArrayHeapPQ() {
        super();
    }

    public ArrayHeapPQ(Comparator<K> comp) {
        super(comp);
    }

    public ArrayHeapPQ(K[] keys, V[] values) {
        super();
        for (int j = 0; j < Math.min(keys.length, values.length); j++)
            list.add(new PQEntry<>(keys[j], values[j]));
        heapify();
    }

    public ArrayHeapPQ(K[] keys, V[] values, Comparator<K> comp) {
        super(comp);
        for (int j = 0; j < Math.min(keys.length, values.length); j++)
            list.add(new PQEntry<>(keys[j], values[j]));
        heapify();
    }

    public List<PQEntry<K,V>> sort() {
        for(int i = this.size(); i > 0; i--) {
            PQEntry<K, V> e = this.removeMin();
            list.add(e);
        }

        return list;
    }

    private void heapify() {
        int startIndex = parent(this.size() - 1); // start at PARENT of last entry
        for (int j = startIndex; j >= 0; j--) // loop until processing the root
            sink(j);
    }

    private int parent(int j) {
        return (j - 1) / 2;
    }

    private int left(int j) {
        return j * 2 + 1;
    }

    private int right(int j) {
        return j * 2 + 2;
    }

    private boolean hasLeft(int j) {
        return left(j) < this.size();
    }

    private boolean hasRight(int j) {
        return right(j) < this.size();
    }

    private void swap(int i, int j) {
        Collections.swap(list, i, j); // using this out of convenience
    }

    private void swim(int i) {
        while (i > 0) {
            int p = parent(i);
            if (super.compare(list.get(i), list.get(p)) >= 0) break; // child is larger than
            swap(i, p);
            i = p;
        }
    }

    private void sink(int i) {
        while (hasLeft(i)) {
            int leftIndex = left(i);
            int minIndex = leftIndex;

            if (hasRight(i)) {
                int rightIndex = right(i);
                if (compare(list.get(leftIndex), list.get(rightIndex)) > 0)
                    minIndex = rightIndex;
            }

            if (compare(list.get(minIndex), list.get(i)) >= 0) break;

            swap(i, minIndex);
            i = minIndex;
        }
    }

    @Override
    public int size() {
         return list.size();
    }

    @Override
    public PQEntry<K, V> insert(K key, V value) throws IllegalArgumentException {
        super.checkKey(key);
        PQEntry<K, V> entry = new PQEntry<>(key, value);
        list.add(entry);
        swim(list.size() - 1);
        return entry;
    }

    @Override
    public PQEntry<K, V> min() {
        if (list.isEmpty()) return null;
        return list.get(0);
    }

    @Override
    public PQEntry<K, V> removeMin() {
        if (this.isEmpty()) return null;
        PQEntry<K, V> entry = list.get(0);
        swap(0, list.size() - 1);
        list.remove(list.size() - 1);
        sink(0);
        return entry;
    }

}
