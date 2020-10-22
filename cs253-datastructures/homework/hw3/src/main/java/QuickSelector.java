/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.ArrayList;
import java.util.Collections;

class QuickSelector {
    public static Integer quickSelect(ArrayList<Integer> array, int index, PivotRule rule){
        return quickSelect(array, 0, array.size() - 1, index, rule);
    }

    private static int quickSelect(ArrayList<Integer> array, int low, int high, int index, PivotRule rule) {

        int pivot = partition(array, low, high, rule);

        if(index == pivot) {
            return array.get(index);
        }
        else if(index < pivot) {
            return quickSelect(array, low, pivot - 1, index, rule);
        }
        else {
            return quickSelect(array, pivot + 1, high, index, rule);
        }
    }

    private static int partition(ArrayList<Integer> array, int low, int high, PivotRule rule) {
        Collections.swap(array, rule.getPivot(array, low, high), high);
        int pivot = array.get(high);
        int j = low - 1;

        for(int i = low; i < high; i++) {
            if(array.get(i) < pivot) {
                j++;
                Collections.swap(array, i, j);
            }
        }
        Collections.swap(array, j + 1, high);

        return j + 1;
    }

}
