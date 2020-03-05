from src.histographer.analysis.ranking.algorithms import balanced_rank_estimation, elo, rank_centrality, iterate_active_elo, active_elo
from src.histographer.analysis.ranking.mock import generate_mock_comparisons, generate_mock_comparisons_btl, save_dummy_gradient
from src.histographer.analysis.ranking.error import e_vs_error_rate, e_vs_n_comparisons, e_vs_n_objects
from random import sample
import numpy as np

N_COMPARISONS = 500
N_OBJECTS = 10
ERROR_RATE = 0.05

save_dummy_gradient((0, 255, 0), (255, 255, 255), (512, 512), 16)
