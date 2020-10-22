public interface BinaryTree<Key extends Comparable<Key>, Value> {
    void put(Key key, Value value);

    Value get(Key key);

    void delete(Key key);

    int size();

    class Node {
    }
}
