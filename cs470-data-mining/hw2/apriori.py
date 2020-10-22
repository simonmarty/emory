# Apriori.py -- Simon Marty

import sys
import time
from itertools import combinations
from typing import Set, Tuple, Dict, List, Any


def prune(frequency_map: Dict[Tuple[int], int], min_support: int, prune_set: Set[Tuple[int]]) -> None:
    """
    Removes all itemsets with support count lower than min_support
    :param prune_set: Set to pruned out tuples
    :param frequency_map: a dictionary that maps itemsets to support counts
    :param min_support: minimum support count
    """
    for k, v in frequency_map.items():
        if v < min_support:
            prune_set.add(k)

    for k in prune_set:
        if k in frequency_map.keys():
            del frequency_map[k]


def get_supports(dataset: List[Tuple[Any]], candidate_set: Set[Tuple[int, Any]],
                 min_support: int, prune_set: Set[Tuple[int]], k: int) -> Dict[Tuple[int], int]:
    """
    Calculates the support count for each tuple in candidate_set
    :param dataset: List of transactions
    :param candidate_set: Set of tuples (itemsets)
    :param min_support: minimum support count
    :param prune_set: set of pruned (non-frequent) itemsets
    :param k: size of the current itemsets
    :return: A dictionary that maps frequent itemsets to their dictionary
    """
    d = {i: 0 for i in candidate_set}
    for line in dataset:
        subsets = list(combinations(line, k))
        for subset in subsets:
            if subset in d:
                d[subset] = d.get(subset, 0) + 1

    prune(frequency_map=d, min_support=min_support, prune_set=prune_set)
    return d


def has_infrequent_subset(itemset: Tuple[int, Any], prune_set: Set[Tuple[int]]):
    """
    :type itemset: itemset
    :param prune_set: Set of non-frequent itemsets
    :return: True if itemset has a subset that is not frequent
    """
    for subset in combinations(itemset, len(itemset) - 1):
        if subset in prune_set:
            prune_set.add(itemset)
            return True
    return False


def join_candidates(previous_itemsets: Set[Tuple[int]], prune_set: Set[Tuple[int]]) -> Set[Tuple[int, Any]]:
    """
    Joins candidates of size k to generate candidates of size (k + 1)
    :param previous_itemsets: The previous set of itemsets
    :param prune_set: Set of non-frequent itemsets
    :return: The set of valid candidates
    """
    res = set()
    for candidate_1 in previous_itemsets:
        for candidate_2 in previous_itemsets:
            if candidate_1[:-1] == candidate_2[:-1] and candidate_1[-1] < candidate_2[-1]:
                new_candidate = candidate_1 + (candidate_2[-1],)

                if not has_infrequent_subset(new_candidate, prune_set):
                    res.add(new_candidate)
    return res


def get_size_one_itemsets(dataset: List[Tuple[Any]], prune_set: Set[Tuple[int]], min_support: int = 0) \
        -> Dict[Tuple[int], int]:
    """
    Initially generates the itemsets of size 1
    :param dataset: List of transactions
    :param prune_set: Set of non-frequent itemsets
    :param min_support: Minimum support count, default 0
    :return: A dictionary that maps frequent one-itemsets to their support count
    """
    d = {}

    for line in dataset:
        for item in line:
            d[(int(item),)] = d.get((int(item),), 0) + 1
    prune(frequency_map=d, prune_set=prune_set, min_support=min_support)
    return d


def write_out(path: str, result: Dict[Tuple[int], int]) -> None:
    """
    Outputs the result of this program to a file
    :param path: Path to file
    :param result: Result mapping
    :return: None
    """
    out_file = open(path, 'w')
    for k, v in sorted(result.items()):
        out_file.write(f"{' '.join(str(i) for i in k)} ({v})\n")


def apriori(dataset: List[Tuple[Any]], min_support: int) -> Dict[Tuple[int], int]:
    """
    Performs apriori on dataset
    :param dataset: List of transactions
    :param min_support: minimum support count
    :return: A dictionary that maps frequent itemsets to their corresponding frequency
    """
    _prune_set = set()
    s = get_size_one_itemsets(dataset, prune_set=_prune_set, min_support=min_support)
    result = s
    i = 2
    while True:
        next_candidates = join_candidates(set(s.keys()), _prune_set)

        if not next_candidates:
            break

        pruned_support_map = get_supports(dataset=dataset, candidate_set=next_candidates,
                                          min_support=min_support, k=i, prune_set=_prune_set)
        result.update(pruned_support_map)
        s = pruned_support_map
        i += 1

    return result


if __name__ == "__main__":
    print("Reading Input")
    _min_support, _in_file_path, _out_file_path = (sys.argv[i] for i in range(1, 4))
    _min_support = int(_min_support)

    print("Generating Dataset...")
    in_file = open(_in_file_path, "r")
    _dataset = sorted([tuple(sorted({int(item) for item in line.split()})) for line in in_file])
    in_file.close()
    print("Dataset generated\n")

    print("Performing Apriori")

    start_time = time.time()
    _result = apriori(dataset=_dataset, min_support=_min_support)
    print(f"--- {int(time.time() - start_time)} seconds ---")

    write_out(_out_file_path, _result)
