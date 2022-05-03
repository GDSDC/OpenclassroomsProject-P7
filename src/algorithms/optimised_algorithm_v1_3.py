# Imports
from .algorithm_tools import get_portfolio_cost, get_portfolio_benefit_ptc, get_csv_data, display_portfolio, \
    MAXIMUM_PURCHASE_COST


# Optimised algorithm v1
def get_best_portfolio(data_csv):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = []

    # Get the actions data / O(n)
    actions_data = get_csv_data(data_csv)

    # Sort them by descending action benefit /  O(n*log(n))
    actions_data_sorted = sorted(actions_data, key=lambda x: x[2], reverse=True)

    # Get actions under maximum cost /
    actions_data_sorted_under_max_purchase_cost = [action for action in actions_data_sorted if
                                                   get_portfolio_cost([action]) <= MAXIMUM_PURCHASE_COST]

    # Sum action until total cost <= 500 / O(n)
    best_portfolio.append(actions_data_sorted_under_max_purchase_cost[0])
    # TODO : write the section below with destructuration so we can understand
    for i in range(1, len(actions_data_sorted_under_max_purchase_cost)):
        must_continue = False
        for action in actions_data_sorted_under_max_purchase_cost[i:]:
            if (get_portfolio_cost(best_portfolio) + action[1] > MAXIMUM_PURCHASE_COST) and (
                    get_portfolio_cost(best_portfolio[:-1]) + action[1] <= MAXIMUM_PURCHASE_COST):
                if best_portfolio[-1][1] * best_portfolio[-1][2] < action[1] * action[2]:
                    best_portfolio.pop()
                    best_portfolio.append(action)
                    must_continue = True
                    if get_portfolio_cost(best_portfolio) == MAXIMUM_PURCHASE_COST:
                        break
        if must_continue is True:
            continue
        elif (get_portfolio_cost(best_portfolio) + actions_data_sorted_under_max_purchase_cost[i][
                1] < MAXIMUM_PURCHASE_COST):
            best_portfolio.append(actions_data_sorted_under_max_purchase_cost[i])
            if get_portfolio_cost(best_portfolio) == MAXIMUM_PURCHASE_COST:
                break
        else:
            continue

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = 2 * O(n) + 2 * O(n) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
