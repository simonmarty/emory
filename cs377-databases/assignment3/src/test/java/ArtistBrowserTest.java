import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.*;

public class ArtistBrowserTest {
    private ArtistBrowser artistBrowser;
    private static final String POSTGRES_USERNAME = "postgres";
    private static final String POSTGRES_PASSWORD = "Ellesmere1!";
    private static final String IP = "martyhome.ga";
    private static final String PORT = "5432";

    public void setUp() {
        artistBrowser = new ArtistBrowser();
        String url = "jdbc:postgresql://" + IP + ":" + PORT + "/postgres?currentSchema=artistDB";
        artistBrowser.connectDB(url, POSTGRES_USERNAME, POSTGRES_PASSWORD);
    }

    @Test
    public void testJUnit() {
        String str = "Junit is working fine";
        assertEquals("Junit is working fine", str);
    }

    @Test
    public void successfullyConnectedToDatabase() {
        if (artistBrowser == null) setUp();
        assert artistBrowser != null;
    }

    @Test
    public void findArtistsInGenreReturnsEmpty() {
        if (artistBrowser == null) setUp();
        ArrayList<String> ar = artistBrowser.findArtistsInGenre("wefwfew");
        assertNotNull("Got null result", ar);
        assertEquals("Expected empty collection, got collection of size " + ar.size(), 0, ar.size());
    }

    @Test
    public void findArtistsInGenreReturnsSomething() {
        if (artistBrowser == null) setUp();
        ArrayList<String> ar = artistBrowser.findArtistsInGenre("Rock");
        assertNotNull("Got null result", ar);
        assertTrue("Return count was less than expected", ar.size() > 0);
    }

    @Test
    public void findCollaboratorsReturnsCorrect() {
        if (artistBrowser == null) setUp();
        ArrayList<String> ar = artistBrowser.findCollaborators("Michael Jackson");
        assertArrayEquals(ar.toArray(), new String[]{"Akon", "Paul McCartney"});
    }

    @Test
    public void findSongwritersReturnsCorrect() {
        if (artistBrowser == null) setUp();
        ArrayList<String> ar = artistBrowser.findSongwriters("Justin Bieber");
        assertArrayEquals(ar.toArray(), new String[]{"Akon", "Don Henley"});
    }

    @Test
    public void findCommonAquaintancesReturnsCorrect() {
        if (artistBrowser == null) setUp();
        ArrayList<String> ar = artistBrowser.findCommonAcquaintances("Jaden Smith", "Miley Cyrus");
        assertArrayEquals(ar.toArray(), new String[]{"Justin Bieber"});
    }
}
