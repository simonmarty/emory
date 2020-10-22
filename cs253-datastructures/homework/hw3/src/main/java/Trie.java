/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.io.*;
import java.util.*;

class Trie {
    static class TrieNode {
        private final HashMap<Character, TrieNode> charMap = new HashMap<>();
        void insert(String s){
            if(s.length() == 0) {
                return;
            }
            char first = s.charAt(0);
            if(!charMap.containsKey(first)) {
                charMap.put(first, new TrieNode());
            }
            if(s.length() - 1 > 0) {
                charMap.get(first).insert(s.substring(1));
            }
        }
        boolean contains(String s){
            if(s.length() == 0 && !charMap.containsKey('.')) {
                return false;
            }
            if(s.length() == 0) {
                return true;
            }

            return charMap.containsKey(s.charAt(0)) && charMap.get(s.charAt(0)).contains(s.substring(1));
        }
    }
    private final TrieNode root = new TrieNode();

    public void insert(String s){
        root.insert(s + '.');
    }
    public boolean contains(String s){
        return root.contains(s);
    }

    public void insertDictionary(String filename) {
        File file = new File(filename);
        Scanner scan;
        try {
            scan = new Scanner(file);
            while(scan.hasNext()) {
                this.insert(scan.nextLine());
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }


    }
}
