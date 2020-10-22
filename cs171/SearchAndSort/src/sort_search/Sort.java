public class Sort {

    public static void main(String[] args) {
        int[] a = {1, 4, 5, 7, 8, 3, 5, 7, 344, 457, 4, 2, 5, 65, 768, 32, 32, 76};
        selectionSort(a);

        StringBuilder stringBuilder = new StringBuilder();
        for (int i : a) stringBuilder.append(i).append(" ");
        System.out.println(stringBuilder.toString());
    }

    /**
     * Takes O(n^2)
     *
     * @param a
     * @return
     */
    public static void bubbleSort(int[] a) {
        for (int i = 0; i < a.length - 1; i++)
            for (int j = 0; j < a.length - i - 1; j++)
                if (a[j] > a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
    }

    /**
     * Runs O(n^2)
     *
     * @param a
     */
    public static void selectionSort(int[] a) {

        for (int i = 0; i < a.length - 1; i++) {
            int i2 = i;
            for (int j = i + 1; j < a.length; j++)
                if (a[j] < a[i2])
                    i2 = j;

            int temp = a[i2];
            a[i2] = a[i];
            a[i] = temp;

        }
    }


    public static void insertionSort(int[] a) {

    }
}
