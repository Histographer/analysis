from src.histographer.analysis.ranking.format import relative_favorability_from_comparisons
from typing import List, Tuple
import numpy as np


def balanced_rank_estimation(comparisons: List[Tuple[int, int]], n_objects: int):
    """
    Returns a permutations of the integers in the range of n_objects which represents an ordering based on the given
    pairwise comparisons.
    :param comparisons: A list containing tuples representing comparisons of the form (winner, loser)
    :param n_objects: The number of different objects the comparisons are sampled from
    :return: A numpy array of integers between 0 and n_objects ranked by their favorability
    """
    relative_favorability = relative_favorability_from_comparisons(comparisons, n_objects)
    relative_favorability[relative_favorability.nonzero()] = 2 * relative_favorability[relative_favorability.nonzero()] - 1
    scores = np.sum(relative_favorability, axis=1)
    return np.argsort(scores)
