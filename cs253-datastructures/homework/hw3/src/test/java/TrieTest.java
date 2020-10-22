import org.junit.Test;

import static junit.framework.TestCase.*;

public class TrieTest {
    @Test
    public void TrieNotNull() {
        Trie t = new Trie();

        assertNotNull(t);
    }

    @Test
    public void trieInserts() {
        Trie t = new Trie();
        t.insert("hello");
        t.insert("its");
        t.insert("johnny");
        t.insert("italian");

        assertTrue(t.contains("its"));
        assertFalse(t.contains("he"));
        assertFalse(t.contains("johnnys"));

    }

    @Test
    public void dictInserts() {
        String filename = "src/main/resources/words.txt";
        Trie t = new Trie();
        t.insertDictionary(filename);

        assertTrue(t.contains("adolescent"));
    }
}
