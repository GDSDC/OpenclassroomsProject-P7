# Imports
from .algorithm_tools import get_portfolio_cost
from src.model import MAXIMUM_PURCHASE_COST, Portfolio, Action
from typing import List


# Optimised algorithm v1_4 -> Greedy algorithm
def optimised_algorithm_v1(data : List[Action]):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = Portfolio(data=[])

    # Sort them by descending action efficiency (benefit_ptc/cost) /  O(n*log(n))
    actions_data_sorted = sorted(data, key=lambda x: x.performance / x.cost, reverse=True)

    # Get actions under maximum cost /
    actions_data_sorted_under_max_purchase_cost = [action for action in actions_data_sorted if
                                                   action.cost <= MAXIMUM_PURCHASE_COST]

    # Sum action until total cost <= 500 / O(n)
    best_portfolio.data.append(actions_data_sorted_under_max_purchase_cost[0])
    for action in actions_data_sorted_under_max_purchase_cost[1:]:
        if best_portfolio.cost + action.cost <= MAXIMUM_PURCHASE_COST:
            best_portfolio.data.append(action)
            if best_portfolio.cost == MAXIMUM_PURCHASE_COST:
                break

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = O(n) + 2 * O(1) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
