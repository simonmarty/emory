import org.junit.Test;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

public class QuickSelectPerfTest {

    public void quickSelectPerf(PivotRule p) {
        long sum = 0;
        for (int size = 10000; size <= 10000000; size*= 10) {
            for(int trial = 0; trial < 30; trial++) {
                ArrayList<Integer> l = new ArrayList<>();

                for (int i = 0; i < size; i++) {
                    l.add(ThreadLocalRandom.current().nextInt());
                }
                int k = ThreadLocalRandom.current().nextInt(0, size);
                // TIMING
                long startTime = System.currentTimeMillis();
                int i = QuickSelector.quickSelect(l, k, p);

                long totalTime = System.currentTimeMillis() - startTime;
                //END TIMING
                sum += totalTime;
            }
            System.out.println("Regular Quick Select | " + size + " | " + (double) sum/30000);
        }
        System.out.println();
    }

    @Test
    public void normalQuickSelectPerf() {
        this.quickSelectPerf(new PivotRule());
    }
    @Test
    public void randomizedQuickSelectPerf() {
        this.quickSelectPerf(new RandomizedRule());
    }
    @Test
    public void medianOfMediansQuickSelectPerf() {
        this.quickSelectPerf(new MedianOfMediansRule());
    }
}
