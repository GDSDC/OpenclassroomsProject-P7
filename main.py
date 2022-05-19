# Imports
from typing import List
from core.algorithms.bruteforce import bruteforce_algorithm
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy
from core.algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic
from core.algorithms.optimised_algorithm_dynamic_v3 import optimised_algorithm_dynamic_v3
from core.algorithms.algorithm_tools import display_portfolio, get_csv_data
from core.model import Action
import sys

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'
DEFAULT_ALGORITHM = 'dyn_algo'

ALGORITHM_PROVIDER = {
    'bf_algo': bruteforce_algorithm,
    'greedy_algo': optimised_algorithm_greedy,
    'dyn_algo': optimised_algorithm_dynamic,
    'dyn_algo_v3': optimised_algorithm_dynamic_v3
}

# DISPLAY MAIN FUNCTION
def display_best_portfolio(algorithm, actions):
    """Function that run algorithm and display the result"""
    # Header
    print(f'//  {algorithm.__name__}  //')
    print('Voici le meilleur portefeuille d\'investissement !')
    # Run the algorithm
    result = algorithm(actions=actions)
    # Display result
    display_portfolio(result)


if __name__ == '__main__':
    print('')

    algo_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ALGORITHM
    algorithm = ALGORITHM_PROVIDER[algo_name]

    csv_path = sys.argv[2] if  len(sys.argv) > 2 else ACTIONS_DATA_CSV
    actions : List[Action] = get_csv_data(csv_path)

    display_best_portfolio(algorithm=algorithm, actions=actions)
    print('')
