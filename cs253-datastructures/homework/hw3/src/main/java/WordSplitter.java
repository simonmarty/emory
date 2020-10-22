/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.ArrayList;

@SuppressWarnings("unchecked")
class WordSplitter {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Entered too few arguments");
            return;
        }
        String filename = args[0];
        String word = args[1];

        Trie t = new Trie();
        t.insertDictionary(filename);

        System.out.println(wordSplitter(word, t));
    }

    static String wordSplitter(String s, Trie d) {
        int n = s.length();
        if (n == 0) return "Split Not Found";

        boolean[] table = new boolean[n + 1];
        ArrayList<String>[] start = new ArrayList[n + 1];
        table[0] = true;

        for (int i = 0; i < n; i++) {
            if (table[i]) {
                for (int j = i + 1; j <= n; j++) {
                    if (d.contains(s.substring(i, j))) {
                        table[j] = true;
                        if (start[i] == null) start[i] = new ArrayList<>();
                        start[i].add(s.substring(i, j));
                    }
                }
            }
        }

        if (!table[n]) {
            return "Split Not Found";
        }
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (ArrayList<String> a : start) {
            if (count == s.length()) break;
            if (a != null) {
                sb.append(a.get(a.size() - 1)).append(" ");
                count += a.get(a.size() - 1).length();
            }
        }
        return sb.toString();
    }
}
