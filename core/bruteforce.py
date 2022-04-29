# Imports
import csv
from itertools import combinations

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Informations_sur_les_actions.csv'
ACTIONS_DATA_CSV_21 = 'resources/Informations_sur_les_actions21.csv'
# RULES
ACTION_PURCHASE_LIMIT = 1
ACTION_MINIMUM_FRACTION = 1
MAXIMUM_PURCHASE_COST = 500


# Functions
def get_csv_data(data_csv):
    """Function to get data from CSV file"""

    # Init
    data = []

    # CSV reader
    with open(data_csv, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        for row in data_reader:
            data.append(row)

    # Formating result
    result = [[action_name, int(action_cost), int(action_profit[:-1])]
              for [action_name, action_cost, action_profit] in data[1:]]

    return result


def get_all_combinations(data):
    """Function that return a list of all combinations of input list items"""

    # Init
    comb = []

    # Get all Combinations
    for n in range(0, len(data) + 1):
        comb.extend([list(i) for i in list(combinations(data, n)) if list(i)])

    return comb


def get_portfolio_cost(portfolio):
    """Function that returns the total value of a portfolio"""
    # Init
    portfolio_cost = 0
    # Iteration
    for (_, action_cost, _) in portfolio:
        portfolio_cost += action_cost
    return portfolio_cost


def get_portfolio_benefit(portfolio):
    """Function that returns the total benefit of a portfolio"""
    # Init
    portfolio_value = 0
    portfolio_cost = get_portfolio_cost(portfolio)

    # Iteration
    for (_, action_cost, action_benefit_percentage) in portfolio:
        portfolio_value += action_cost * (1 + action_benefit_percentage / 100)

    # Getting total profit
    portfolio_benefit_value = portfolio_value - portfolio_cost

    return portfolio_benefit_value


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
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost, key=lambda x: get_portfolio_benefit(x),
                                              reverse=True)

    # Best portfolio / O(1)
    return portfolios_under_max_cost_sorted[0]

    # Overall Complexity = O(n) + 2 * O(2^n) + O(n*log(n)) + O(1) => O(2^n)


# Display functions
def display_portfolio(portfolio):
    """Function that display nicely portfolio content"""

    print(display_action(['Nom de l\'Action','Coût','Bénéfice']))

    for action in portfolio:
        action_display = display_action(action)

        print(action_display)


def display_action(action):
    """Function that display 3 elements in columns"""
    action_name, action_cost, action_benefit_percentage = action
    name_space = 20
    cost_space = 10
    benefit_space = 20

    display = f'{action_name}'.center(name_space) + '|' + \
              f'{action_cost}'.center(cost_space) + '|' + \
              f'{action_benefit_percentage} %'.center(benefit_space) + '|'

    return display


if __name__ == '__main__':
    print('Voici le meilleur portefeuille d\'investissement !')
    display_portfolio(get_best_portfolio(ACTIONS_DATA_CSV))
