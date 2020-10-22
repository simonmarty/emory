// SUBMITTED BY: Simon Marty

import java.util.Stack;

// A celebrity at a party is someone that is known by everyone, but knows nobody himself or herself.
// Task: Given a 2d matrix of acquaintances, find the celebrity.

public class Party {

    private int[][] acquaintances;

    private Party(int[][] acquaintances) {
        int numPeople = acquaintances.length;
        this.acquaintances = new int[numPeople][numPeople];
        System.arraycopy(acquaintances, 0, this.acquaintances, 0, numPeople);
    }

    public static void main(String[] args) {

        // if acquaintances[a][b] == 1, then "a knows b"
        // if acquaintances[a][b] == 0, then "a does not know b"

        int[][] acquaintances = {{0, 1, 1, 1},
                {1, 0, 1, 0},
                {0, 0, 0, 0},
                {1, 0, 1, 0}};

        Party party = new Party(acquaintances);
        int celebrity = party.findCelebrity();

        if (celebrity == -1)
            System.out.println("No Celebrity");
        else
            System.out.println("Celebrity ID = " + celebrity);
    }

    private boolean knows(int a, int b) {
        return (this.acquaintances[a][b] == 1);
    }

    private int findCelebrity() {

        Stack<Integer> stack = new Stack<>();
        int numPeople = this.acquaintances.length;

        for (int i = 0; i < numPeople; i++) {
            stack.push(i);
        }

        while (stack.size() > 1) {
            int person1 = stack.pop();
            int person2 = stack.pop();

            if (this.knows(person1, person2)) {
                stack.push(person2);
            } else {
                stack.push(person1);
            }
        }
        int lastPerson = stack.pop();
        for (int i = 0; i < numPeople; i++) {
            if (this.knows(lastPerson, i)) {
                return -1;
            }
        }

        return lastPerson;
    }
}
