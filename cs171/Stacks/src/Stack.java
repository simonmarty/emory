public interface Stack<E> extends Iterable<E> {

    boolean isEmpty();
    int size();

    void push(E item);

    E pop();
    //Iterator<E> iterator();

}
