from src.histographer.analysis.ranking.format import relative_favorability_from_comparisons, centrality_matrix_from_comparisons
from typing import List, Tuple, Callable
import numpy as np


def balanced_rank_estimation(comparisons: List[Tuple[int, int]], n_objects: int) -> np.ndarray:
    """
    Implements the BRE-algorithm to find an ordering based on pairwise comparisons
    :param comparisons: A list containing tuples representing comparisons of the form (winner, loser)
    :param n_objects: The number of different objects the comparisons are sampled from
    :return: A numpy array of integers between 0 and n_objects ranked by their favorability
    """
    relative_favorability = relative_favorability_from_comparisons(comparisons, n_objects)
    relative_favorability[relative_favorability.nonzero()] = 2 * relative_favorability[relative_favorability.nonzero()] - 1
    scores = np.sum(relative_favorability, axis=1)
    return np.argsort(scores)


def elo(comparisons: List[Tuple[int, int]], n_objects: int) -> np.ndarray:
    """
    Implements the ELO-algorithm to find an ordering based on pairwise comparisons
    :param comparisons: A list containing tuples representing comparisons of the form (winner, loser)
    :param n_objects: The number of different objects the comparisons are sampled from
    :return: A numpy array of integers between 0 and n_objects ranked by their favorability
    """
    scores = np.full(n_objects, 1000, dtype=float)
    for winner, loser in comparisons:
        prob_result = 1 / (1 + 1.0 * np.power(10, (scores[winner] - scores[loser]) / 400))
        scores[winner] += (1 - prob_result) * 800 / len(comparisons)
        scores[loser] -= prob_result * 800 / len(comparisons)

    return np.argsort(scores)


def rank_centrality(comparisons: List[Tuple[int, int]], n_objects: int) -> np.ndarray:
    """
    Finds an ordering based on pairwise comparison using a random-walk interpretation over
    a rank centrality graph.
    :param comparisons: A list containing tuples representing comparisons of the form (winner, loser)
    :param n_objects: The number of different objects the comparisons are sampled from
    :return: A numpy array of integers between 0 and n_objects ranked by their favorability
    """
    cm = centrality_matrix_from_comparisons(comparisons, n_objects)

    eigenvalues, eigenvectors = np.linalg.eig(cm.T)
    scores = eigenvectors[:, np.isclose(eigenvalues, 1)]
    scores = scores[:, 0]
    scores /= np.sum(scores)
    return np.argsort(scores)
