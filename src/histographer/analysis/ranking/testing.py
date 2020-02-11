from src.histographer.analysis.ranking.algorithms import balanced_rank_estimation, elo
from src.histographer.analysis.ranking.error import e_vs_error_rate, e_vs_n_comparisons, e_vs_n_objects

N_OBJECTS = 21
N_COMPARISONS = 500
ERROR_RATE = 0.05

e_vs_n_comparisons(N_OBJECTS, ERROR_RATE, [elo, balanced_rank_estimation], 50)
