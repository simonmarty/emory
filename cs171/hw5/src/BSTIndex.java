// SUBMITTED BY: Simon Marty

public class BSTIndex {

    private Node root;

    public MovieInfo findExact(String key) {
        key = key.toLowerCase();
        return findExact(key, root);
    }

    private MovieInfo findExact(String key, Node n) {
        if (n == null)
            return null;

        int cmp = key.compareTo(n.info.shortName.toLowerCase());
        if (cmp < 0)
            return findExact(key, n.left);
        else if (cmp > 0)
            return findExact(key, n.right);
        else
            return n.info;
    }

    public MovieInfo findPrefix(String prefix) {
        prefix = prefix.substring(0, prefix.length() - 1).toLowerCase(); // trim the asterisk
        return findPrefix(prefix, root);
    }

    private MovieInfo findPrefix(String prefix, Node n) {
        if (n == null)
            return null;

        String s2 = n.info.shortName.toLowerCase();
        if(s2.length() > prefix.length()) s2 = s2.substring(0, prefix.length());
        int cmp = prefix.compareTo(s2);
        if (cmp < 0)
            return findPrefix(prefix, n.left);
        else if (cmp > 0)
            return findPrefix(prefix, n.right);
        else
            return n.info;
    }

    public void insert(MovieInfo data) {
        root = insert(data, root);
    }

    private Node insert(MovieInfo data, Node n) {
        if (n == null)
            return new Node(data);

        int cmp = data.shortName.toLowerCase().compareTo(n.info.shortName.toLowerCase());
        if (cmp < 0) {
            n.left = insert(data, n.left);
        } else if (cmp > 0) {
            n.right = insert(data, n.right);
        } else
            n.info = data;
        return n;
    }

    private class Node {
        private MovieInfo info;
        private Node left;
        private Node right;

        Node(MovieInfo info) {
            this.info = info;
        }
    }
}