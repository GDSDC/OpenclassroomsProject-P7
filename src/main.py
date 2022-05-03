# Imports
from algorithms.bruteforce import get_best_portfolio as bt_algo
from algorithms.optimised_algorithm_v1 import get_best_portfolio as ov1_algo
from algorithms.optimised_algorithm_v1_2 import get_best_portfolio as ov2_algo
from algorithms.optimised_algorithm_v1_3 import get_best_portfolio as ov3_algo
from algorithms.algorithm_tools import display_portfolio

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Informations_sur_les_actions.csv'

if __name__ == '__main__':
    print('Voici le meilleur portefeuille d\'investissement !')
    display_portfolio(sorted(bt_algo(ACTIONS_DATA_CSV), key=lambda x: x[2],reverse=True))

