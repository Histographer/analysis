from typing import List, Tuple
import numpy as np


def format_comparisons_as_matrix(comparisons: List[Tuple[int, int]], n_objects: int) -> np.ndarray:
    """
    Encodes the set of pairwise comparisons as a matrix
    :param comparisons: A list containing tuples representing comparisons of the form (winner, loser)
    :param n_objects: The number of different objects the comparisons are sampled from
    :return: A matrix in which element 0 <= [i, j] <= 1 represents the ratio of wins to losses of i over j
    """
    won_comparisons = np.zeros(shape=(n_objects, n_objects), dtype=float)
    total_comparisons = np.zeros(shape=(n_objects, n_objects), dtype=float)
    for winner, loser in comparisons:
        won_comparisons[winner, loser] += 1
        total_comparisons[winner, loser] += 1
        total_comparisons[loser, winner] += 1

    won_comparisons[won_comparisons.nonzero()] /= total_comparisons[total_comparisons.nonzero()]

    return won_comparisons
