public class BST<Key extends Comparable<Key>, Value> implements BinaryTree<Key, Value> {

    private Node root;

    @Override
    public void put(Key key, Value value) {
        root = put(key, value, root);
    }

    private Node put(Key key, Value val, Node n) {
        if (n == null)
            return new Node(key, val, 1);

        int cmp = key.compareTo(n.key);
        if (cmp < 0)
            n.left = put(key, val, n.left);
        else if (cmp > 0)
            n.right = put(key, val, n.right);
        else
            n.val = val;
        n.count = size(n.left) + size(n.right) + 1;
        return n;
    }

    @Override
    public Value get(Key key) {
        return get(key, root);
    }

    private Value get(Key key, Node n) {
        if (n == null)
            return null;
        int cmp = key.compareTo(n.key);
        if (cmp < 0)
            return get(key, n.left); // key < n.key
        if (cmp > 0)
            return get(key, n.right); // key > n.key
        else
            return n.val; // key == n.key
    }

    @Override
    public void delete(Key key) {
        root = delete(root,key);
    }

    private Node delete(Node n, Key key) {
        if(n == null) return null;
        int cmp = key.compareTo(n.key);
        if(cmp < 0) n.left = delete(n.left, key); // key is smaller than n.key
        if(cmp > 0) n.right = delete(n.right, key);
        else {
            if(n.right == null) return n.left;
            Node t = n;
            n = select(t.right, 0);
            n.right = deleteMin(t.right);
            n.left = t.left;
        }
        n.count = size(n.left) + size(n.right) + 1;
        return n;
    }

    @Override
    public int size() {
        return size(root);
    }

    private int size(Node n) {
        return ((n == null) ? 0 : n.count);
    }

    public Iterable<Key> keysInOrder() {
        Queue<Key> queue = new QueueArray<Key>();
        keysInOrder(root, queue);
        return queue;
    }

    private void keysInOrder(Node n, Queue<Key> q) {
        if (n == null)
            return;
        keysInOrder(n.left, q);
        q.enqueue(n.key);
        keysInOrder(n.right, q);
    }

    public Iterable<Key> keysPostOrder() {
        Queue<Key> queue = new QueueArray<>();
        keysPostOrder(root, queue);
        return queue;
    }

    private void keysPostOrder(Node n, Queue<Key> q) {
        if (n == null)
            return;
        keysPostOrder(n.left, q);
        keysPostOrder(n.right, q);
        q.enqueue(n.key);
    }

    public Iterable<Key> keysPreOrder() {
        Queue<Key> queue = new QueueArray<>();
        keysPreOrder(root, queue);
        return queue;
    }

    public Key min() {
        return min(root).key;
    }

    public Node min(Node n) {
        if (n.left == null)
            return n;
        else
            return min(n.left);
    }

    public Key floor(Key key) {
        Node n = floor(root, key);
        if (n == null)
            return null;
        else
            return n.key;
    }

    private Node floor(Node n, Key key) {
        if (n == null)
            return null;
        int cmp = key.compareTo(n.key);
        if (cmp == 0)
            return n;
        else if (cmp < 0)
            return floor(n.left, key);
        Node m = floor(n.right, key);
        if (m != null)
            return m;
        else
            return n;
    }

    public int rank(Key key) {
        return rank(key, root);
    }

    private int rank(Key key, Node n) {
        if (n == null)
            return 0;
        int cmp = key.compareTo(n.key);
        if (cmp < 0)
            return rank(key, n.left);
        else if (cmp > 0)
            return 1 + size(n.left) + rank(key, n.right);
        else
            return size(n.left);
    }

    public Key select(int rank) {
        return select(root, rank).key;
    }

    private Node select(Node n, int rank) {
        if (n == null)
            return null;
        int numToLeft = size(n.left);
        if (numToLeft > rank)
            return select(n.left, rank);
        else if (numToLeft < rank)
            return select(n.right, rank - numToLeft - 1);
        return n;
    }

    private void keysPreOrder(Node n, Queue<Key> q) {
        if (n == null)
            return;
        q.enqueue(n.key);
        keysPreOrder(n.left, q);
        keysPreOrder(n.right, q);
    }

    private Node deleteMin(Node n) {
        if(n.left == null) return n.right;
        n.left = deleteMin(n.left);

        n.count = size(n.left) + size(n.right) + 1;
        return n;
    }

    private class Node {
        private Key key;
        private Value val;
        private Node left;
        private Node right;
        private int count;

        public Node(Key key, Value val, int count) {
            this.key = key;
            this.val = val;
            this.count = count;
        }
    }
}