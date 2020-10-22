// Min heap
public class Heap<T extends Comparable<T>> {
    private T[] t;
    private int size;

    public Heap(int size) {
        t = (T[]) new Comparable[1 + size];
    }

    public int size() {
        return size;
    }

    public void put(T type) {
        t[++size] = type;
        swim(size);
    }

    public T popMin() {
        T type = t[1];
        t[1] = t[size];
        t[size--] = null;
        sink();
        return type;
    }

    @Override
    public String toString() {
        StringBuilder strb = new StringBuilder();
        for(int i = 1; i <= size; i++) {
            strb.append(t[i]).append(" ");
        }
        return strb.toString();
    }

    private void sink() {
        int i = 1;
        while(i*2 <= size) {
            int j = 2*i;
            if(j < size && less(j+1, j)) {
                j++;
            }
            if(less(i, j)) {
                break;
            } 
            swap(i, j);
            i = j;
        }
    }

    private void swim(int i) {
        while (i > 1 && less(i, i / 2)) {
            swap(i / 2, i);
            i /= 2;
        }
    }

    private boolean less(int v, int w) {
        return t[v].compareTo(t[w]) < 0;
    }

    private void swap(int i, int j) {
        T temp = t[i];
        t[i] = t[j];
        t[j] = temp;
    }
}
