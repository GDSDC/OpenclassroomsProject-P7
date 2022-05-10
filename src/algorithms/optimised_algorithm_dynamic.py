# Imports
from typing import List
from src.model import MAXIMUM_PURCHASE_COST, Portfolio, Action


def optimised_algorithm_dynamic(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that returns the best portfolio - dynamic algorithm"""

    # Init
    k = [[list() for _ in range(max_cost + 1)] for _ in range(len(actions) + 1)]

    for i in range(len(actions) + 1):
        for w in range(max_cost + 1):
            if i == 0 or w == 0:
                pass
            elif w >= actions[i - 1].cost:
                if actions[i - 1].value_after_two_years + Portfolio(
                        actions=k[i - 1][w - actions[i - 1].cost]).value_after_two_years > Portfolio(actions=k[i - 1][w]).value_after_two_years:
                    k[i][w].extend(k[i - 1][w - actions[i - 1].cost])
                    k[i][w].append(actions[i - 1])
                else:
                    k[i][w].extend(k[i - 1][w])
            else:
                k[i][w].extend(k[i - 1][w])

    return Portfolio(actions=k[len(actions)][max_cost])
