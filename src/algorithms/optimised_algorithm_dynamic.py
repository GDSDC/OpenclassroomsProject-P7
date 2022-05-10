# Imports
from typing import List
from .algorithm_tools import MAXIMUM_PURCHASE_COST, Portfolio, Action


def optimised_algorithm_dynamic(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """
    Function that returns the best portfolio - dynamic algorithm
    cf https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos paragraphe Resolution exacte
    """

    # Init
    actions_count = len(actions)
    optimized_repartitions_space = [[list() for _ in range(max_cost + 1)] for _ in range(actions_count + 1)]

    for action_idx in range(actions_count + 1):
        for portfolio_funds in range(max_cost + 1):
            if action_idx == 0 or portfolio_funds == 0:
                #
                optimized_repartitions_space[action_idx][portfolio_funds].extend([0 for _ in range(actions_count)])
            else:
                action = actions[action_idx - 1]
                if portfolio_funds >= action.cost:
                    portfolio1 = Portfolio(
                        data=actions,
                        repartition=optimized_repartitions_space[action_idx - 1][portfolio_funds - action.cost]
                    )
                    portfolio2 = Portfolio(
                        data=actions,
                        repartition=optimized_repartitions_space[action_idx - 1][portfolio_funds]
                    )
                    if action.benefit_value() + portfolio1.benefit_value > portfolio2.benefit_value:
                        optimized_repartitions_space[action_idx][portfolio_funds].extend(
                            optimized_repartitions_space[action_idx - 1][portfolio_funds - action.cost]
                        )
                        optimized_repartitions_space[action_idx][portfolio_funds][action_idx - 1] = 1
                    else:
                        optimized_repartitions_space[action_idx][portfolio_funds].extend(
                            optimized_repartitions_space[action_idx - 1][portfolio_funds]
                        )
                else:
                    optimized_repartitions_space[action_idx][portfolio_funds].extend(
                        optimized_repartitions_space[action_idx - 1][portfolio_funds])

    return Portfolio(data=actions, repartition=optimized_repartitions_space[len(actions)][max_cost])
