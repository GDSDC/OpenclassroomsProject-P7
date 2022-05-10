# Imports
from typing import List

from algorithms.bruteforce import bruteforce_algorithm
from algorithms.optimised_algorithm_v1 import optimised_algorithm_v1
from algorithms.optimised_algorithm_v1_2 import optimised_algorithm_v1_2
from algorithms.optimised_algorithm_v1_3 import optimised_algorithm_v1_3
from algorithms.optimised_algorithm_v1_4 import optimised_algorithm_v1_4
from algorithms.optimised_algorithm_v1_5 import optimised_algorithm_v1_5
from algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic
from algorithms.algorithm_tools import Action, display_best_portfolio, get_csv_data
import sys

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'
ACTIONS_DATA = get_csv_data(ACTIONS_DATA_CSV)
DEFAULT_ALGORITHM = 'optimised_algorithm_dynamic'

ALGORITHM_PROVIDER = {
    'bruteforce_algorithm': bruteforce_algorithm,
    'optimised_algorithm_v1': optimised_algorithm_v1,
    'optimised_algorithm_v1_2': optimised_algorithm_v1_2,
    'optimised_algorithm_v1_3': optimised_algorithm_v1_3,
    'optimised_algorithm_v1_4': optimised_algorithm_v1_4,
    'optimised_algorithm_v1_5': optimised_algorithm_v1_5,
    'optimised_algorithm_dynamic': optimised_algorithm_dynamic,
}

if __name__ == '__main__':
    print('')
    actions: List[Action] = get_csv_data(ACTIONS_DATA_CSV)

    algo_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ALGORITHM
    algorithm = ALGORITHM_PROVIDER[algo_name]

    display_best_portfolio(algorithm=algorithm, actions=actions)
    print('')
