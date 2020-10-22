/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. [Simon Marty, 2283420]
*/

import java.util.ArrayList;
import java.util.HashMap;

public class BipartiteGraph {
    // to get the edges incident with a vertex v, just call adjacencyMap.get(v)
    private HashMap<Vertex, ArrayList<Edge>> adjacencyMap;
    private ArrayList<Vertex> leftVertices;
    private ArrayList<Vertex> rightVertices;

    public BipartiteGraph(int nLeft, int nRight, ArrayList<int[]> edges) {
        leftVertices = new ArrayList<>();
        rightVertices = new ArrayList<>();
        adjacencyMap = new HashMap<>();
        for (int i = 0; i < nLeft; i++){
            Vertex v = new Vertex(i, true);
            leftVertices.add(v);
            adjacencyMap.put(v, new ArrayList<Edge>());
        }
        for (int i = 0; i < nRight; i++){
            Vertex v = new Vertex(i, false);
            rightVertices.add(v);
            adjacencyMap.put(v, new ArrayList<Edge>());
        }
        for (int[] edge : edges){
            Vertex u = leftVertices.get(edge[0]);
            Vertex v = rightVertices.get(edge[1]);
            Edge e = new Edge(leftVertices.get(edge[0]), rightVertices.get(edge[1]));
            adjacencyMap.get(u).add(e);
            adjacencyMap.get(v).add(e);
        }
    }
    public ArrayList<Vertex> getVertices(){
        ArrayList<Vertex> verts = new ArrayList<>();
        for (Vertex v : leftVertices)
            verts.add(v);
        for (Vertex v : rightVertices)
            verts.add(v);
        return verts;
    }
    public ArrayList<Edge> getEdges(){
        ArrayList<Edge> edgeList = new ArrayList<>();
        for (Vertex v : leftVertices){
            for (Edge e : adjacencyMap.get(v)){
                edgeList.add(e);
            }
        }
        return edgeList;
    }
    public boolean augmentFlow(ArrayList<Edge> augmentingPath){


        if (augmentingPath == null || augmentingPath.size() == 0){
            return false;
        }
        for (int i = 0; i < augmentingPath.size(); i++){
            if ((i%2==0) == augmentingPath.get(i).isInMatching()){
				// just a sanity check to make sure it alternates blue/red
                return false;
            }
        }
        //as long as the order of the edges is correct, augmenting a flow
        //can be done in this way
        for (int i = 0; i < augmentingPath.size(); i++) {
            augmentingPath.get(i).setInMatching(i % 2 == 0);
        }
        return true;
    }

    private int previousFlow = 0;

    public ArrayList<Edge> findAugmentingPath() {
        ArrayList<Edge> path = new ArrayList<>();

        int currentFlow = previousFlow;
        for (Vertex v : getVertices()) {
            for (Edge e : adjacencyMap.get(v)) {
                if (!e.isInMatching() && !isMatched(e.getTail()) && !isMatched(e.getHead())) {
                    path.add(e);
                    if (++currentFlow > previousFlow) {
                        previousFlow = currentFlow;
                        return path;
                    }
                }
            }
        }

        for (Vertex v : getVertices()) {
            if (!isMatched(v)) {
                path = new ArrayList<>();
                dfs(v, false, path);
                if (path.size() > previousFlow) {
                    return path;
                }
            }
        }

        return null;
    }

    private boolean isMatched(Vertex v) {
        for (Edge e : adjacencyMap.get(v)) {
            if (e.isInMatching()) {
                return true;
            }
        }
        return false;
    }

    private void dfs(Vertex head, boolean lookingForMatched, ArrayList<Edge> path) {
        for (Edge e : adjacencyMap.get(head)) {
            if (isMatched(e.opposite(head))) {
                if (e.isInMatching() && lookingForMatched) {
                    path.add(e);
                    dfs(e.opposite(head), false, path);
                } else if (!e.isInMatching() && !lookingForMatched) {
                    path.add(e);
                    dfs(e.opposite(head), true, path);
                }
            } else {
                path.add(e);
                return;
            }
        }
    }

}
