import java.util.ArrayList;

public class Graph {

    private int numVertices;
    private int numEdges;
    private ArrayList<Integer>[] adj;

    @SuppressWarnings("unchecked")
    public Graph(int numVertices) {
        this.numVertices = numVertices;
        adj = (ArrayList<Integer>[]) new ArrayList[numVertices];
        for (int v = 0; v < numVertices; v++) adj[v] = new ArrayList<>();
    }

    public void addEdge(int v, int w) {
        adj[v].add(w);
        adj[w].add(v);
        numEdges++;
    }

    public void addEdge(int[] a, int[] b) {
        if (a.length != b.length) throw new IllegalArgumentException("Arrays are not the same size");
        for (int i = 0; i < a.length; i++) {
            addEdge(a[i], b[i]);
        }
    }

    public int getNumVertices() {
        return numVertices;
    }

    public ArrayList<Integer> getAdj(int v) {
        return adj[v];
    }
}
