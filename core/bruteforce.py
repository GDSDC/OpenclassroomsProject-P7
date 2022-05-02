# Imports
from itertools import combinations
from main import get_portfolio_cost, get_portfolio_benefit_ptc, get_csv_data, display_portfolio,\
    MAXIMUM_PURCHASE_COST, ACTIONS_DATA_CSV


# Functions
def get_all_combinations(data):
    """Function that return a list of all combinations of input list items"""

    # Init
    comb = []

    # Get all Combinations
    for n in range(0, len(data) + 1):
        comb.extend([list(i) for i in list(combinations(data, n)) if list(i)])

    return comb


# Bruteforce algorithm
def get_best_portfolio(data_csv):
    """Function that gets the best portfolio"""
    # Get the actions data / O(n)
    actions_data = get_csv_data(data_csv)

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(actions_data)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [portfolio for portfolio in portfolios if
                                 get_portfolio_cost(portfolio) <= MAXIMUM_PURCHASE_COST]

    # Sort them by total benefit /  O(n*log(n))
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost,
                                              key=lambda x: get_portfolio_benefit_ptc(x) * get_portfolio_cost(x),
                                              reverse=True)

    # Best portfolio / O(1)
    return portfolios_under_max_cost_sorted[0]

    # Overall Complexity = O(n) + 2 * O(2^n) + O(n*log(n)) + O(1) => O(2^n)


if __name__ == '__main__':
    print('Voici le meilleur portefeuille d\'investissement !')
    display_portfolio(get_best_portfolio(ACTIONS_DATA_CSV))
