# Imports
from typing import List
from .algorithm_tools import MAXIMUM_PURCHASE_COST, Portfolio, Action


def optimised_algorithm_dynamic(data: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that returns the best portfolio - dynamic algorithm"""

    # Init
    k = [[list() for _ in range(max_cost + 1)] for _ in range(len(data) + 1)]

    for i in range(len(data) + 1):
        for w in range(max_cost + 1):
            if i == 0 or w == 0:
                k[i][w].extend([0 for _ in range(len(data))])
            elif w >= data[i - 1].cost:
                if data[i - 1].benefit_value + Portfolio(data=data, repartition=k[i - 1][
                    w - data[i - 1].cost]).benefit_value > Portfolio(data=data, repartition=k[i - 1][w]).benefit_value:
                    k[i][w].extend(k[i - 1][w - data[i - 1].cost])
                    k[i][w][i - 1] = 1
                else:
                    k[i][w].extend(k[i - 1][w])
            else:
                k[i][w].extend(k[i - 1][w])

    return Portfolio(data=data, repartition=k[len(data)][max_cost])
