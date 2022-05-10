# Imports
from dataclasses import dataclass
from typing import List
import csv
from itertools import combinations
from time import time
import tracemalloc

# RULES
ACTION_PURCHASE_LIMIT = 1
ACTION_MINIMUM_FRACTION = 1
MAXIMUM_PURCHASE_COST = 500

# DISPLAY CONSTANTS
DISPLAY_HEADER = ['Nom de l\'Action', 'Coût', 'Bénéfice %', 'Bénéfice value', 'Efficacité']
DISPLAY_HEADER_WHITE_SPACE = 2
DISPLAY_COLUMN_WIDTH = [len(header) + 2 * DISPLAY_HEADER_WHITE_SPACE for header in DISPLAY_HEADER]


# CLASSES
@dataclass(unsafe_hash=True)
class Action:
    """Class for actions"""
    name: str
    cost: int
    benefit_pct: int

    def benefit_value(self):
        return (self.cost * self.benefit_pct) / 100


@dataclass
class Portfolio2:
    """Class for portfolios"""
    actions: List[Action]

    def cost(self):
        return sum([a.cost for a in self.actions])

    def benefit(self):
        result = 0
        for action in self.actions:
            result += action.cost * action.benefit_pct / 100
        return result

    def performance(self):
        cost = self.cost()
        benefit = self.benefit()
        return ((cost + benefit) / cost - 1) * 100 if cost > 0 else 0


@dataclass
class Portfolio:
    """Class for portfolios"""
    data: List[Action]
    repartition: List[int]
    cost: int
    benefit_value: float
    benefit_pct: float

    def __init__(self, data, repartition=False):
        self.data = data
        self.repartition = self.get_portfolio_repartition(repartition)
        self.cost = self.get_portfolio_cost()
        self.benefit_value = self.get_portfolio_benefit_value()
        self.benefit_pct = self.get_portfolio_benefit_pct()

    def get_portfolio_repartition(self, repartition):
        if repartition:
            return repartition
        else:
            return [1 for _ in self.data]

    def get_portfolio_cost(self):
        """Method to get portfolio total cost"""
        return sum([action.cost for action in self.data if self.repartition[self.data.index(action)] == 1])

    def get_portfolio_benefit_value(self):
        """Method to get portfolio total benefit in value"""
        result = 0
        for action in [action for action in self.data if self.repartition[self.data.index(action)] == 1]:
            result += action.cost * action.benefit_pct / 100
        return result

    def get_portfolio_benefit_pct(self):
        """Method to get portfolio total benefit in percentage"""
        if self.cost == 0:
            return 0
        else:
            return ((self.cost + self.benefit_value) / self.cost - 1) * 100


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
def get_csv_data(data_csv):
    """Function to get data from CSV file"""

    # Init
    data = []

    # CSV reader
    with open(data_csv, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        next(data_reader)
        for row in data_reader:
            data.append(row)

    # Formatting result
    result = [[action_name, int(action_cost), int(action_profit[:-1])]
              for [action_name, action_cost, action_profit] in data]

    actions = [Action(*row) for row in result]
    return actions


# Functions
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


def get_portfolio_benefit_pct(portfolio):
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


# Display functions
def display_portfolio(portfolio):
    """Function that display nicely portfolio content"""

    # Header
    header_string = ''
    for i in range(len(DISPLAY_HEADER)):
        header_string += DISPLAY_HEADER[i].center(DISPLAY_COLUMN_WIDTH[i]) + '|'
    print(header_string)

    for action in portfolio.data:
        if portfolio.repartition[portfolio.data.index(action)] == 1:
            action_display = display_action(action)
            print(action_display)

    print(f'Nombre d\'actions en portefeuille : {sum(portfolio.repartition)}')
    print(f'Coût total du portefeuille : {portfolio.cost}')
    print(f'Valeur du portefeuille au bout de 2 ans :'
          f' {round(portfolio.cost + portfolio.benefit_value, 2)}')
    print(f'Valeur du bénéfice : {round(portfolio.benefit_value, 2)}')
    print(
        f'Bénéfice en pourcentage : '
        f'{round(portfolio.benefit_pct, 2)} %')


def display_action(action):
    """Function that display 5 elements in columns"""
    name_space, cost_space, benefit_pct_space, benefit_value_space, efficiency_space = DISPLAY_COLUMN_WIDTH

    display = f'{action.name}'.center(name_space) + '|' + \
              f'{action.cost}'.center(cost_space) + '|' + \
              f'{action.benefit_pct} %'.center(benefit_pct_space) + '|' + \
              f'{round(action.benefit_value(), 2)}'.center(benefit_value_space) + '|' + \
              f'{round(action.benefit_pct / action.cost, 2)}'.center(efficiency_space) + '|'
    return display


def display_best_portfolio(algorithm, actions: List[Action]):
    """Function that run algorithm and display the result"""
    # Header
    print(f'//  {algorithm.__name__}  //')
    print('Voici le meilleur portefeuille d\'investissement !')
    # Run the algorithm
    result = algorithm(actions)
    # Display result
    display_portfolio(result)


if __name__ == '__main__':
    pass
