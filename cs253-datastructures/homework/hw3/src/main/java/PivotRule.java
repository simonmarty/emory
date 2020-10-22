/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

class PivotRule {
    public Integer getPivot(ArrayList<Integer> array, int low, int high) {
        return high;
    }
}

class RandomizedRule extends PivotRule {
    @Override
    public Integer getPivot(ArrayList<Integer> array, int low, int high) {
        return ThreadLocalRandom.current().nextInt(low, high + 1);
    }
}

class MedianOfMediansRule extends PivotRule {
    @Override
    public Integer getPivot(ArrayList<Integer> array, int low, int high) {
        if (high - low < 5) {
            return sort5(array, low, high);
        }

        for (int i = low; i <= high; i += 5) {
            int j = i + 4;  // Right bound of subarray
            if (j > high) {
                j = high;
            }

            int median = sort5(array, i, j);
            Collections.swap(array, median, low + (i - low) / 5);
        }
        return (high - low) / 10 + low + 1;
    }

    /**
     * Computes the median of an array of size 5
     * @param low lower bound of array, inclusive
     * @param high upper bound of array, inclusive
     * @return index of median
     */
    private int sort5(ArrayList<Integer> array, int low, int high) {
        Collections.sort(array.subList(low, high + 1));
        return (high - low) / 2;
    }
}
