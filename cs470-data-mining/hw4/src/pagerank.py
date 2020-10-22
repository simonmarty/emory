import sys

import networkx as nx

DEBUG = True


def pagerank(G, damping=0.85, max_iterations=1000, tolerance=10e-6) -> dict:
    if len(G) == 0:
        return {}

    # A right-stochastic graph is a weighted digraph in which for each node,
    # the sum of the weights of all the out-edges of that node is 1. (From NetworkX documentation)
    stoch = nx.stochastic_graph(G)
    n = stoch.number_of_nodes()

    ranks = dict.fromkeys(stoch, 1.0 / n)
    dead_ends = [node for node in stoch if stoch.out_degree(node) == 0.0]

    for _ in range(max_iterations):
        previous_x = ranks
        ranks = dict.fromkeys(previous_x.keys(), 0)
        dead_end_sum = damping*sum(previous_x[node] for node in dead_ends)
        for node in ranks:
            for outgoing_node in stoch[node]:
                ranks[outgoing_node] += damping * previous_x[node] * stoch[node][outgoing_node]['weight']
            ranks[node] += dead_end_sum * (1.0 / n) + (1.0 - damping) * (1.0 / n)

        # Check if the difference is within tolerance
        if sum([abs(ranks[node] - previous_x[node]) for node in ranks]) < n * tolerance:
            return ranks
    raise BaseException


def log(s):
    if DEBUG:
        print(s)


if __name__ == '__main__':
    input_path, output_path = (sys.argv[i] for i in range(1, 3))
    log('Ingesting Graph')
    # Ingest a DOT digraph and convert it to a NetworkX directed graph
    graph = nx.Graph(nx.drawing.nx_pydot.read_dot(input_path)).to_directed()

    output = open(output_path, 'w')
    output.write('vertex,pagerank\n')

    log('Computing PageRank')
    d = pagerank(graph)

    for k, v in d.items():
        output.write(f'{k},{v}\n')
    output.close()

    if DEBUG:
        output = open(f'{output_path}.actual', 'w')
        output.write('vertex,pagerank\n')
        for k, v in nx.pagerank(graph).items():
            output.write(f'{k},{v}\n')
