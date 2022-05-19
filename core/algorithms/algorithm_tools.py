# Imports
from typing import List
import csv
from itertools import combinations
from time import time
import tracemalloc
from core.model import Action, Portfolio

# DISPLAY CONSTANTS
DISPLAY_HEADER = ['Nom de l\'Action', 'Coût', 'Bénéfice %', 'Bénéfice value', 'Efficacité']
DISPLAY_HEADER_WHITE_SPACE = 2
DISPLAY_COLUMN_WIDTH = [len(header) + 2 * DISPLAY_HEADER_WHITE_SPACE for header in DISPLAY_HEADER]


# FUNCTIONS
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


# Get Timing Decorator
def get_time_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        result = round(t2 - t1, 2)
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


# Get RAM peak Decorator
def get_ram_peak_func(func):
    def wrap_func(*args, **kwargs):
        tracemalloc.start()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        result = round(peak / 10 ** 6, 2)
        tracemalloc.stop()
        return result

    return wrap_func


# Functions
def get_csv_data(data_csv_path: str) -> Portfolio:
    """Function to get data from CSV file"""

    # Init
    data = []

    # CSV reader
    with open(data_csv_path, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        next(data_reader)
        for row in data_reader:
            data.append(row)

    # Formatting result
    result = [[action_name, float(action_cost), float(action_profit)]
              for [action_name, action_cost, action_profit] in data if data_validator([action_name, action_cost, action_profit])]

    return Portfolio(
        actions=[Action(action_name, action_cost, action_performance) for (action_name, action_cost, action_performance)
                 in
                 result])


def data_validator(data: List[str]) -> bool:
    """Function that validate if data is workable or not"""

    result = False

    try:
        _, action_cost, action_benefit_pct = data
        if float(action_cost) > 0  and float(action_benefit_pct) > 0:
            result = True
    except:
        pass

    return result






def get_all_combinations(portfolio: Portfolio) -> List[Portfolio]:
    """Function that return a list of all combinations of input list items"""

    # Init
    comb = []

    # Get all Combinations
    for n in range(0, len(portfolio.actions) + 1):
        comb.extend([Portfolio(actions=list(i)) for i in list(combinations(portfolio.actions, n))])

    return comb


def display_data_report(data_csv_path: str):
    """Function to show report of data in data_csv_path"""

    # Init
    data = []

    # CSV reader
    with open(data_csv_path, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        next(data_reader)
        for row in data_reader:
            data.append(row)

    # Formatting data
    data = [[action_name, float(action_cost), float(action_profit)]
            for [action_name, action_cost, action_profit] in data]

    actions_cost_null = [[action_name, action_cost, action_benefit_pct] for
                         [action_name, action_cost, action_benefit_pct] in data if action_cost == 0]

    actions_negative_cost = [[action_name, action_cost, action_benefit_pct] for
                             [action_name, action_cost, action_benefit_pct] in data if action_cost < 0]

    actions_benefit_null = [[action_name, action_cost, action_benefit_pct] for
                            [action_name, action_cost, action_benefit_pct] in data if action_benefit_pct == 0]

    actions_negative_benefit = [[action_name, action_cost, action_benefit_pct] for
                                [action_name, action_cost, action_benefit_pct] in data if action_benefit_pct < 0]

    data_unworkable_count = len(actions_cost_null) \
                            + len(actions_negative_cost) \
                            + len(actions_benefit_null) \
                            + len(actions_negative_benefit)

    display_message = f"Rapport d'exploration de l'ensemble des données :\n" \
                      f"Actions : {len(data)}\n" \
                      f"Actions coût nul : {len(actions_cost_null)}\n" \
                      f"Actions coût strictement négatif : {len(actions_negative_cost)}\n" \
                      f"Actions bénéfice nul : {len(actions_benefit_null)}\n" \
                      f"Actions bénéfice striquement négatif : {len(actions_negative_benefit)}\n" \
                      f"-------------------------------\n" \
                      f"Actions inexploitables : {data_unworkable_count}" \
                      f" / soit une part de {round(data_unworkable_count / len(data) * 100, 2)} %"

    print(display_message)


# Display functions
def display_portfolio(portfolio):
    """Function that display nicely portfolio content"""

    # Header
    header_string = ''
    for i in range(len(DISPLAY_HEADER)):
        header_string += DISPLAY_HEADER[i].center(DISPLAY_COLUMN_WIDTH[i]) + '|'
    print(header_string)

    for action in portfolio.actions:
        action_display = display_action(action)
        print(action_display)

    print(f'Nombre d\'actions en portefeuille : {len(portfolio.actions)}')
    print(f'Coût total du portefeuille : {round(portfolio.cost,2)}')
    print(f'Valeur du portefeuille au bout de 2 ans :'
          f' {round(portfolio.value_after_two_years, 2)}')
    print(f'Valeur du bénéfice : {round(portfolio.benefit_value, 2)}')
    print(
        f'Performance en pourcentage : '
        f'{round(portfolio.performance, 2)} %')


def display_action(action):
    """Function that display 5 elements in columns"""
    name_space, cost_space, benefit_pct_space, benefit_value_space, efficiency_space = DISPLAY_COLUMN_WIDTH

    display = f'{action.name}'.center(name_space) + '|' + \
              f'{action.cost}'.center(cost_space) + '|' + \
              f'{action.performance} %'.center(benefit_pct_space) + '|' + \
              f'{round(action.benefit_value, 2)}'.center(benefit_value_space) + '|' + \
              f'{round(action.efficiency, 2)}'.center(efficiency_space) + '|'
    return display


if __name__ == '__main__':
    pass
