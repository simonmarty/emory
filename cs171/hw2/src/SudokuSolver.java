// SUBMITTED BY: Simon Marty

import java.awt.*;
import java.util.Stack;

public class SudokuSolver {
// non-recursive, stack-based, backtracking solver of sudoku puzzles

    private int size;
    private int boxSideLength;
    private int[][] grid;

    public SudokuSolver(int[][] grid) {
        size = grid.length;
        if (size % 3 == 0) {
            boxSideLength = size / 3;
        } else throw new RuntimeException("You did not enter a sudoku puzzle of valid size");
        this.grid = new int[size][size];
        System.arraycopy(grid, 0, this.grid, 0, size);
    }

    public static void main(String[] args) {

        int[][] solvableGrid = {{0, 3, 9, 0, 0, 0, 7, 0, 0},
                {0, 0, 0, 7, 0, 0, 1, 0, 0},
                {6, 0, 0, 0, 8, 0, 0, 0, 4},
                {8, 0, 4, 0, 0, 7, 0, 0, 6},
                {0, 0, 0, 8, 0, 0, 4, 0, 0},
                {0, 5, 0, 2, 0, 6, 8, 1, 0},
                {0, 0, 0, 0, 0, 0, 0, 7, 0},
                {5, 8, 0, 0, 0, 3, 9, 4, 0},
                {7, 2, 3, 4, 0, 8, 6, 0, 0}};

        int[][] unsolvableGrid = {{3, 1, 6, 5, 7, 8, 4, 2, 0},
                {5, 2, 0, 0, 0, 0, 0, 0, 0},
                {0, 8, 7, 0, 0, 0, 0, 3, 1},
                {0, 0, 3, 0, 1, 0, 0, 8, 0},
                {9, 0, 0, 8, 6, 3, 0, 0, 5},
                {0, 5, 0, 0, 9, 0, 6, 0, 0},
                {1, 3, 0, 0, 0, 0, 2, 5, 0},
                {0, 0, 0, 0, 0, 0, 0, 7, 4},
                {0, 0, 5, 2, 0, 6, 3, 0, 0}};

        System.out.println("Testing solvable puzzle...\n");
        SudokuSolver sudokuSolver = new SudokuSolver(solvableGrid);
        if (sudokuSolver.solve())
            sudokuSolver.printGrid();
        else {
            System.out.println("No solution exists");
        }

        System.out.println("=================\n");

        System.out.println("Testing unsolvable puzzle...\n");
        sudokuSolver = new SudokuSolver(unsolvableGrid);
        if (sudokuSolver.solve())
            sudokuSolver.printGrid();
        else {
            System.out.println("No solution exists");
        }
    }

    private boolean isInRow(int num, int row) {
        for (int i = 0; i < size; i++) {
            if (num == this.grid[row][i]) return true;
        }
        return false;
    }

    private boolean isInCol(int num, int col) {
        for (int i = 0; i < size; i++) {
            if (num == this.grid[i][col]) return true;
        }
        return false;
    }

    private boolean isInBox(int row, int col, int num) {
        row -= row % boxSideLength;
        col -= col % boxSideLength;

        for (int i = row; i < row + boxSideLength; i++) {
            for (int j = col; j < col + boxSideLength; j++) {
                if (this.grid[i][j] == num) {
                    return true;
                }
            }
        }
        return false;
    }

    private Point nextBlank() {
        Point point = new Point(0, 0);

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (this.grid[i][j] == 0) {
                    point.setLocation(i, j);
                    return point;
                }
            }
        }
        return null;
    }

    private boolean safeToPutNumInPos(int num, int row, int col) {
        return !isInBox(row, col, num) && !isInCol(num, col) && !isInRow(num, row);
    }


    public boolean solve() {
        Point index = new Point(0, 0);
        Stack<Point> points = new Stack<>();
        int lastNumInSpot = 0;
        boolean successful = true;

        while (nextBlank() != null) {

            for (int i = 1; i <= size; i++) {
                assert index != null;
                if (i > lastNumInSpot && safeToPutNumInPos(i, index.x, index.y)) {
                    this.grid[index.x][index.y] = i;
                    successful = true;
                    points.push(index);
                    index = nextBlank();
                    lastNumInSpot = 0;
                    break;
                }
                successful = false;
            }
            if (!successful && points.isEmpty()) break;

            if (!successful) {
                this.grid[index.x][index.y] = 0;
                index = points.pop();
                lastNumInSpot = this.grid[index.x][index.y];
                this.grid[index.x][index.y] = 0;
            }

        }

        return nextBlank() == null;
    }

    public void printGrid() {
        // Prints this.grid - needed in main(), also useful for debugging...
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++)
                System.out.print(this.grid[row][col] + " ");
            System.out.println();
        }
        System.out.println();
    }
}

