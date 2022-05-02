# Imports
import csv
from time import time
import tracemalloc

# from memory_profiler import profile

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Informations_sur_les_actions.csv'
ACTIONS_DATA_CSV_21 = 'resources/Informations_sur_les_actions21.csv'
# RULES
ACTION_PURCHASE_LIMIT = 1
ACTION_MINIMUM_FRACTION = 1
MAXIMUM_PURCHASE_COST = 500


# Timing Decorator
def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


# RAM Allocation Decorator
def ram_func(func):
    def wrap_func(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(
            f'Function {func.__name__!r} executed : '
            f'Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB')
        tracemalloc.stop()
        return result

    return wrap_func


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


# Optimised algorithm v1
def get_best_portfolio(data_csv):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = []

    # Get the actions data / O(n)
    actions_data = get_csv_data(data_csv)

    # Sort them by descending action benefit /  O(n*log(n))
    actions_data_sorted = sorted(actions_data, key=lambda x: x[2], reverse=True)

    # Sum action until total cost <= 500 / O(n)
    for action in actions_data_sorted:
        total_cost = get_portfolio_cost(best_portfolio) + get_portfolio_cost([action])
        if (total_cost > MAXIMUM_PURCHASE_COST):
            continue
        else:
            best_portfolio.append(action)
            if (total_cost == MAXIMUM_PURCHASE_COST):
                break

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = 2 * O(n) + 2 * O(n) + O(n*log(n)) => O(n*log(n))


# Display functions
def display_portfolio(portfolio):
    """Function that display nicely portfolio content"""

    # print(display_action(['Nom de l\'Action', 'Coût', 'Bénéfice %', 'Bénéfice value']))
    print('Nom de l\'Action'.center(20) + '|' + \
          'Coût'.center(10) + '|' + \
          'Bénéfice %'.center(20) + '|' + \
          'Bénéfice value'.center(20) + '|')

    for action in portfolio:
        action_display = display_action(action)

        print(action_display)

    print(f'Nombre d\'actions en portefeuille : {len(portfolio)}')
    print(f'Coût total du portefeuille : {get_portfolio_cost(portfolio)}')
    print(f'Valeur du portefeuille au bout de 2 ans :'
          f' {round(get_portfolio_cost(portfolio) + get_portfolio_benefit(portfolio), 2)}')
    print(f'Valeur du bénéfice : {round(get_portfolio_benefit(portfolio), 2)}')
    print(
        f'Bénéfice en pourcentage : {round(get_portfolio_benefit(portfolio) / get_portfolio_cost(portfolio) * 100, 2)} %')


def display_action(action):
    """Function that display 3 elements in columns"""
    action_name, action_cost, action_benefit_percentage = action
    name_space = 20
    cost_space = 10
    benefit_space = 20

    display = f'{action_name}'.center(name_space) + '|' + \
              f'{action_cost}'.center(cost_space) + '|' + \
              f'{action_benefit_percentage} %'.center(benefit_space) + '|' + \
              f'{round(action_benefit_percentage * action_cost / 100, 2)}'.center(benefit_space) + '|'
    return display


if __name__ == '__main__':
    print('Voici le meilleur portefeuille d\'investissement !')
    display_portfolio(sorted(get_best_portfolio(ACTIONS_DATA_CSV), key=lambda x: x[1]))
