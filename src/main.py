# Imports
from algorithms.bruteforce import bruteforce_algorithm
from algorithms.optimised_algorithm_v1 import optimised_algorithm_v1
from algorithms.optimised_algorithm_v1_2 import optimised_algorithm_v1_2
from algorithms.optimised_algorithm_v1_3 import optimised_algorithm_v1_3
from algorithms.optimised_algorithm_v1_4 import optimised_algorithm_v1_4
from algorithms.optimised_algorithm_v1_5 import optimised_algorithm_v1_5
from algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic
from algorithms.algorithm_tools import display_best_portfolio, get_csv_data

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'
ACTIONS_DATA = get_csv_data(ACTIONS_DATA_CSV)

if __name__ == '__main__':
    print('')
    display_best_portfolio(algorithm=optimised_algorithm_dynamic, data=ACTIONS_DATA)
    print('')