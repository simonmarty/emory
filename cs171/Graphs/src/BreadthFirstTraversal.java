import java.util.ArrayDeque;

public class BreadthFirstTraversal {


    public static void traverse(Graph g, int source) {
        boolean[] visited;
        ArrayDeque<Integer> q;
        visited = new boolean[g.getNumVertices()];
        q = new ArrayDeque<>();

        System.out.print(source + " ");
        visited[source] = true;
        q.add(source);

        while (!q.isEmpty()) {
            int v = q.poll();
            for (int w : g.getAdj(v)) {
                if (!visited[w]) {
                    visited[w] = true;
                    System.out.print(w + " ");
                    q.add(w);
                }
            }
        }
    }

    public static void main(String[] args) {

        Graph g = new Graph(7);
        g.addEdge(0, 1);
        g.addEdge(0, 6);
        g.addEdge(1, 3);
        g.addEdge(1, 5);
        g.addEdge(1, 6);
        g.addEdge(2, 3);
        g.addEdge(2, 5);
        g.addEdge(2, 6);
        g.addEdge(3, 4);
        g.addEdge(4, 5);

        System.out.println(g);

        traverse(g, 0);
    }
}
