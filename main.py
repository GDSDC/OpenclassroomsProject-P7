# Imports
from core.algorithms.bruteforce import bruteforce_algorithm
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy
from core.algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic
from core.algorithms.optimised_algorithm_dynamic_v2 import optimised_algorithm_dynamic_v2
from core.algorithms.algorithm_tools import display_portfolio, get_csv_data
import sys

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'
DEFAULT_ALGORITHM = 'dyn_algo'

ALGORITHM_PROVIDER = {
    'bf_algo': bruteforce_algorithm,
    'greedy_algo': optimised_algorithm_greedy,
    'dyn_algo': optimised_algorithm_dynamic,
    'dyn_algo_v2': optimised_algorithm_dynamic_v2
}


# DISPLAY MAIN FUNCTION
def display_best_portfolio(algorithm, portfolio):
    """Function that run algorithm and display the result"""
    # Header
    print(f'//  {algorithm.__name__}  //')
    print('Voici le meilleur portefeuille d\'investissement !')
    # Run the algorithm
    result = algorithm(portfolio)
    # Display result
    display_portfolio(result)


if __name__ == '__main__':
    print('')

    algo_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ALGORITHM
    algorithm_to_run = ALGORITHM_PROVIDER[algo_name]

    csv_path = sys.argv[2] if len(sys.argv) > 2 else ACTIONS_DATA_CSV
    portfolio_to_optimize = get_csv_data(csv_path)

    display_best_portfolio(algorithm=algorithm_to_run, portfolio=portfolio_to_optimize)
    print('')
