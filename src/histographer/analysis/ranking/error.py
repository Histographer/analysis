from src.histographer.analysis.ranking.mock import generate_mock_comparisons
import numpy as np
import matplotlib.pyplot as plt


def calculate_error_norm(ranking: np.ndarray, norm: int = 2):
    return np.linalg.norm(ranking - np.arange(ranking.shape[0]), norm)


def e_vs_error_rate(n_comparisons: int, n_objects: int, algorithm: staticmethod, repeats: int = 10, norm: int = 2):
    errors = []
    error_rates = np.linspace(0.01, 0.20, num=repeats)
    for error_rate in error_rates:
        error = 0
        for _ in range(repeats):
            comparisons = generate_mock_comparisons(n_comparisons, n_objects, error_rate)
            ranking = algorithm(comparisons, n_objects)
            error += calculate_error_norm(ranking, norm)
        errors.append(error / repeats)

    plt.plot(error_rates, errors)
    plt.show()


def e_vs_n_comparisons(n_objects: int, error_rate: float, algorithm: staticmethod, repeats: int = 10, norm: int = 2):
    errors = []
    n_comparisonss = [int(x) for x in np.linspace(20, 1000, num=repeats)]
    for n_comparisons in n_comparisonss:
        error = 0
        for _ in range(repeats):
            comparisons = generate_mock_comparisons(n_comparisons, n_objects, error_rate)
            ranking = algorithm(comparisons, n_objects)
            error += calculate_error_norm(ranking, norm)
        errors.append(error / repeats)

    plt.plot(n_comparisonss, errors)
    plt.show()


def e_vs_n_objects(n_comparisons: int, error_rate: float, algorithm: staticmethod, repeats: int = 10, norm: int = 2):
    errors = []
    n_objectss = [int(x) for x in np.linspace(5, 100, num=repeats)]
    for n_objects in n_objectss:
        error = 0
        for _ in range(repeats):
            comparisons = generate_mock_comparisons(n_comparisons, n_objects, error_rate)
            ranking = algorithm(comparisons, n_objects)
            error += calculate_error_norm(ranking, norm)
        errors.append(error / repeats)

    plt.plot(n_objectss, errors)
    plt.show()
