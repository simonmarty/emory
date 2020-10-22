import java.io.IOException;
import java.sql.*;
import java.util.Scanner;

class Canvas {

    public static void main(String args[]) throws IOException, SQLException {
        String url;
        Connection conn;
        PreparedStatement pStatement;
        ResultSet rs;
        String queryString;

        try {
            Class.forName("org.postgresql.Driver");
        }
        catch (ClassNotFoundException e) {
            throw new SQLException("Failed to connect to the JDBC driver");
        }
        try
        {
            // This program connects to the database "postgres",
            // with user name "postgres" and password "postgres" (very creative, eh?)

            // Establish our own connection to the database.
            // Replace "localhost" with the IP of your SQL instance (if you're using a remote instance).
            // Replace the first "postgres" string with your user name and the second "postgres" with your password.
            url = "jdbc:postgresql://database-1.clejnkpfq81h.us-east-1.rds.amazonaws.com:5432/postgres?currentSchema=university";
            conn = DriverManager.getConnection(url, "postgres", "12345678");

            // Q1. How many columns are in table student?
            // TODO: Add your code here ...
            queryString = "SELECT * FROM student LIMIT 1";
            pStatement = conn.prepareStatement(queryString);
            rs = pStatement.executeQuery();
            System.out.println("Column count in table student: " + rs.getMetaData().getColumnCount());


            // Q2. Print the max, min, and average cgpa of students in this university
            // TODO: Add your code here ...

            queryString = "SELECT min(cgpa), max(cgpa), avg(cgpa) FROM student";
            pStatement = conn.prepareStatement(queryString);
            rs = pStatement.executeQuery();

            while (rs.next()) {
                System.out.println(rs.getObject(1) + " " + rs.getObject(2)
                + " " + rs.getObject(3));
            }


            // Q3. Read a campus name from the user and print all students who
            // are registered in this campus:
            String campus = "";
            // How-to read input from console:
            //    System.out.println("Enter campus name: ");
            //    Scanner input = new Scanner(System.in);
            //    String campus = input.nextLine();

            // TODO: Add your code here ...
            Scanner scan = new Scanner(System.in);
            campus = scan.next();

            queryString = "SELECT sid FROM student WHERE campus = ?";
            pStatement = conn.prepareStatement(queryString);
            pStatement.setString(1, campus);

            while (rs.next()) {
                System.out.println("\nResult = " + rs.getObject(1));
            }

            // Q4. Now, for fun, let's inject some evil SQL...
            // TODO: Add your code here ...



        }
        catch (SQLException se)
        {
            System.err.println("SQL Exception." +
                    "<Message>: " + se.getMessage());
        }

    }

}
