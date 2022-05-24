# Imports
from typing import List
from core.model import MAXIMUM_PURCHASE_COST, Portfolio, Action
from math import ceil


def optimised_algorithm_dynamic(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """
    Function that returns the best portfolio - dynamic algorithm
    cf https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos paragraphe Resolution exact
    """

    # Init -> O(1)
    actions_count = len(actions)
    # Creating result array initialized with empty Portfolios
    optimised_space: List[List[Portfolio]] = [[Portfolio(actions=[]) for _ in range(max_cost + 1)] for _ in
                                              range(actions_count + 1)]

    # Iteration -> O(n^2)
    for nb_actions in range(actions_count + 1):
        # nb_actions -> number of actions in portfolio
        for portfolio_funds in range(max_cost + 1):
            # portfolio_funds -> maximum cost of Portfolio

            # Initialization : empty Portfolio for init
            if nb_actions == 0 or portfolio_funds == 0:
                pass
            else:
                action = actions[nb_actions - 1]  # current action index = nb_actions - 1
                # because actions[0] correspond to nb_actions = 1
                previous_portfolio = optimised_space[nb_actions - 1][portfolio_funds]
                portfolio_without_action_funds = optimised_space[nb_actions - 1][portfolio_funds - ceil(action.cost)]

                # Init
                actual_portfolio = previous_portfolio

                if action.cost <= portfolio_funds:
                    # new_portfolio is portfolio_without_action_funds + action
                    new_portfolio_parameter_to_maximize = \
                        action.parameter_to_maximize + portfolio_without_action_funds.parameter_to_maximize

                    if new_portfolio_parameter_to_maximize > previous_portfolio.parameter_to_maximize:
                        # new portfolio with action in there
                        new_actions = portfolio_without_action_funds.actions + [action]
                        actual_portfolio = Portfolio(actions=new_actions)

                # Filling optimised_space with actual_portfolio
                optimised_space[nb_actions][portfolio_funds] = actual_portfolio

    # Result
    return optimised_space[actions_count][max_cost]

    # Overall Complexity = O(n^2)
