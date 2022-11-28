# Imports
from core.algorithms.bruteforce import bruteforce_algorithm
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy
from core.algorithms.optimized import optimised_algorithm_dynamic
from core.algorithms.optimised_algorithm_dynamic_v2 import optimised_algorithm_dynamic_v2
from core.algorithms.algorithm_tools import display_portfolio, get_csv_data
import sys

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/actions_data/Informations_sur_les_actions.csv'
DEFAULT_ALGORITHM = 'optimized'

ALGORITHM_PROVIDER = {
    'bruteforce': bruteforce_algorithm,
    'optimized': optimised_algorithm_dynamic,
    'dyn_algo_v2': optimised_algorithm_dynamic_v2,
    'greedy_algo': optimised_algorithm_greedy
}


# DISPLAY MAIN FUNCTION
def display_best_portfolio(algorithm, actions):
    """Function that run algorithm and display the result"""
    # Header
    print(f'//  {algorithm.__name__}  //')
    print('Voici le meilleur portefeuille d\'investissement !')
    # Run the algorithm
    result = algorithm(actions)
    # Display result
    display_portfolio(result)


if __name__ == '__main__':

    print('')

    # Init
    algo_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ALGORITHM
    algorithm_to_run = ALGORITHM_PROVIDER[algo_name]

    csv_path = sys.argv[2] if len(sys.argv) > 2 else ACTIONS_DATA_CSV
    actions_from_csv = get_csv_data(csv_path)

    # Display Result
    display_best_portfolio(algorithm=algorithm_to_run, actions=actions_from_csv)
    print('')
