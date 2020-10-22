package net.datastructures;

import org.junit.Test;

import java.util.concurrent.ThreadLocalRandom;

public class AVLTreeMapTest {

    private static final int ENTRY_COUNT = 50000;
    private static final boolean BLACK = false;
    private static final boolean RED = true;
    private AVLTreeMap<Integer, Integer> tree;

    private AVLTreeMap<Integer, Integer> makeAVLTree() {
        AVLTreeMap<Integer, Integer> tree = new AVLTreeMap<>();
        for (int i = 0; i < ENTRY_COUNT; i++) {
            tree.put(ThreadLocalRandom.current().nextInt(1000), ThreadLocalRandom.current().nextInt(1000));
        }

        return tree;
    }

    @Test
    public void doesAVLTreeMapDelete() {
        tree = makeAVLTree();
        tree.remove(5);
        Integer res = tree.get(5);

        assert res == null;
    }

    @Test
    public void redBlackifiesCorrectly() {
        tree = makeAVLTree();

//        tree.put(3,1);
//        tree.put(2,3);
//
//        tree.put(4,5);
//        tree.put(9,1);
//        tree.put(7,5);
//        tree.put(11,2);
        tree.redBlackRecolor();
//        System.out.println(tree.toString());
        assert tree.isValidRedBlack();
    }

    @Test
    public void ratio() {
        tree = makeAVLTree();
        int height = tree.height(tree.root());
        tree.redBlackRecolor();
        int rbHeight = tree.computeBlackHeight(tree.root());
        assert (double) rbHeight / height == 0.5;
    }

    @Test
    public void detectsValidRedBlack() {
        tree = new AVLTreeMap<>(); // manually made
        tree.put(3,1);
        tree.put(2,3);

        tree.put(4,5);
        tree.put(9,1);
        tree.put(7,5);
        tree.put(11,2);

        Position<Entry<Integer, Integer>> p = tree.root();
        Position<Entry<Integer, Integer>> left = tree.left(p);
        Position<Entry<Integer, Integer>> right = tree.right(p);

        tree.setColor(tree.left(left), RED);
        tree.setColor(tree.right(left), RED);
        tree.setColor(tree.right(right), RED);

        assert tree.isValidRedBlack();
    }

    @Test
    public void detectsBadRedBlack() {
        tree = new AVLTreeMap<>();
        tree.put(3, 1);
        tree.put(2, 3);

        tree.put(4, 5);
        tree.put(9, 1);
        tree.put(7, 5);
        tree.put(11, 2);

        assert !tree.isValidRedBlack();
    }
}
