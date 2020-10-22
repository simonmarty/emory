import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class IndexTester {

    public static void main(String[] args) throws FileNotFoundException {
        BSTIndex t = new BSTIndex();
        String movies = "D:\\Files\\Documents\\2nd Year Oxford\\CS 171\\cs171\\hw5\\movies.txt";
        String actors = "D:\\Files\\Documents\\2nd Year Oxford\\CS 171\\cs171\\hw5\\actors.txt";
        String file;

        Scanner scan = new Scanner(System.in);
        System.out.println("Enter m to use the movie database\na to use the actor database");
        String choice = scan.next().toLowerCase();

        switch (choice) {
            case "m": {
                file = movies;
                System.out.println("Parsing the movie database");
                break;
            }
            case "a": {
                file = actors;
                System.out.println("Parsing the actors database");
                break;
            }
            default: {
                System.out.println("You entered an invalid choice");
                file = null;
                break;
            }
        }

        if (file == null) {
            scan.close();
            throw new IllegalArgumentException("You entered an invalid choice");
        }

        scan = new Scanner(new FileInputStream(file));
        long start = System.currentTimeMillis();
        int i = 0;

        while (scan.hasNext()) {
            String line = scan.nextLine();
            String[] fields = line.split("\t");
            int id = Integer.parseInt(fields[0].trim());
            String shortName = fields[1].trim();
            String fullName = fields[2].trim();
            MovieInfo info = new MovieInfo(id, shortName, fullName);

            t.insert(info);
            i++;
            if (i % 10000 == 0) System.out.println("Inserted " + i + " records.");

        }
        long end = System.currentTimeMillis();
        System.out.println("Index building complete. Inserted " + i +
                " records. Elapsed time = " + (end - start) / 1000 +
                " seconds.");
        
                scan.close();
        scan = new Scanner(System.in);

        System.out.println("Enter search string, end in a '*' for prefix search." +
                " q to quit");
        while (scan.hasNext()) {
            String search = scan.nextLine().trim();
            if (search.equals("q")) break;
            if (search.indexOf('*') > 0) {
                //call prefix search.
                MovieInfo item = t.findPrefix(search);
                if (item == null) System.out.println("Not Found");
                else System.out.println(item.ID + " " + item.shortName +
                        " " + item.fullName);

            } else {
                //call exact search, modify to return MovieInfo
                MovieInfo item = t.findExact(search);
                if (item == null) System.out.println("Not Found");
                else System.out.println(item.ID + " " + item.shortName +
                        " " + item.fullName);
            }
        }
        scan.close();
    }
}