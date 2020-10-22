/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.Comparator;

public class LinkedHeapPQ<K, V> extends AbstractPriorityQueue<K, V> {
    private LinkedPQEntry<K, V> root;
    private int size = 0;   // total number of nodes

    public LinkedHeapPQ() {
        super();
    }

    public LinkedHeapPQ(Comparator<K> c) {
        super(c);
    }

    public LinkedHeapPQ(K[] keys, V[] values) {
        this();
        if (keys.length != values.length)
            throw new IllegalArgumentException();
        for (int i = 0; i < keys.length; i++) {
            this.insert(keys[i], values[i]);
        }
    }

    public LinkedHeapPQ(K[] keys, V[] values, Comparator<K> c) {
        this(c);
        if (keys.length != values.length)
            throw new IllegalArgumentException();
        for (int i = 0; i < keys.length; i++) {
            this.insert(keys[i], values[i]);
        }
    }

    @Override
    public LinkedPQEntry<K, V> insert(K key, V value) throws IllegalArgumentException {
        checkKey(key);
        LinkedPQEntry<K, V> entry = new LinkedPQEntry<>(key, value, null, null, null);
        if (size == 0) {
            root = entry;
            size++;
            return root;
        }

        int locationOfNextNode = size + 1;
        LinkedPQEntry<K, V> parent = traverseToThisEntry(locationOfNextNode / 2);
        if (locationOfNextNode % 2 == 0) {
            parent.setLeftChild(entry);
        } else {
            parent.setRightChild(entry);
        }
        entry.setParent(parent);

        size++;
        swim(entry);
        return entry;
    }

    @Override
    public Entry<K, V> min() {
        return root;
    }

    private void swim(LinkedPQEntry<K, V> node) {
        while(node.getParent() != null) {
            LinkedPQEntry<K, V> parent = node.getParent();
            if (compare(node, parent) >= 0) break;
            swap(node, parent);

            node = parent;
        }
    }

    private LinkedPQEntry<K, V> traverseToThisEntry(int position) {
        if(position == 1) return root;
        char[] pathToTake = Integer.toBinaryString(position).substring(1).toCharArray();
        LinkedPQEntry<K, V> pointer = root;
        for(char c : pathToTake) {
            if(c == '0') pointer = pointer.getLeftChild();
            else if (c == '1') pointer = pointer.getRightChild();
        }
        return pointer;
    }

    @Override
    public Entry<K, V> removeMin() {
        if(root == null) return null;
        LinkedPQEntry<K, V> entry;
        if(size == 1) {
            entry = root;
            root = null;
            size = 0;
            return entry;
        }
        if(size == 2) {
            entry = root;
            root = root.getLeftChild();
            size = 1;
            return entry;
        }

        entry = traverseToThisEntry(size);  // last element
        if(entry != null) {
            swap(entry, root);

            if(entry.getParent() != null) {
                LinkedPQEntry<K, V> parent = entry.getParent();
                if(parent.getRightChild() == entry) parent.setRightChild(null);
                if(parent.getLeftChild() == entry) parent.setLeftChild(null);
            }
            entry.setParent(null);

            sink(root);
        }
        size--;
        return entry;
    }

    private void sink(LinkedPQEntry<K, V> node) {
        while(node.getLeftChild() != null) {
            LinkedPQEntry<K, V> nodeToSwapWith = node.getLeftChild();

            if(node.getRightChild() != null) {
                if(compare(node.getLeftChild(), node.getRightChild()) > 0)
                    nodeToSwapWith = node.getRightChild();
            }

            if(compare(nodeToSwapWith, node) >= 0) break;

            swap(nodeToSwapWith, node);

            node = nodeToSwapWith;
        }
    }

    /**
     * Returns the number of nodes in the tree.
     */
    public int size() {
        return size;
    }

    private void swap(LinkedPQEntry<K, V> node1, LinkedPQEntry<K, V> node2) {
        K tempKey = node1.getKey();
        V tempValue = node1.getValue();
        node1.setKey(node2.getKey());
        node1.setValue(node2.getValue());
        node2.setKey(tempKey);
        node2.setValue(tempValue);
    }

    protected static class LinkedPQEntry<K, V> extends PQEntry<K, V> {
        private LinkedPQEntry<K, V> parent;
        private LinkedPQEntry<K, V> leftChild;
        private LinkedPQEntry<K, V> rightChild;

        LinkedPQEntry(K key, V value, LinkedPQEntry<K, V> parent, LinkedPQEntry<K, V> leftChild, LinkedPQEntry<K, V> rightChild) {
            super(key, value);
            this.parent = parent;
            this.leftChild = leftChild;
            this.rightChild = rightChild;
        }

        public LinkedPQEntry<K, V> getParent() {
            return parent;
        }

        public LinkedPQEntry<K, V> getLeftChild() {
            return leftChild;
        }

        public LinkedPQEntry<K, V> getRightChild() {
            return rightChild;
        }

        public void setParent(LinkedPQEntry<K, V> parent) {
            this.parent = parent;
        }

        public void setLeftChild(LinkedPQEntry<K, V> leftChild) {
            this.leftChild = leftChild;
        }

        public void setRightChild(LinkedPQEntry<K, V> rightChild) {
            this.rightChild = rightChild;
        }
    }
}