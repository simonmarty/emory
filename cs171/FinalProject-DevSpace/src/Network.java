// SUBMITTED BY: Bhargav Annigeri, Simon Marty, Alex Welsh

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.ConcurrentLinkedQueue;

public class Network {
    private int numUsers;
    private int numFriendships;

    // This class stores which users are friends with whom. It should not
    // be accessed or edited by the client
    private HashMap<User, HashSet<User>> friendsMap;

    // This map stores the equivalencies between usernames and Users
    private HashMap<String, User> userLookupTable;

    public Network() {
        friendsMap = new HashMap<>();
        userLookupTable = new HashMap<>();
    }

    public void add(String username, String name, String bio, List<String> recentCommits, String password) {
        User u = new User(username, name, bio, recentCommits, password);
        this.add(u);
    }

    private void add(User u) {
        friendsMap.put(u, new HashSet<>());
        userLookupTable.put(u.getUsername(), u);
        numUsers++;
    }

    public boolean contains(String username) {
        return userLookupTable.containsKey(username);
    }

    private boolean contains(User user) {
        return friendsMap.containsKey(user);
    }

    public HashSet<User> getFriends(String username) {
        return getFriends(userLookupTable.get(username));
    }

    private HashSet<User> getFriends(User u) {
        return friendsMap.get(u);
    }

    public void befriend(String u1, String u2) {
        befriend(userLookupTable.get(u1), userLookupTable.get(u2));
    }

    private void befriend(User u, User w) {
        if (this.contains(u) && this.contains(w)) {
            HashSet<User> set = friendsMap.get(u);
            set.add(w);
            friendsMap.replace(u, set);
            set = friendsMap.get(w);
            set.add(u);
            friendsMap.replace(w, set);
            numFriendships++;
        }
    }

    public void unfriend(String u, String w) {
        unfriend(userLookupTable.get(u), userLookupTable.get(w));
    }

    private void unfriend(User u, User w) {
        if (this.contains(u) && this.contains(w)) {
            HashSet<User> set = friendsMap.get(u);
            set.remove(w);
            friendsMap.replace(u, set);
            set = friendsMap.get(w);
            set.remove(u);
            friendsMap.replace(w, set);
            numFriendships--;
        }
    }

    public boolean areFriends(String u, String w) {
        return areFriends(userLookupTable.get(u), userLookupTable.get(w));
    }

    public User getUser(String username) {
        return userLookupTable.get(username);
    }

    private boolean areFriends(User u, User w) {
        if (this.contains(u) && this.contains(w)) {
            return friendsMap.get(u).contains(w);
        }
        return false;
    }

    // convenient method to add multiple users at once
    public void befriend(List<String> a, List<String> b) {
        int n = a.size();
        if (n != b.size())
            throw new IllegalArgumentException("Lists are not the same size");
        for (int i = 0; i < n; i++) {
            befriend(a.get(i), b.get(i));
        }
    }

    public int getNumFriendships() {
        return numFriendships;
    }

    public int getNumUsers() {
        return numUsers;
    }

    public int degreeOfSeparation(String name1, String name2) {
        User u = getUser(name1);
        User w = getUser(name2);
        ArrayList<String> visited = new ArrayList<String>();
        ArrayList<String> userTo = new ArrayList<String>();
        userTo.add(null);
        // userTo is effectively a parallel ArrayList that keeps track of the users in
        // an edge-to tree to each user

        ConcurrentLinkedQueue<User> q = new ConcurrentLinkedQueue<User>();

        visited.add(u.getUsername());
        q.add(u);

        boolean secondUserReached = false;

        while (!q.isEmpty()) { // Repeat until queue is empty:
            User current = q.remove(); // dequeue v from queue
            for (User adjacentUser : getFriends(current)) { // enqueue all unvisited adjacent vertices
                if (!visited.contains(adjacentUser.getUsername())) { // marking them visited as you do so
                    visited.add(adjacentUser.getUsername());
                    userTo.add(current.getUsername());
                    q.add(adjacentUser);
                }
                if (adjacentUser.equals(w)) {
                    secondUserReached = true;
                    break;
                }
            }
            if (secondUserReached) {
                break;
            }
        }

        User currentUser = w;
        int dist = 1;
        int index = visited.indexOf(currentUser.getUsername());
        while (!currentUser.equals(u)) {
            index = visited.indexOf(userTo.get(index));
            currentUser = getUser(userTo.get(index));
            dist++;
        }
        return dist;
    }

    public ArrayList<String> getAllFriends(User u) {
        HashSet<User> set = friendsMap.get(u);
        ArrayList<String> friends = new ArrayList<>();
        for (User w : set) {
            friends.add(w.getName());
        }
        return friends;
    }
}
