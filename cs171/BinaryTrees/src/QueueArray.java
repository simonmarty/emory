import java.util.Iterator;

public class QueueArray<E> implements Queue<E>, Iterable<E> {

    private int head;
    private int tail;
    private int size;
    private E[] items;

    public QueueArray() {
        // head = tail = size = 0
        items = (E[]) new Object[1];
    }

    @Override
    public void enqueue(E e) {
        if (size == items.length - 1) {
            resize(2 * items.length);
        }
        items[tail++] = e;
        if (tail == items.length) {
            tail = 0;
        }
        size++;
    }

    @Override
    public E dequeue() throws IndexOutOfBoundsException {
        if (this.isEmpty()) {
            throw new IndexOutOfBoundsException("Tried to dequeue an empty queue");
        }
        E itemToReturn = items[head];
        items[head++] = null;
        size--;
        if (head == items.length) {
            head = 0;
        }
        if (size == items.length / 4) {
            resize(items.length / 2);
        }

        return itemToReturn;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }


    @Override
    public Iterator<E> iterator() {
        return new Iterator<>() {

            private int i = head;
            private int count = 0;

            @Override
            public boolean hasNext() {
                return count < size;
            }

            @Override
            public E next() {
                count++;
                E e = items[i++];
                if (i == items.length) {
                    i = 0;
                }
                return e;
            }
        };
    }

    private void resize(int capacity) {
        E[] newArray = (E[]) new Object[capacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = items[(head + i) % items.length];
        }
        items = newArray;
        head = 0;
        tail = size;
    }
}
