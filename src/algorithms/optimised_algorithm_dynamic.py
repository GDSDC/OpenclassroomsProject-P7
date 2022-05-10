# Imports
from typing import List
from src.model import MAXIMUM_PURCHASE_COST, Portfolio, Action


def optimised_algorithm_dynamic(data: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that returns the best portfolio - dynamic algorithm"""

    # Init
    k = [[list() for _ in range(max_cost + 1)] for _ in range(len(data) + 1)]

    for i in range(len(data) + 1):
        for w in range(max_cost + 1):
            if i == 0 or w == 0:
                pass
            elif w >= data[i - 1].cost:
                if data[i - 1].benefit_value + Portfolio(
                        data=k[i - 1][w - data[i - 1].cost]).benefit_value > Portfolio(data=k[i - 1][w]).benefit_value:
                    k[i][w].extend(k[i - 1][w - data[i - 1].cost])
                    k[i][w].append(data[i - 1])
                else:
                    k[i][w].extend(k[i - 1][w])
            else:
                k[i][w].extend(k[i - 1][w])

    return Portfolio(data=k[len(data)][max_cost])
