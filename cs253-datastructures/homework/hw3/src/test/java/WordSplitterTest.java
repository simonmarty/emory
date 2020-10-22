import org.junit.Test;

public class WordSplitterTest {
    @Test
    public void wordSplitterDetectsNonSplittable() {
        Trie t = new Trie();
        t.insertDictionary(Constants.DICT_PATH);

        System.out.println(WordSplitter.wordSplitter("helloworldair", t));
    }
}
