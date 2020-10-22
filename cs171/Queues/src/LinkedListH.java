import java.util.Iterator;

public class LinkedListH<Item> implements Iterable<Item> {

    private Node first;
    private Node last;
    private int size = 0;

    public static void main(String[] args) {
        String s;
        LinkedListH<String> list = new LinkedListH<String>();

        list.addFirst("a");
        System.out.println(list);
        list.addFirst("b");
        System.out.println(list);
        list.addFirst("c");
        System.out.println(list);
        list.addFirst("d");
        System.out.println(list);

        System.out.println("contains c? " + list.contains("b"));

        s = list.removeFirst();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeFirst();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeFirst();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeFirst();
        System.out.println("removed " + s + ";   " + list);

        list.addLast("a");
        System.out.println(list);
        list.addLast("b");
        System.out.println(list);
        list.addLast("c");
        System.out.println(list);
        list.addLast("d");
        System.out.println(list);

        System.out.println("contains c? " + list.contains("b"));

        s = list.removeLast();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeLast();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeLast();
        System.out.println("removed " + s + ";   " + list);
        s = list.removeLast();
        System.out.println("removed " + s + ";   " + list);
    }

    public boolean isEmpty() {
        return (first == null);
    }

    public int size() {
        return size;
    }

    public void addFirst(Item item) {
        Node node = new Node();
        node.item = item;

        if (isEmpty()) {
            last = node;
        } else {
            node.next = first;
            first = node;
            size++;
        }
    }

    public Item removeFirst() {
        if (this.isEmpty()) { // no nodes in list
            return null;
        } else if (first == last) {
            Item item = first.item;
            first = null;
            last = null;
            size--;
            return item;
        } else { // one or more nodes in list
            Item item = first.item;
            first = first.next;
            size--;
            return item;
        }
    }

    public void addLast(Item item) {
        // This method is INEFFICIENT as it requires traversal of the list
        // to get to the node whose next reference is affected.  This can
        // be made much more efficient in a linked list implementation that
        // keeps as an instance variable a reference to the last element
        // of the list.

        Node node = new Node();
        node.item = item;

        if (this.isEmpty()) { // no nodes in list
            first = node;
        } else { // one or more nodes in list
            last.next = node;
        }
        last = node;
        size++;
    }

    public Item removeLast() {
        // This method is INEFFICIENT as it requires traversal of the list
        // to get to the node whose next reference is affected.  This can
        // be made much more efficient in a doubly-linked list implementation
        // where each node keeps a reference to both the next node and
        // the previous node.

        if (this.isEmpty())  // no nodes in list, nothing to return
            return null;
        else if (first.next == null) { // one item in list
            Item item = first.item;
            first = null;
            last = null;
            size--;
            return item;
        } else { // more than one item in list
            Node n = first;
            while (n.next.next != null) {
                n = n.next;
            }
            // n is now parent to last node...
            Item item = n.next.item;
            n.next = null;
            last = n;
            size--;
            return item;
        }
    }

    public boolean contains(Item item) {
        // This method is INEFFICIENT as it requires traversal of the list
        // to find the node in question.  This method can be made more
        // efficient in other types of collections (e.g., binary trees).

        for (Node n = first; n != null; n = n.next) {
            if (n.item.equals(item)) return true;
        }
        return false;
    }

    public Iterator<Item> iterator() {
        return new Iterator<Item>() {
            Node node = first;

            public boolean hasNext() {
                return (node != null);
            }

            public Item next() {
                Item item = node.item;
                node = node.next;
                return item;
            }
        };
    }

    public String toString() {
        String outputStr = "";
        outputStr += "first: " + ((first != null) ? first.item : "-") + "   ";
        outputStr += "size: " + this.size + "   ";
        outputStr += " list: ";
        for (Item i : this) {
            outputStr += i + " ";
        }
        return outputStr;
    }

    private class Node {
        Item item;
        Node next;
    }

}

