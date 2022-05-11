# Imports
from algorithms.bruteforce import bruteforce_algorithm
from algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy
from algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic
from algorithms.algorithm_tools import display_portfolio, get_csv_data

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'
ACTIONS_DATA = get_csv_data(ACTIONS_DATA_CSV)


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
    display_best_portfolio(algorithm=bruteforce_algorithm, actions=ACTIONS_DATA)
    print('')
