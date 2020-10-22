from graphviz import Digraph
import string
import random
from itertools import combinations, permutations

if __name__ == '__main__':
    alphabet = list(string.ascii_letters)
    dot = Digraph()

    N = 10
    SCALER = 2

    nodes = random.sample(alphabet, N)
    s = random.sample({"".join(val) for val in combinations(nodes, 2)}, N*SCALER)
    dot.edges(s)

    print(dot.source)
