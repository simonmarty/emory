import sys
import time

import numpy as np
import pandas as pd


class KMeans:
    def __init__(self, n_clusters):
        """

        :param n_clusters: Number of clusters to create
        """
        self.n_clusters = n_clusters
        self.classes = {}
        self.result = []
        self.centroids = {}

    @staticmethod
    def euclidean_dist(l1, l2):
        return np.sqrt(sum([(l1[i] - l2[i]) ** 2 for i in range(len(l1))]))

    def fit(self, dataset):
        # Select centroids
        self.centroids = {i: v for i, v in enumerate(dataset.sample(self.n_clusters).values)}
        dataset = dataset.values

        # Maximum number of iterations
        for i in range(5000):
            self.classes = {i: [] for i in range(self.n_clusters)}
            self.result = []
            for i, row in enumerate(dataset):
                distances = [self.euclidean_dist(row, self.centroids[centroid]) for centroid in self.centroids]
                # Closest centroid -> cluster member
                classification = distances.index(min(distances))
                self.classes[classification].append(row)
                self.result.append(classification)

            previous = self.centroids.copy()

            for classification in self.classes:
                # Update centroids to cluster means
                self.centroids[classification] = np.mean(self.classes[classification], axis=0)

            done = True
            # Check if centroids have moved
            for centroid in self.centroids:
                if sum(self.centroids[centroid] - previous[centroid]) != 0:
                    done = False

            if done:
                break

    def silhouette_coefficient(self, dataset):
        res = []
        for i, row in enumerate(dataset.values):
            cluster_in = self.result[i]
            cluster_out = {i for i in self.classes if i != cluster_in}

            datapoints_in = self.classes[cluster_in]
            datapoints_out = [self.classes[out] for out in cluster_out]

            sum_in = sum(
                [self.euclidean_dist(row, point) for point in datapoints_in if not np.array_equal(row, point)]) / (
                             len(datapoints_in) - 1)
            sum_out = min({np.mean([self.euclidean_dist(row, point) for point in entry]) for entry in datapoints_out})

            res.append((sum_out - sum_in) / max(sum_out, sum_in))
        return np.mean(res)

    def sse(self, dataset):
        # calculated like in the textbook
        return sum(
            [self.euclidean_dist(row, self.centroids[self.result[i]]) ** 2 for i, row in enumerate(dataset.values)])


if __name__ == '__main__':
    print("Reading Input...")
    _k, _in_file_path, _out_file_path = (sys.argv[i] for i in range(1, 4))
    _k = int(_k)

    _in_file = open(_in_file_path, 'r')

    _file_data = [i.split(',') for i in _in_file]
    _dataset = pd.DataFrame([[float(j) for j in i[:-1]] for i in _file_data if i[:-1]])

    print("Computing KMeans")

    start_time = time.time()

    km = KMeans(_k)
    km.fit(_dataset)
    _result = km.result

    print(f"--- Took {int(time.time() - start_time)} seconds ---")

    print("Writing to Output...")
    out_file = open(_out_file_path, 'w')
    for row in _result:
        out_file.write(f'{row}\n')

    out_file.write(f'silhouette: {km.silhouette_coefficient(_dataset)}\tSSE: '
                   f'{km.sse(_dataset)}\n')
    out_file.close()
    print("Done!")
