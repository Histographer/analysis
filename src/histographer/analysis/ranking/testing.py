from src.histographer.analysis.ranking.algorithms import balanced_rank_estimation
from src.histographer.analysis.ranking.error import e_vs_error_rate, e_vs_n_comparisons, e_vs_n_objects

N_OBJECTS = 21
N_COMPARISONS = 500
ERROR_RATE = 0.05

e_vs_error_rate(N_COMPARISONS, N_OBJECTS, balanced_rank_estimation, 50)
e_vs_n_comparisons(N_OBJECTS, ERROR_RATE, balanced_rank_estimation)
e_vs_n_objects(N_COMPARISONS, ERROR_RATE, balanced_rank_estimation)
