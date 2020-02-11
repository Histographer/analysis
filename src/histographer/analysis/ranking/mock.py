from typing import List, Tuple
from random import randrange, random


def generate_mock_comparisons(n_comparisons: int, n_objects: int, error_rate: float) -> List[Tuple[int, int]]:
    """
    Used to generate a set of mock pairwise comparisons for testing purposes.
    :param n_comparisons: The number of comparisons to be generated
    :param n_objects: The number of objects the comparisons will be sampled from
    :param error_rate: The probability that a superior object is deemed inferior
    :return: A list of tuples of the form (a, b), which indicate that 'a' compared favorably to 'b'
    """
    comparisons = []
    for _ in range(n_comparisons):
        a, b = randrange(n_objects), randrange(n_objects)
        while a == b:
            b = randrange(n_objects)

        if random() < error_rate:
            comparisons.append((min(a, b), max(a, b)))
        else:
            comparisons.append((max(a, b), min(a, b)))

    return comparisons
