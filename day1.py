import numpy as np

full_credit = 25000
half_credit = 50000
no_extra_credit = 10000000000

# # ---------------------------------------------------------------------
# # Idea 1: factorial approach, binning continuous variables into 16 bins
# # ---------------------------------------------------------------------

# tile_size = np.linspace(0.1,0.6, num=16)
# match_score = np.arange(85,101)
# preview_length = np.linspace(30,121, num=16)
# preview_type = ["TT","AC"]

# total_combinations = len(tile_size) * len(match_score) * len(preview_length) * len(preview_type)

# print(total_combinations) 
# 8,192 total unique combinations of experiments

# print(full_credit/total_combinations)
# ~3 experimental units per experiment (3.0517578125)


# ---------------------------------------------------------------------
# Idea 2: factorial approach, binning continuous variables into 10 bins
# ---------------------------------------------------------------------

tile_size = np.linspace(0.1,0.6, num=7)
match_score = np.arange(94,101)
preview_length = np.linspace(30,121, num=7)
preview_type = ["TT","AC"]

total_combinations = len(tile_size) * len(match_score) * len(preview_length) * len(preview_type)

print(total_combinations) 
# 686 total unique combinations of experiments

print(full_credit/total_combinations)
# ~36 experimental units per experiment

# ---------------------------------------------------------------------
# Notes from class about designing the factorial experiment
# ---------------------------------------------------------------------
# 1: Don;t investigate factors that are highly correlated
# 2. Don't choose levels that are ver similar.
# 3. Don't choose factors that are bad to manupulate outside of an experiment