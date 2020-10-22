import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.concurrent.ThreadLocalRandom;

import static junit.framework.TestCase.assertEquals;

public class QuickSelectTest {

    private static final int ARRAY_SIZE = Constants.ARRAY_SIZE;
    @Test
    public void normalPivotWorks() {
        for(int trial = 0; trial < 500; trial++) {
            ArrayList<Integer> l = new ArrayList<>();
            for (int i = 0; i < ARRAY_SIZE; i++) {
                l.add(ThreadLocalRandom.current().nextInt());
            }
            int k = ThreadLocalRandom.current().nextInt(0, ARRAY_SIZE);
            int i = QuickSelector.quickSelect(l, k, new PivotRule());
            Collections.sort(l);
            int expval = l.get(k);

            assertEquals(expval, i);
        }
    }

    @Test
    public void randomPivotWorks() {
        for(int trial = 0; trial < 500; trial++) {
            ArrayList<Integer> l = new ArrayList<>();
            for (int i = 0; i < ARRAY_SIZE; i++) {
                l.add(ThreadLocalRandom.current().nextInt());
                //l.add(i);
            }
            int k = ThreadLocalRandom.current().nextInt(0, ARRAY_SIZE);
            int i = QuickSelector.quickSelect(l, k, new RandomizedRule());
            Collections.sort(l);
            int expval = l.get(k);

            assertEquals(expval, i);
        }
    }

    @Test
    public void medianOfMedianWorks() {
        for(int trial = 0; trial < 30; trial++) {
            ArrayList<Integer> l = new ArrayList<>();
            for (int i = 0; i < ARRAY_SIZE; i++) {
                l.add(ThreadLocalRandom.current().nextInt());
            }
            int k = ThreadLocalRandom.current().nextInt(1, ARRAY_SIZE);
            int i = QuickSelector.quickSelect(l, k, new MedianOfMediansRule());
            Collections.sort(l);
            int expval = l.get(k);

            assertEquals(expval, i);
        }
    }

    @Test
    public void simpleQuickSelect() {
        ArrayList<Integer> l = new ArrayList<>();
        for(int i =0; i< 5; i++) {
            l.add(i);
        }
        Collections.shuffle(l);
        int i = QuickSelector.quickSelect(l, 2, new PivotRule());
        System.out.println(i);
    }
}
