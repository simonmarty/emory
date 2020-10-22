import java.sql.*;

public class jdbctest {
    public static void main(String[] args) {
        try {
            Class.forName("org.postgresql.Driver"); // Loads to mem
            Connection c = DriverManager.getConnection("jdbc:postgresql://localhost:5432/postgres?" +
                            "currentSchema=public",
                    "postgres", "12345678");
            Statement stmt = c.createStatement();
            ResultSet r = stmt.executeQuery("SELECT name, number FROM mytable WHERE  number < 2");

            while(r.next()) {
                System.out.println(r.getString("name") + "(" + r.getInt("number") + ")");
            }
            stmt.close();
            PreparedStatement execStat = c.prepareStatement("SELECT netWorth FROM MovieExec");
            r = execStat.executeQuery();

            System.out.println(r.getString("netWorth"));

            execStat.close();

            PreparedStatement studioStat = c.prepareStatement("INSERT INTO Studio(name, address) VALUES(?,?)");
            String studioName = "Buena Vista";
            String studioAddr = "LA";

            studioStat.setString(1, studioName);
            studioStat.setString(2, studioAddr);
            studioStat.executeUpdate();


            studioStat.close();
            r.close();
            c.close();



        } catch(SQLException e) {
            System.err.println(e);
            System.err.println(e.getSQLState());
        } catch(ClassNotFoundException e) {
            System.err.println(e);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
