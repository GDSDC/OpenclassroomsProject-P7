# Imports
from typing import List
from core.model import MAXIMUM_PURCHASE_COST, Portfolio
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy


def optimised_algorithm_v3(portfolio: Portfolio, max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """
    Function that returns the best portfolio - PSE algorithm
    cf https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos paragraphe Resolution exact
    """

    # Init
    actions_count = len(portfolio.actions)
    optimised_space = [[Portfolio(actions=[]), True]]
    lower_bound = optimised_algorithm_greedy(portfolio=portfolio, max_cost=max_cost).parameter_to_maximize
    print(f'lower_bound = {lower_bound}')

    # TODO: make it works
    for i in range(actions_count):
        action = portfolio.actions[i]
        portfolio_to_add = []

        for j in range(len(optimised_space)):
            [optimised_portfolio, is_valid] = optimised_space[j]

            if is_valid:

                upper_bound = optimised_portfolio.parameter_to_maximize + Portfolio(
                    actions=portfolio.actions[j:]).parameter_to_maximize

                if upper_bound <= lower_bound:
                    optimised_space[j] = [optimised_portfolio, False]
                    pass
                elif optimised_portfolio.cost + action.cost <= max_cost:
                    portfolio_to_add.append([Portfolio(actions=optimised_portfolio.actions + [action]), True])

        # Add portfolio_to_add to optimised_space
        optimised_space.extend(portfolio_to_add)

    return max(optimised_space, key=lambda x: x[0].parameter_to_maximize)[0]
