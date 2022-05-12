# Imports
from typing import List
from core.model import MAXIMUM_PURCHASE_COST, Portfolio, Action
from math import ceil as rounded_upp


def optimised_algorithm_dynamic_v2(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST,
                                   step: int = 5) -> Portfolio:
    """
    Function that returns the best portfolio - dynamic algorithm
    cf https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos paragraphe Resolution exacte
    """

    # Better Time Performance because of calculating on step interval

    # Init -> O(1)
    actions_count = len(actions)
    optimised_space = []

    # Iteration -> O(n^2)
    for nb_actions in range(actions_count + 1):
        # nb_actions -> number of actions in portfolio
        # Create an empty 'row' in optimised_space
        optimised_space.append([])
        for portfolio_funds in range(max_cost + 1):
            # portfolio_funds -> funds value for portfolio to buy in action
            # Create an empty 'column' in optimised_space[nb_actions]
            optimised_space[nb_actions].append([])

            # Initialization : empty value for init
            if nb_actions == 0 or portfolio_funds == 0:
                pass
            elif portfolio_funds % step != 0:
                pass
            else:
                action = actions[nb_actions - 1]  # current action index = nb_actions - 1
                # because actions[0] correspond to nb_actions = 1
                last_best_portfolio = optimised_space[nb_actions - 1][portfolio_funds]
                last_best_portfolio_without_action_funds = optimised_space[nb_actions - 1][
                    portfolio_funds - rounded_upp(action.cost / step) * step]

                if action.cost <= portfolio_funds:
                    value_after_two_years_portfolio_WITH_action = action.value_after_two_years + Portfolio(
                        actions=last_best_portfolio_without_action_funds).value_after_two_years
                    value_after_two_years_portfolio_WITHOUT_action = Portfolio(
                        actions=last_best_portfolio).value_after_two_years

                    if value_after_two_years_portfolio_WITH_action > value_after_two_years_portfolio_WITHOUT_action:
                        # Create new_best_portfolio with action in there
                        new_best_portfolio = []
                        new_best_portfolio.extend(last_best_portfolio_without_action_funds)
                        new_best_portfolio.extend([action])
                        optimised_space[nb_actions][portfolio_funds].extend(new_best_portfolio)

                    else:
                        # new_best_portfolio = last_best_portfolio
                        optimised_space[nb_actions][portfolio_funds].extend(last_best_portfolio)

                else:
                    # new_best_portfolio = last_best_portfolio
                    optimised_space[nb_actions][portfolio_funds].extend(last_best_portfolio)

    return Portfolio(actions=optimised_space[actions_count][max_cost])

    # Overall Complexity = O(n^2)
