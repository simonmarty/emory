// SUBMITTED BY: Bhargav Annigeri, Simon Marty, Alex Welsh

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    private static Network network = new Network();

    public static void main(String[] args) {
        mainMenu();
    }

    public static void mainMenu() {
        Scanner scan;
        boolean terminated = false;
        while (!terminated) {
            scan = new Scanner(System.in);
            System.out.println("=================================");
            System.out.println("Welcome to DevSpace");
            System.out.println("There are currently " + network.getNumUsers() + " users on the network\n");
            System.out.println("Press 1 to login\n" +
                    "Press 2 to create an account\n" +
                    "Press 3 to lookup a user\n" +
                    "Press 4 to find the distance between two users\n" +
                    "Press anything else to quit\n");

            String choice = scan.next();

            switch (choice) {
                case "1":
                    login();
                    break;
                case "2":
                    createUser();
                    break;
                case "3":
                    lookupUser();
                    break;
                case "4":
                    distBtwUsers();
                    break;
                default:
                    terminated = true;
                    scan.close();
                    break;
            }
        }
    }

    private static void createUser() {
        String name;
        String bio;
        ArrayList<String> commits;
        String commitString;
        String username;

        System.out.println("Username:");
        Scanner scan = new Scanner(System.in);
        if (scan.hasNext()) {
            username = scan.nextLine();
        } else throw new IllegalArgumentException("You entered an empty username");
        // if username exists, sends them back to main menu
        if (network.contains(username)) {
            System.out.println("That account already exists. Try a different name.");
            return;
        }

        System.out.println("Name:");
        scan = new Scanner(System.in);
        if (scan.hasNext()) {
            name = scan.nextLine().trim();
        } else throw new IllegalArgumentException("You entered an empty name");

        System.out.println("Enter a bio (leave blank for a default one):");
        bio = scan.nextLine();
        System.out.println("Enter your recent commits, separated by commas (leave blank if none):");
        commitString = scan.nextLine();

        scan = new Scanner(commitString).useDelimiter(",");
        commits = new ArrayList<>();
        while (scan.hasNext()) {
            commits.add(scan.next().trim());
        }
        boolean validPassword = false;
        String password = "";
        while (!validPassword) {
            System.out.println("Enter a password (longer than 7 characters, with one number and no spaces)");
            scan = new Scanner(System.in);
            password = scan.next().trim();
            // the regex checks if the password contains a numeric character
            if (!password.matches(".*\\d+.*") || password.length() < 7) {
                System.out.println("Password does not contain a number or is too short");
            } else validPassword = true;
        }

        network.add(username, name, bio, commits, password);
        System.out.println("\nAccount created\n");
    }

    private static void login() {
        Scanner scan = new Scanner(System.in);
        String username;
        String password;
        System.out.println("Enter your username");
        username = scan.nextLine().trim();
        if (!network.contains(username)) {
            System.out.println("\nYou do not have an account. Please create one first\n");
            return;
        }
        User u = network.getUser(username);

        System.out.println("Enter your password");
        password = scan.next();
        while (password != null && !u.checkPassword(password)) {
            System.out.println("Password incorrect, enter a valid password or press enter to quit.");
            password = scan.next();
        }
        userMenu(u);
    }

    private static void userMenu(User user) {
        String password;
        User u = user;
        Scanner scan = new Scanner(System.in);
        final int LOGOUT = 0;
        final int ADD_FRIEND = 1;
        final int CHANGE_USERNAME = 2;
        final int CHANGE_PASSWORD = 3;
        final int CHANGE_NAME = 4;
        final int CHANGE_BIO = 5;
        final int ADD_COMMIT = 6;
        final int DELETE_FRIEND = 7;
        final int SHOW_FRIENDS = 8;
        final int RESTART = Integer.MAX_VALUE;
        boolean terminated = false;

        while (!terminated) {
            System.out.println("=================================");
            System.out.println("Welcome to your account, " + u.getUsername());

            System.out.println("Press 0 if you want to logout\nPress 1 if you want to add a friend\nPress 2 if you want to change your username" +
                    "\nPress 3 if you want to change your password\nPress 4 if you want to change your displayed name\n" +
                    "Press 5 if you want to change your bio\nPress 6 if you want to add a commit to your profile\n" +
                    "Press 7 if you want to delete a friend\nPress 8 to display all friends\n");
            int choice = RESTART;
            try {
                choice = scan.nextInt();
            } catch (Exception e) {
                System.out.println("You have entered an invalid option.");
                scan = new Scanner(System.in);
            }

            switch (choice) {
                case LOGOUT:
                    terminated = true;
                    break;
                case ADD_FRIEND:
                    System.out.println("Enter the username of the friend you want to add");
                    String friendUsername = scan.next();
                    if (!network.contains(friendUsername)) System.out.println("User does not exist");
                    else {
                        network.befriend(u.getUsername(), friendUsername);
                        System.out.println("Friend added");
                    }
                    break;
                case DELETE_FRIEND:
                    System.out.println("Enter the username of the friend you want to remove");
                    String friendToRemove = scan.next();
                    if (!network.contains(friendToRemove)) System.out.println("User does not exist");
                    else {
                        network.unfriend(u.getUsername(), friendToRemove);
                        System.out.println("Friend removed");
                    }
                    break;
                case CHANGE_USERNAME:
                    System.out.println("Enter your password");
                    password = scan.next();
                    if (!u.checkPassword(password)) {
                        System.out.println("Password incorrect");
                    } else {
                        System.out.println("Enter your new username");
                        String newUsername = scan.next();
                        if (network.contains(newUsername)) {
                            System.out.println("That username is already taken");
                        } else {
                            u.changeUsername(password, newUsername);
                            System.out.println("Username changed to " + newUsername);
                        }
                        password = null;
                        break;
                    }
                case CHANGE_PASSWORD:
                    System.out.println("Enter your old password");
                    String oldPassword = scan.next();
                    if (u.checkPassword(oldPassword)) {
                        System.out.println("Enter your new password");
                        String newPassword = scan.next();
                        u.changePassword(oldPassword, newPassword);
                        System.out.println("Password changed");
                    } else System.out.println("Password incorrect");
                    break;
                case CHANGE_NAME:
                    System.out.println("Enter your password");
                    password = scan.next();
                    if (u.checkPassword(password)) {
                        System.out.println("Enter your new name");
                        String newName = scan.next();
                        u.changeName(password, newName);
                        System.out.println("Name changed to: " + newName);
                    } else System.out.println("Password incorrect");
                    password = null;
                    break;
                case CHANGE_BIO:
                    System.out.println("Enter your password");
                    password = scan.next();
                    if (u.checkPassword(password)) {
                        System.out.println("Enter your new bio");
                        String newBio = scan.next();
                        u.changeBio(password, newBio);
                        System.out.println("Bio changed");
                    } else System.out.println("Password incorrect");
                    password = null;
                    break;
                case ADD_COMMIT:
                    System.out.println("Enter your password");
                    password = scan.next();
                    if (u.checkPassword(password)) {
                        System.out.println("Enter a commit");
                        scan.nextLine();
                        String newCommit = scan.nextLine().trim();
                        u.addCommit(password, newCommit);
                        System.out.println("Commit added: " + newCommit.trim());
                    } else System.out.println("Password incorrect");
                    password = null;
                    break;
                case SHOW_FRIENDS:
                    System.out.print("Your friends are: ");
                    for (String friend : network.getAllFriends(u)) {
                        System.out.print("\"" + friend + "\" ");
                    }
                    System.out.println();
                    break;
                case RESTART : break;
                default:
                    terminated = true;
                    break;
            }
        }
    }

    private static void lookupUser() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the user's username:");
        String username = scan.next();

        User u = network.getUser(username);
        if (u != null) {
            System.out.println(u.toString());
            System.out.println("Friends:");
            for (String s : network.getAllFriends(u)) {
                System.out.println(s);
            }
            System.out.println("Type any letter and press enter to continue");
            scan.next();
        } else System.out.println("User does not exist in the network");
    }

    private static void distBtwUsers() {
        System.out.println("=====================================");
        Scanner scan = new Scanner(System.in);

        try {
            System.out.println("Enter the username of the first user");
            String username1 = scan.next();
            System.out.println("Enter the username of the second user");
            String username2 = scan.next();
            System.out.println( username1 +
                    " is a friend of degree " +
                    network.degreeOfSeparation(username1, username2) +
                    " to " + username2);
        } catch(Exception e) {
            e.printStackTrace();
        }

    }
}
