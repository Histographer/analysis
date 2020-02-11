from src.histographer.analysis.ranking.mock import generate_mock_comparisons
import numpy as np
import matplotlib.pyplot as plt


def calculate_error_norm(ranking: np.ndarray, norm: int = 2):
    """
    Calculates the error in the given ranking as a distance from the correct solution in the space given by 'norm'
    :param ranking: The ranking to be evaluated
    :param norm: The norm of the space error will be calculated in
    :return: A scalar giving an indication of how far off the given ranking was
    """
    return np.linalg.norm(ranking - np.arange(ranking.shape[0]), norm)


def e_vs_error_rate(n_comparisons: int, n_objects: int, algorithm: staticmethod, repeats: int = 10, norm: int = 2):
    """
    Plots the error as calculated by 'calculate_error_norm' against a number of different error rates
    :param n_comparisons: The number of pairwise comparisons performed
    :param n_objects: The number of different objects the comparisons are sampled from
    :param algorithm: A function object designating the algorithm which is to be tested
    :param repeats: The number of times a set of comparisons will be generated for a given error rate, as well as the
    the number of different error rates to be evaluated
    :param norm: The norm of the space used to calculate the error
    :return: Returns nothing, displays a graph
    """
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
    """
    Plots the error as calculated by 'calculate_error_norm' against a number of different error rates
    :param n_objects: The number of different objects the comparisons are sampled from
    :param error_rate: The ratio of pairwise comparisons which to not reflect the 'true' permutation
    :param algorithm: A function object designating the algorithm which is to be tested
    :param repeats: The number of times a set of comparisons will be generated for a given number of comparisons,
    as well as the the number of different n_comparisons to be evaluated
    :param norm: The norm of the space used to calculate the error
    :return: Returns nothing, displays a graph
    """
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
    """
    Plots the error as calculated by 'calculate_error_norm' against a number of different error rates
    :param n_comparisons: The number of pairwise comparisons performed
    :param error_rate: The ratio of pairwise comparisons which to not reflect the 'true' permutation
    :param algorithm: A function object designating the algorithm which is to be tested
    :param repeats: The number of times a set of comparisons will be generated for a given number of objects,
    as well as the the number of different n_objects to be evaluated
    :param norm: The norm of the space used to calculate the error
    :return: Returns nothing, displays a graph
    """
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
