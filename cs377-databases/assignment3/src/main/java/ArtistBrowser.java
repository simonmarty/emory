/* THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
WRITTEN BY OTHER STUDENTS OR COPIED FROM ONLINE RESOURCES.   Simon Marty */

import java.util.ArrayList;
import java.sql.*;
import java.util.Arrays;
import java.util.Collections;

@SuppressWarnings("SqlResolve")
public class ArtistBrowser {

    /* A connection to the database */
    private Connection connection;

    /**
     * Constructor loads JDBC driver. There is no need to modify this.
     */
    public ArtistBrowser() {
        try {
            Class.forName("org.postgresql.Driver");
        } catch (ClassNotFoundException e) {
            System.err.println("Failed to find the JDBC driver.");
        }
    }

    /**
     * Establishes a connection to be used for this session, assigning it to
     * the private instance variable 'connection'.
     *
     * @param url      the url to the database
     * @param username the username to connect to the database
     * @param password the password to connect to the database
     * @return true if the connection is successful, false otherwise
     */
    public boolean connectDB(String url, String username, String password) {
        try {
            this.connection = DriverManager.getConnection(url, username, password);
            return true;
        } catch (SQLException se) {
            System.err.println("SQL Exception. <Message>: " + se.getMessage());
            return false;
        }
    }

    /**
     * Closes the database connection.
     *
     * @return true if the closing was successful, false otherwise.
     */
    public boolean disconnectDB() {
        try {
            this.connection.close();
            return true;
        } catch (SQLException se) {
            System.err.println("SQL Exception. <Message>: " + se.getMessage());
            return false;
        }
    }

    /**
     * Returns a sorted list of the names of all musicians and bands
     * who released at least one album in a given genre.
     * <p>
     * Returns an empty list if no such genre exists or no artist matches.
     * <p>
     * NOTE:
     * Use Collections.sort() to sort the names in ascending
     * alphabetical order.
     * Use prepared statements.
     *
     * @param genre the genre to find artists for
     * @return a sorted list of artist names
     */
    public ArrayList<String> findArtistsInGenre(String genre) {
        try {


            String query = "SELECT DISTINCT name FROM artist " +
                    "JOIN album a on artist.artist_id = a.artist_id " +
                    "join genre g on a.genre_id = g.genre_id " +
                    "where genre = ?";

            PreparedStatement p = connection.prepareStatement(query);
            p.setString(1, genre);

            ResultSet rs = p.executeQuery();
            ArrayList<String> res = new ArrayList<>();
            while (rs.next()) {
                res.add(rs.getString(1));
            }

            Collections.sort(res);

            p.close();
            rs.close();

            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * Returns a sorted list of the names of all collaborators
     * (either as a main artist or guest) for a given artist.
     * <p>
     * Returns an empty list if no such artist exists or the artist
     * has no collaborators.
     * <p>
     * NOTE:
     * Use Collections.sort() to sort the names in ascending
     * alphabetical order.
     * Use prepared statements.
     *
     * @param artist the name of the artist to find collaborators for
     * @return a sorted list of artist names
     */
    public ArrayList<String> findCollaborators(String artist) {

        try {
            String query = "SELECT name from artist " +
                    "where artist_id in ( " +
                    "select artist1 from collaboration where artist2 = ( " +
                    "select artist_id from artist where name = ?) " +
                    "UNION " +
                    "select artist2 from collaboration where artist1 = ( " +
                    "select artist_id from artist where name = ?))";


            PreparedStatement p = connection.prepareStatement(query);

            p.setString(1, artist);
            p.setString(2, artist);

            ResultSet rs = p.executeQuery();

            ArrayList<String> res = new ArrayList<>();


            while (rs.next()) {
                res.add(rs.getString(1));
            }
            Collections.sort(res);
            p.close();
            rs.close();

            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }


    /**
     * Returns a sorted list of the names of all songwriters
     * who wrote songs for a given artist (the given artist is excluded).
     * <p>
     * Returns an empty list if no such artist exists or the artist
     * has no other songwriters other than themself.
     * <p>
     * NOTE:
     * Use Collections.sort() to sort the names in ascending
     * alphabetical order.
     *
     * @param artist the name of the artist to find the songwriters for
     * @return a sorted list of songwriter names
     */
    public ArrayList<String> findSongwriters(String artist) {
        try {
            String query = "select name " +
                    "from song join artist a " +
                    "on song.songwriter_id = a.artist_id " +
                    "where song_id in ( " +
                    "select song_id " +
                    "from belongstoalbum " +
                    "join album a2 on belongstoalbum.album_id = a2.album_id " +
                    "join artist a3 on a2.artist_id = a3.artist_id " +
                    "where a3.name = ?" +
                    ") " +
                    "and a.name != ?";

            PreparedStatement p = connection.prepareStatement(query);
            p.setString(1, artist);
            p.setString(2, artist);

            ResultSet rs = p.executeQuery();

            ArrayList<String> res = new ArrayList<>();

            while (rs.next()) {
                res.add(rs.getString(1));
            }

            Collections.sort(res);
            p.close();
            rs.close();

            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * Returns a sorted list of the names of all common acquaintances
     * for a given pair of artists.
     * <p>
     * Returns an empty list if either of the artists does not exist,
     * or they have no acquaintances.
     * <p>
     * NOTE:
     * Use Collections.sort() to sort the names in ascending
     * alphabetical order.
     *
     * @param artist1 the name of the first artist to find acquaintances for
     * @param artist2 the name of the second artist to find acquaintances for
     * @return a sorted list of artist names
     */
    public ArrayList<String> findCommonAcquaintances(String artist1, String artist2) {
        try {
            String query = "select name " +
					"from artist " +
					"where artist_id in ( " +
						"select artist_id " +
						"from collaboration " +
							"join artist a on collaboration.artist1 = a.artist_id " +
						"where artist2 in ( " +
							"select artist_id " +
							"from artist " +
							"where name = ?) " +
						"INTERSECT " +
						"select artist_id " +
						"from collaboration " +
						"join artist a on collaboration.artist1 = a.artist_id " +
						"where artist2 in ( " +
							"select artist_id " +
							"from artist " +
							"where name = ?))";

            PreparedStatement p = connection.prepareStatement(query);
            p.setString(1, artist1);
            p.setString(2, artist2);
            ResultSet rs = p.executeQuery();

            ArrayList<String> res = new ArrayList<>();

            while (rs.next()) {
                res.add(rs.getString(1));
            }

            Collections.sort(res);
            p.close();
            rs.close();

            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * Returns a sorted list of the names of record labels whose
     * total album sales increased consistently every year, when
     * considering all consecutive years in the dataset that appear
     * for a given label. If a label has a year in the middle with 0
     * revenue (i.e., no produced albums or all albums had 0 sales),
     * it doesn't satisfy the criteria and shouldn't be included here.
     * <p>
     * Returns an empty list if no such labels fit the criteria.
     * <p>
     * NOTE:
     * Use Collections.sort() to sort the names in ascending
     * alphabetical order.
     *
     * @return a sorted list of record label names
     */
    public ArrayList<String> findRisingLabels() {
        try {

            PreparedStatement p;
            p = connection.prepareStatement("DROP VIEW IF EXISTS notgucci");
            p.executeUpdate();
            p = connection.prepareStatement("DROP VIEW IF EXISTS labelsales");
            p.executeUpdate();

            // I ended up going back to using label_id as the identifier of a label
            // with the provided dataset, this does not return anything
            // however, with a dataset where each label has its own unique label_id
            // this should return the correct stuff

            String query = "create view LabelSales as ( " +
                                "select recordlabel.label_id, year, sum(sales) as sales " +
                                "from recordlabel join producedby p on recordlabel.label_id = p.label_id " +
                                "join album a on p.album_id = a.album_id " +
                                "group by recordlabel.label_id, year " +
                                "having sum(sales) != 0)";

            p = connection.prepareStatement(query);
            p.executeUpdate();

            query = "create view notGucci as ( " +
                        "select l1.label_id " +   // Labels that didnt grow $ between two years
                        "from LabelSales l1, LabelSales l2 " +
                        "where l1.label_id = l2.label_id " +
                            "and l1.year > l2.year " +
                            "and l1.sales <= l2.sales " +
                    "UNION " +
                        "select l1.label_id " + // Labels that only made sales for a year
                        "from LabelSales l1 " +
                        "group by label_id, " +
                        "year having count(year) = 1)";

            p = connection.prepareStatement(query);
            p.executeUpdate();

            query = "select label_name " +
                    "from recordlabel " +
                    "where label_id not in ( " +
                        "select label_id " +
                        "from notGucci)";
            p = connection.prepareStatement(query);
            ResultSet rs = p.executeQuery();

            p = connection.prepareStatement("DROP VIEW IF EXISTS notgucci");
            p.executeUpdate();
            p = connection.prepareStatement("DROP VIEW IF EXISTS labelsales");
            p.executeUpdate();

            ArrayList<String> res = new ArrayList<>();

            while (rs.next()) {
                res.add(rs.getString(1));
            }

            Collections.sort(res);
            p.close();
            rs.close();

            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }


    public static void main(String[] args) {

        if (args.length < 2) {
            System.out.println("Usage: java ArtistBrowser <userName> <password>");
            return;
        }

        String user = args[0];
        String pass = args[1];

        ArtistBrowser a3 = new ArtistBrowser();

        String url = "jdbc:postgresql://localhost:5432/postgres?currentSchema=artistDB";
        a3.connectDB(url, user, pass);

        System.err.println("\n----- ArtistsInGenre -----");
        ArrayList<String> res = a3.findArtistsInGenre("Rock");
        for (String s : res) {
            System.err.println(s);
        }

        System.err.println("\n----- Collaborators -----");
        res = a3.findCollaborators("Michael Jackson");
        for (String s : res) {
            System.err.println(s);
        }

        System.err.println("\n----- Songwriters -----");
        res = a3.findSongwriters("Justin Bieber");
        for (String s : res) {
            System.err.println(s);
        }

        System.err.println("\n----- Common Acquaintances -----");
        res = a3.findCommonAcquaintances("Jaden Smith", "Miley Cyrus");
        for (String s : res) {
            System.err.println(s);
        }

        System.err.println("\n----- Rising Record Labels -----");
        res = a3.findRisingLabels();
        for (String s : res) {
            System.err.println(s);
        }

        a3.disconnectDB();
    }
}
