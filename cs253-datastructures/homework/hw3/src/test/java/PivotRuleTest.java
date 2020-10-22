import org.junit.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.concurrent.ThreadLocalRandom;

import static junit.framework.TestCase.*;

public class PivotRuleTest {
    private static final int ARRAY_SIZE = Constants.ARRAY_SIZE;

    @Test
    public void isMedianOfMediansCorrect() {
        ArrayList<Integer> l = new ArrayList<>(), sortedList = new ArrayList<>();

        for(int i = 0; i < ARRAY_SIZE; i++) {
            int j = ThreadLocalRandom.current().nextInt(4000);
            l.add(j);
            sortedList.add(j);
        }

        Collections.sort(sortedList);
        PivotRule p = new MedianOfMediansRule();

        int computedMedian = p.getPivot(l,0, l.size() - 1);
        int expectedMedian;
//        if(ARRAY_SIZE % 2 == 0 ) {
//            median2 = (sortedList.get(ARRAY_SIZE / 2) + sortedList.get(ARRAY_SIZE / 2 + 1)) / 2;
//        }
//        else {
            expectedMedian = sortedList.get(ARRAY_SIZE / 2);
//        }

        assertTrue(Math.abs(expectedMedian - computedMedian) < sortedList.get(sortedList.size() - 1) / 2);
    }
}
