// SUBMITTED BY: Bhargav Annigeri, Simon Marty, Alex Welsh

import java.util.ArrayList;
import java.util.List;

public class User {
    private String username;
    private String pwHash;
    private String name;
    private String bio;
    private String salt;
    private List<String> recentCommits;

    public User(String username, String name, String bio, List<String> recentCommits, String password) {
        this.username = username;
        this.name = name;
        this.bio = bio;
        this.recentCommits = recentCommits;
        this.salt = new RandomString();
        this.pwHash = this.hash(password);
    }

    private String hash(String password) {
        final int NUM_HASHES = 10;
        String pwHash = SHA256.hash(password + this.salt);
        for(int i = 0; i<NUM_HASHES; i++) {
            pwHash = SHA256.hash(pwHash);
        }

        return pwHash;
    }

    public User(String username, String name, String bio, String password) {
        this(username, name, bio, null, password);
        this.recentCommits = new ArrayList<>();
    }

    public User(String username, String name, String password) {
        this(username, name, null, password);
        this.bio = "Hi! I'm new on DevSpace";
    }

    public void addCommit(String password, String commit) {
        if(this.hash(password).equals(pwHash)) {
            recentCommits.add(commit);
        }
    }

    public void changeUsername(String password, String username) {

        if(this.hash(password).equals(pwHash))
            this.username = username;
    }

    public void changeName(String password, String name) {
        if(this.hash(password).equals(pwHash)) {
            this.name = name;
        }
    }

    public void changePassword(String oldPassword, String newPassword) {
        if(this.hash(oldPassword).equals(pwHash)) {
            this.pwHash = this.hash(newPassword);
        }
    }

    public void changeBio(String password, String newBio) {
        if(this.hash(password).equals(pwHash)) {
            this.bio = newBio;
        }
    }

    public String getName() {
        return name;
    }

    public List<String> getRecentCommits() {
        return recentCommits;
    }

    public String getBio() {
        return bio;
    }

    public String getUsername() {
        return username;
    }

    public String getPwHash() {
        return pwHash;
    }

    public boolean checkPassword(String password) {
        return pwHash.equals(this.hash(password));
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s = new StringBuilder("Name: " + name + "\nBio: " + bio + "\n Recent Commits: \n");
        for(String w : recentCommits)
            s.append("\t").append(w).append("\n");
        return s.toString();
    }
}