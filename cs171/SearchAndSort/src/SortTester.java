import java.util.Arrays;

public class SortTester {

    private final static int INSERTION = 0;
    private final static int SELECTION = 1;
    private final static int MERGE = 2;
    private final static int MERGE_NR = 3;
    private final static int QUICK = 4;

    private final static int NUM_TRIALS = 100;
    private final static int MIN_LOG_SIZE = 2;
    private final static int MAX_LOG_SIZE = 14;

    private static Double[] randomArrayOfDoubles(int n) {
        Double[] a = new Double[n];
        for (int i = 0; i < n; i++)
            a[i] = Math.random();
        return a;
    }

    private static boolean sortingIsCorrect(Double[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i] > a[i + 1]) return false;
        }
        return true;
    }

    public static void main(String[] args) {

        double times[][] = new double[MAX_LOG_SIZE - MIN_LOG_SIZE + 1][5];

        for (int p = 0; p < MAX_LOG_SIZE - MIN_LOG_SIZE; p++) {

            int arraySize = (int) (Math.pow(2, p + MIN_LOG_SIZE));

            for (int i = 0; i < NUM_TRIALS; i++) {

                Double[] a = randomArrayOfDoubles(arraySize);

                Sorter<Double> sorter;
                for (int j = 2; j < 5; j++) {

                    switch (j) {
                        case INSERTION:
                            sorter = new InsertionSorter<Double>();
                            break;
                        case SELECTION:
                            sorter = new SelectionSorter<Double>();
                            break;
                        case MERGE:
                            sorter = new MergeSorter<Double>();
                            break;
                        case MERGE_NR:
                            sorter = new MergeSorterNR<Double>();
                            break;
                        case QUICK:
                            sorter = new QuickSorter<Double>();
                            break;
                        default:
                            sorter = null;
                    }

                    Double[] aCopy = Arrays.copyOf(a, a.length);

                    Stopwatch stopwatch = new Stopwatch();
                    sorter.sort(aCopy);
                    times[p][j] += stopwatch.elapsedTime();

                    if (!sortingIsCorrect(aCopy))
                        throw new RuntimeException("sorting incorrect");
                }
            }
        }

        System.out.println("Size \tIns \tSel \tMrg \tMrgNR \tQuick");
        for (int p = 0; p < MAX_LOG_SIZE - MIN_LOG_SIZE; p++) {
            System.out.printf("%d\t", (int) Math.pow(2, p + MIN_LOG_SIZE));
            System.out.printf("%.3f\t", times[p][INSERTION]);
            System.out.printf("%.3f\t", times[p][SELECTION]);
            System.out.printf("%.3f\t", times[p][MERGE]);
            System.out.printf("%.3f\t", times[p][MERGE_NR]);
            System.out.printf("%.3f\t", times[p][QUICK]);
            System.out.println();
        }
    }
}

