# Imports
from .algorithm_tools import get_portfolio_cost, MAXIMUM_PURCHASE_COST


# Optimised algorithm v1_4 -> Greedy algorithm
def optimised_algorithm_v1_4(data):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = []

    # Sort them by descending action efficiency (benefit_ptc/cost) /  O(n*log(n))
    actions_data_sorted = sorted(data, key=lambda x: x[2] / x[1], reverse=True)

    # Get actions under maximum cost /
    actions_data_sorted_under_max_purchase_cost = [action for action in actions_data_sorted if
                                                   get_portfolio_cost([action]) <= MAXIMUM_PURCHASE_COST]

    # Sum action until total cost <= 500 / O(n)
    best_portfolio.append(actions_data_sorted_under_max_purchase_cost[0])
    for action in actions_data_sorted_under_max_purchase_cost[1:]:
        _, action_cost, _ = action
        if get_portfolio_cost(best_portfolio) + action_cost <= MAXIMUM_PURCHASE_COST:
            best_portfolio.append(action)
            if get_portfolio_cost(best_portfolio) == MAXIMUM_PURCHASE_COST:
                break

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = O(n) + 2 * O(1) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
