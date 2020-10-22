public class RedBlackBST<Key extends Comparable<Key>, Value> {

    private static final boolean RED = true;
    private static final boolean BLACK = false;

    private Node root;

    private class Node {
        Key key;
        Value val;
        Node left;
        Node right;
        int size;
        boolean color;

        public Node(Key key, Value val, int size, boolean color) {
            this.key = key;
            this.val = val;
            this.size = size;
            this.color = color;
        }
    }

    public int size() {
        return size(root);
    }

    private int size(Node n) {
        if(n == null) return 0;
        return n.size;
    }

    private boolean isRed(Node n) {
        if(n == null) return BLACK;
        return n.color == RED;
    }

    private Node rotateLeft(Node n) {
        Node x = n.right;
        n.right = x.left;
        x.left = n;
        x.color = n.color;
        n.color = RED;
        x.size = n.size;
        n.size = size(n.left) + size(n.right) + 1;
        return x;
    }

    private Node rotateRight(Node n) {
        Node x = n.left;
        n.left = x.left;
        x.right = n;
        x.color = n.color;
        n.color = RED;
        x.size = n.size;
        n.size = size(n.left) + size(n.right) + 1;
        return x;
    }

    private void flipColors(Node n) {
        n.color = RED;
        n.left.color = BLACK;
        n.right.color = BLACK;
    }

    public void put(Key key, Value val) {
        root = put(root, key, val);
        root.color = BLACK;
    }

    private Node put(Node n, Key key, Value val) {
        if(n == null) return new Node(key, val, 1, RED);
        int cmp = key.compareTo(n.key);

        if(cmp < 0) n.left = put(n.left, key, val);
        if(cmp > 0) n.right = put(n.right, key, val);
        else n.val = val;
       
        if(isRed(n.right) && ! isRed(n.left))
            n = rotateLeft(n);
        if(isRed(n.left) && isRed(n.left.left))
            n = rotateRight(n);
        if(isRed(n.left) && isRed(n.right))
            flipColors(n);
        
        n.size = size(n.left) + size(n.right) + 1;
        return n;
    }
}