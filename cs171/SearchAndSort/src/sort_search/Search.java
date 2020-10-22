public class Search {

    public static void main(String[] args) {
        int[] array = {1, 2, 4, 3, 0, 5, -1, 10, 11, 100};
        System.out.println(linearSearch(array, 3));
    }

    /**
     * Takes O(n)
     *
     * @param list An unsorted int array
     * @param key  An integer to search for
     * @return the index at which key is located in list
     */
    public static int linearSearch(int[] list, int key) {
        for (int i = 0; i < list.length; i++)
            if (key == list[i]) return i;
        return -1;
    }

    /**
     * Takes O(ln n)
     *
     * @param list
     * @param key
     * @return
     */
    public static int binarySearch(int[] list, int key) {
        int low = 0;
        int high = list.length - 1;

        while (high >= low) {
            int mid = (low + high) / 2;
            if (key < list[mid]) high = mid - 1;
            if (key > list[mid]) low = mid + 1;
            else return mid;
        }
        return -1;
    }
}
