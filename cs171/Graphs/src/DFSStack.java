import java.util.Stack;

public class DFSStack {

    private boolean[] visited;

    public DFSStack(Graph g, int source) {
        visited = new boolean[g.getNumVertices()];
        Stack<Integer> stack = new Stack<>();
        stack.push(source);
        while (!stack.isEmpty()) {
            int v = stack.pop();
            visited[v] = true;
            System.out.print(v + " ");
            for (int i : g.getAdj(v)) {
                if (!visited[i]) stack.push(i);
            }
        }
    }
}
