public class DepthFirstTraversal {

    private boolean[] visited;

    public DepthFirstTraversal(Graph g, int source) {
        visited = new boolean[g.getNumVertices()];
        dfs(g, source);
    }

    private void dfs(Graph g, int v) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int i : g.getAdj(v)) {
            if (!visited[i])
                dfs(g, i);
        }
    }
}
