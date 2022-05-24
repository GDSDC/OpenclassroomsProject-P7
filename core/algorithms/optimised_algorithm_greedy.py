# Imports
from core.model import MAXIMUM_PURCHASE_COST, Portfolio, Action
from typing import List


# Optimised algorithm v1_4 -> Greedy algorithm
def optimised_algorithm_greedy(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that gets the best portfolio"""

    # Init / O(1)
    best_portfolio = Portfolio(actions=[])

    # Get actions under maximum cost / O(n)
    actions_under_max_cost = [action for action in actions if action.cost <= max_cost]

    # Sort them by descending action efficiency /  O(n*log2(n))
    actions_sorted_under_max_cost = sorted(actions_under_max_cost, key=lambda x: x.efficiency, reverse=True)

    # Sum action until total cost <= 500 / O(n)
    best_portfolio.actions.append(actions_sorted_under_max_cost[0])
    for action in actions_sorted_under_max_cost[1:]:
        if best_portfolio.cost + action.cost <= max_cost and action.cost > 0:
            best_portfolio.actions.append(action)
            if best_portfolio.cost == max_cost:
                break

    # Result / O(1)
    return best_portfolio

    # Overall Complexity => O(n*log2(n)) : Log2 Linear


if __name__ == '__main__':
    pass
