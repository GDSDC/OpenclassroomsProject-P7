# Imports
from .algorithm_tools import get_portfolio_cost, MAXIMUM_PURCHASE_COST


# Optimised algorithm v1_3
def optimised_algorithm_v1_3(data):
    """Function that gets the best portfolio"""
    # Init / O(1)
    best_portfolio = []

    # Sort them by descending action benefit /  O(n*log(n))
    actions_data_sorted = sorted(data, key=lambda x: x[2], reverse=True)

    # Get actions under maximum cost /
    actions_data_sorted_under_max_purchase_cost = [action for action in actions_data_sorted if
                                                   get_portfolio_cost([action]) <= MAXIMUM_PURCHASE_COST]

    # Iteration over actions while total cost <= 500 / O(n)
    # Init
    best_portfolio.append(actions_data_sorted_under_max_purchase_cost[0])
    # 1st Iteration
    for i in range(1,len(actions_data_sorted_under_max_purchase_cost)):
        # Destructuring action
        action_i = actions_data_sorted_under_max_purchase_cost[i]
        _,action_i_cost,_ = action_i
        # Continue condition
        must_continue = False

        # 2nd Iteration
        for action_2 in actions_data_sorted_under_max_purchase_cost[i:]:
            # Destructuring action
            _, action_2_cost,action_2_benefit_ptc = action_2
            # Previous iteration of best_portfolio
            previous_iteration_portfolio = best_portfolio[:-1]
            # Las action added in portfolio / action added in previous iteration of best_portfolio
            _, last_action_added_in_portfolio_cost, last_action_added_in_portfolio_benefit_ptc = best_portfolio[-1]

            if (get_portfolio_cost(best_portfolio) + action_2_cost > MAXIMUM_PURCHASE_COST) and (
                    get_portfolio_cost(previous_iteration_portfolio) + action_2_cost <= MAXIMUM_PURCHASE_COST):
                if last_action_added_in_portfolio_cost * last_action_added_in_portfolio_benefit_ptc < action_2_cost * action_2_benefit_ptc:
                    best_portfolio.pop()
                    best_portfolio.append(action_2)
                    must_continue = True
                    if get_portfolio_cost(best_portfolio) == MAXIMUM_PURCHASE_COST:
                        break
        if must_continue is True:
            continue
        elif (get_portfolio_cost(best_portfolio) + action_i_cost < MAXIMUM_PURCHASE_COST):
            best_portfolio.append(action_i)
            if get_portfolio_cost(best_portfolio) == MAXIMUM_PURCHASE_COST:
                break
        else:
            continue

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = O(n) + 2 * O(1) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
