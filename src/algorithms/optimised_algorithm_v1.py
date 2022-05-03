# Imports
from .algorithm_tools import get_portfolio_cost, get_csv_data, display_portfolio, MAXIMUM_PURCHASE_COST


# Optimised algorithm v1
def get_best_portfolio(data_csv):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = []

    # Get the actions data / O(n)
    actions_data = get_csv_data(data_csv)

    # Sort them by descending action benefit /  O(n*log(n))
    actions_data_sorted = sorted(actions_data, key=lambda x: x[2], reverse=True)

    # Sum action until total cost <= 500 / O(n)
    for action in actions_data_sorted:
        total_cost = get_portfolio_cost(best_portfolio) + get_portfolio_cost([action])
        if total_cost > MAXIMUM_PURCHASE_COST:
            continue
        else:
            best_portfolio.append(action)
            if total_cost == MAXIMUM_PURCHASE_COST:
                break

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = 2 * O(n) + 2 * O(n) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
