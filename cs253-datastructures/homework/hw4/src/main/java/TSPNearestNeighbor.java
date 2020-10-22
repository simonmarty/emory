/*
THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. Simon Marty, 2283420
*/

import java.util.ArrayList;

public class TSPNearestNeighbor {
    public static ArrayList<Line2D> computeNearestNeighbor(ArrayList<Point2D> points) {
        ArrayList<Line2D> tour = new ArrayList<>();
        points.get(0).setVisited(true);

        int current = 0;
        int next = 0;

        for(int j = 0; j < points.size(); j++) {
            double min = Double.MAX_VALUE;
            for (int i = 0; i < points.size(); i++) {
                if (i != current && !points.get(i).isVisited() ) {
                    double dist = points.get(current).distance(points.get(i));
                    if(dist < min) {
                        min = dist;
                        next = i;
                    }
                }
            }
            points.get(next).setVisited(true);
            tour.add(new Line2D(points.get(current), points.get(next)));
            current = next;
        }
        tour.add(new Line2D(points.get(current), points.get(0)));

        // RESET
        for(Point2D p : points) {
            p.setVisited(false);
        }
        return tour;
    }
}
