import java.util.Iterator;

public class StackArray<E> implements Iterable<E>, Stack<E> {

    private E[] items;
    private int size;

    public StackArray() {
        items = (E[]) (new Object[1]);
        size = 0;
    }

    public static void main(String[] args) {
        StackArray<String> stack = new StackArray<>();
        stack.push("one");
        stack.push("two");
        stack.push("three");
        stack.push("four");

        stack.pop();

        for (String s : stack) {
            System.out.println(s);
        }

        System.out.println(stack);
    }

    public void push(E element) {
        if (size == items.length) {
            resize(items.length * 2);
        }
        items[size++] = element;
    }

    public E pop() {
        if (this.isEmpty()) return null;
        E item = items[--size];
        items[size] = null;
        if (size == items.length / 4 && size != 0) resize(items.length / 2);
        return item;
    }

    public boolean isEmpty() {
        return (size == 0);
    }

    @Override
    public int size() {
        return this.items.length;
    }

    private void resize(int capacity) {
        E[] temp = (E[]) (new Object[capacity]);
        System.arraycopy(items, 0, temp, 0, size);
        items = temp;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (E item : this) {
            s.append(item.toString()).append(" ");
        }
        return s.toString();
    }

    @Override
    public Iterator<E> iterator() {

        return new Iterator<>() {

            private int nextPos = 0;

            @Override
            public boolean hasNext() {
                return nextPos < size;
            }

            @Override
            public E next() {
                return items[nextPos++];
            }
        };
    }
}
