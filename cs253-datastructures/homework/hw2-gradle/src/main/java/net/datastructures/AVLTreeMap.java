package net.datastructures;

import java.util.Comparator;

public class AVLTreeMap<K, V> extends TreeMap<K, V> {

    private static final boolean BLACK = false;
    private static final boolean RED = true;

    public AVLTreeMap() {
        super();
    }

    public AVLTreeMap(Comparator<K> comp) {
        super(comp);
    }

    protected int height(Position<Entry<K, V>> p) {
        return tree.getAux(p);
    }

    protected void computeHeight(Position<Entry<K, V>> p) {
        tree.setAux(p, 1 + Math.max(height(left(p)), height(right(p))));
    }

    protected int getBalance(Position<Entry<K, V>> p) {
        return tree.getAux(left(p)) - tree.getAux(right(p));
    }

    protected boolean isBalanced(Position<Entry<K, V>> p) {
        return Math.abs(getBalance(p)) <= 1;
    }

    protected Position<Entry<K, V>> tallerChild(Position<Entry<K, V>> p) {
        if (height(left(p)) > height(right(p))) return left(p);
        if (height(right(p)) > height(left(p))) return right(p);

        if (isRoot(p)) return left(p);
        // keep aligning like parent
        if (p == left(parent(p))) return left(p);
        else return right(p);
    }

    protected void rebalance(Position<Entry<K, V>> p) {
        int oldHeight;
        int newHeight;

        do {
            oldHeight = height(p);

            if (!isBalanced(p)) {
                p = restructure(tallerChild(tallerChild(p)));
                computeHeight(left(p));
                computeHeight(right(p));
            }
            computeHeight(p);
            newHeight = height(p);
            p = parent(p);
        } while (oldHeight != newHeight && p != null);
    }

    @Override
    protected void rebalanceInsert(Position<Entry<K, V>> p) {
        rebalance(p);
    }


    @Override
    protected void rebalanceDelete(Position<Entry<K, V>> p) {
        if (parent(p) != null) rebalance(parent(p));
    }

    public void redBlackRecolor() {
        colorBlack(root());
    }

    private void colorChildren(Position<Entry<K, V>> c1, Position<Entry<K, V>> c2) {
        int h1 = height(c1);
        int h2 = height(c2);

        if (h1 < h2 || h1 % 2 == 0) {
            colorBlack(c1);
        } else colorRed(c1);

        if (h1 > h2 || h2 % 2 == 0) {
            colorBlack(c2);
        } else colorRed(c2);
    }

    private void colorRed(Position<Entry<K, V>> p) {
        tree.setColor(p, RED);
        colorChildren(left(p), right(p));
    }

    private void colorBlack(Position<Entry<K, V>> p) {
        tree.setColor(p, BLACK);
        if(p.getElement() != null) colorChildren(left(p), right(p));
    }


    public boolean isValidRedBlack() {
        if (tree.getColor(root()) != BLACK) return false;
        if(!traverse(root())) return  false;
        return computeBlackHeight(root()) != -1;
    }

    private boolean traverse(Position<Entry<K, V>> root) {
        if (root == null) return true;
        if(tree.parent(root) != null) {
            if (tree.getColor(parent(root)) == RED && tree.getColor(root) == RED) return false;
        }
        return traverse(tree.left(root)) && traverse(tree.right(root));
    }

    public int computeBlackHeight(Position<Entry<K, V>> p) {
        if (p.getElement() == null) return 0;

        int left = computeBlackHeight(left(p));
        if(left == -1) return -1;
        int right = computeBlackHeight(right(p));
        if(right == -1) return -1;

        if (left != right) return -1;

        int thisNode = tree.getColor(p) == BLACK ? 1 : 0;
        return left + thisNode;
    }

    @Override
    public String toString() {
        if(root() == null) return "";

        StringBuilder sb = new StringBuilder();
        inOrderAppend(root(), sb);

        return sb.toString();
    }

    private void inOrderAppend(Position<Entry<K, V>> p, StringBuilder sb) {
        sb.append('(')
                .append(p.getElement().getKey())
                .append(',')
                .append(p.getElement().getValue())
                .append(',')
                .append(tree.getColor(p) == BLACK ? "B" : "R")
                .append(") ");

        if(left(p).getElement() != null) inOrderAppend(left(p), sb);
        if(right(p).getElement() != null) inOrderAppend(right(p), sb);
    }
}
