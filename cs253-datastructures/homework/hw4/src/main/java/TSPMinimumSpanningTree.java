/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. Simon Marty, 2283420
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class TSPMinimumSpanningTree {
    public static ArrayList<Line2D> computeMST(ArrayList<Point2D> points) {
        ArrayList<Line2D> treeEdges = new ArrayList<>();
        int j = 0;
        PriorityQueue<PQEntry<Double, Integer>> pq = new PriorityQueue<>(Map.Entry.comparingByKey());

        do {
            for (int i = 0; i < points.size(); i++) {
                if (i != j)
                    pq.add(new PQEntry<>(points.get(j).distance(points.get(i)), j, i));
            }

            boolean successful = false;

            while (!pq.isEmpty() && !successful) {
                PQEntry<Double, Integer> bestPoint = pq.poll();
                if (!points.get(bestPoint.getValue()).isVisited()) {
                    treeEdges.add(new Line2D(points.get(bestPoint.getOrigin()), points.get((bestPoint.getValue()))));
                    j = bestPoint.getValue();
                    points.get(j).setVisited(true);
                    successful = true;
                }
            }
        } while (!pq.isEmpty());

        for (Point2D p : points) {
            p.setVisited(false);
        }
        return treeEdges;
    }

    public static ArrayList<Line2D> computeDFSTour(ArrayList<Point2D> points, ArrayList<Line2D> mst) {
        HashMap<Point2D, ArrayList<Point2D>> map = new HashMap<>();
        fillMap(map, mst);
        ArrayList<Line2D> tour = new ArrayList<>();
        ArrayList<Point2D> sequence = new ArrayList<>();
        Point2D p = mst.get(0).getP1();
        dfs(p, map, sequence);

        for (int i = 0; i < sequence.size() - 1; i++) {
            tour.add(new Line2D(sequence.get(i), sequence.get(i + 1)));
        }

        tour.add(new Line2D(sequence.get(sequence.size() - 1), sequence.get(0)));

        for (Point2D r : points) {
            r.setVisited(false);
        }
        return tour;
    }

    private static void dfs(Point2D p, HashMap<Point2D, ArrayList<Point2D>> map,
                            ArrayList<Point2D> sequence) {
        if (p == null) {
            return;
        }
        p.setVisited(true);

        sequence.add(p);

        if (map.containsKey(p)) {
            for (Point2D q : map.get(p)) {
                if (!q.isVisited()) {
                    dfs(q, map, sequence);
                }
            }
        }
    }

    private static void fillMap(HashMap<Point2D, ArrayList<Point2D>> map, ArrayList<Line2D> mst) {
        for (Line2D l : mst) {
            if (!map.containsKey(l.getP1())) {
                map.put(l.getP1(), new ArrayList<>());
            }
            ArrayList<Point2D> a = map.get(l.getP1());
            a.add(l.getP2());
            map.put(l.getP1(), a);
        }
    }

    private static class PQEntry<K, V> implements Map.Entry<K, V> {
        private K key;
        private V value;
        private V origin;

        public PQEntry(K key, V origin, V value) {
            this.key = key;
            this.value = value;
            this.origin = origin;
        }

        @Override
        public K getKey() {
            return key;
        }

        @Override
        public V getValue() {
            return value;
        }

        public V getOrigin() {
            return origin;
        }

        @Override
        public V setValue(V v) {
            value = v;
            return value;
        }

        public void setOrigin(V origin) {
            this.origin = origin;
        }
    }
}
