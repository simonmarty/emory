import java.util.Scanner;
import java.util.Stack;


public class NQueensSolver {

    private final int boardSize;
    private Stack<Integer> colPositions;
    private int solutionsFound;

    public NQueensSolver(int boardSize) {
        this.boardSize = boardSize;
        colPositions = new Stack<>();
        solutionsFound = 0;
    }

    public static void main(String[] args) {
        System.out.println("Enter board size to solve: ");
        Scanner scanner = new Scanner(System.in);
        int boardSize = scanner.nextInt();
        scanner.close();
        NQueensSolver nQueensSolver = new NQueensSolver(boardSize);
        nQueensSolver.findSolutions();
    }

    private boolean isValid(int currentCol) {
        // returns true if the next queen to be placed can be put in column col
        // without being threatened by any previously placed queens
        // Insert code here...


        for (int i = 0; i < colPositions.size(); i++) {

            if (currentCol > boardSize) return false;

            int q2Col = colPositions.get(i);
            int currentRow = colPositions.size();

            if (q2Col == currentCol) {
                return false;
            }
            if (Math.abs(q2Col - currentCol) == Math.abs(currentRow - i)) {
                return false;
            }
        }
        return true;
    }

    private void printSolution() {
        // prints the board with queens at positions specified by colPositions,
        // taking advantage of the non-stack-like method get() of the java.util.Stack class
        for (int r = 0; r < boardSize; r++) {
            for (int c = 0; c < boardSize; c++) {
                System.out.print(colPositions.get(r) == c ? " Q " : " . ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public void findSolutions() {
        // Insert code here...
        int col = 0;

        while (true) {
            while (!isValid(col) && col < boardSize) {
                col++;
            }
            if (col < boardSize) {
                colPositions.push(col);
                col = 0;
            } else {
                if (colPositions.isEmpty()) {
                    break;
                } else {
                    col = colPositions.pop() + 1; // backtrace
                }
            }

            if (colPositions.size() == boardSize) {
                printSolution();
                col = colPositions.pop() + 1; // backtrace
                solutionsFound++;
            }
        }

        System.out.println("Found " + solutionsFound + " solutions.");
        colPositions = new Stack<>();
        solutionsFound = 0;
    }

}

