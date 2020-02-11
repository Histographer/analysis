import numpy as np


def calculate_error_norm(ranking: np.ndarray, norm: int = 2):
    return np.linalg.norm(ranking - np.arange(ranking.shape[0]), norm)
