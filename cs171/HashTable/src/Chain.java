public class Chain<Key, Value> {

    private Node first;
    private int size;

    public void put(Key key, Value val) {
        for (Node n = first; n != null; n = n.next) {
            if (key.equals(n.key)) {
                n.val = val;
                return;
            }
        }

        first = new Node(key, val, first);
        size++;
    }

    public Value get(Key key) {
        for (Node n = first; n != null; n = n.next) {
            if (key.equals(n.key)) {
                return n.val;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Node n = first; n != null; n = n.next) {
            s.append(n.val).append(" ");
        }
        return s.toString();
    }

    private class Node {
        Key key;
        Value val;
        Node next;

        public Node(Key key, Value val, Node next) {
            this.key = key;
            this.val = val;
            this.next = next;
        }
    }
}
