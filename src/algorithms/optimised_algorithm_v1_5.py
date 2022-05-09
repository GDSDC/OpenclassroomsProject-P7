# Imports
from .algorithm_tools import get_portfolio_cost, MAXIMUM_PURCHASE_COST


class Portfolio:
    def __init__(self, data, repartition=False):
        self.data = data
        if repartition:
            self.repartition = repartition
        else:
            self.repartition = [1 for item in self.data]
        self.cost = self.get_portfolio_cost()
        self.benefit_value = self.get_portfolio_benefit_value()
        self.benefit_ptc = self.get_portfolio_benefit_ptc()

    def get_portfolio_cost(self):
        """Method to get portfolio total cost"""
        return sum([action[1] for action in self.data if self.repartition[self.data.index(action)] == 1])

    def get_portfolio_benefit_value(self):
        """Method to get portfolio total benefit in value"""
        result = 0
        for action in [action for action in self.data if self.repartition[self.data.index(action)] == 1]:
            _, action_cost, action_benfit_pct = action
            result += action_cost * action_benfit_pct / 100
        return result

    def get_portfolio_benefit_ptc(self):
        """Method to get portfolio total benefit in percentage"""
        return ((self.cost + self.benefit_value) / self.cost - 1) * 100


# Optimised algorithm v1_5
def optimised_algorithm_v1_5(data):
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
    best_portfolio.append(actions_data_sorted_under_max_purchase_cost[0])  # beginning portfolio with first action
    actions_data_sorted_under_max_purchase_cost.pop(0)  # removing the action from actions available

    # 1st STEP : Fill best_portfolio summing action until total cost <= 500 / O(n)
    i = 0
    for _ in range(len(actions_data_sorted_under_max_purchase_cost)):
        action = actions_data_sorted_under_max_purchase_cost[i]
        _, action_cost, _ = action
        total_cost = get_portfolio_cost(best_portfolio) + action_cost
        if total_cost > MAXIMUM_PURCHASE_COST:
            i += 1
            continue
        else:
            best_portfolio.append(action)
            actions_data_sorted_under_max_purchase_cost.remove(action)
            if total_cost == MAXIMUM_PURCHASE_COST:
                break

    # for best_action in reversed(best_portfolio):
    #     _,best_action_cost,best_action_benefit_ptc = best_action
    #     for action in actions_data_sorted_under_max_purchase_cost:
    #         _,action_cost,action_benefit_ptc = action
    #         if action_cost <= MAXIMUM_PURCHASE_COST - (get_portfolio_cost(best_portfolio) - best_action_cost):
    #             if action_cost * (100 + action_benefit_ptc) > best_action_cost * (100 + best_action_benefit_ptc):
    #                 best_portfolio.insert(action,best_portfolio.index(best_action))
    #                 actions_data_sorted_under_max_purchase_cost.append(best_action)
    #                 actions_data_sorted_under_max_purchase_cost.sort(key=lambda x: x[2], reverse=True)
    #                 actions_data_sorted_under_max_purchase_cost.remove(action)
    #                 break

    must_break_while_loop = False
    while not must_break_while_loop:
        must_break = False
        for i in reversed(range(len(best_portfolio) - 1, -1, -1)):
            if must_break:
                break
            else:
                best_action = best_portfolio[i]
                _, best_action_cost, best_action_benefit_ptc = best_action
                for action in actions_data_sorted_under_max_purchase_cost:
                    _, action_cost, action_benefit_ptc = action
                    if action_cost <= MAXIMUM_PURCHASE_COST - (get_portfolio_cost(best_portfolio) - best_action_cost):
                        if action_cost * (100 + action_benefit_ptc) > best_action_cost * (
                                100 + best_action_benefit_ptc):
                            best_portfolio.insert(action, best_portfolio.index(best_action))
                            actions_data_sorted_under_max_purchase_cost.append(best_action)
                            actions_data_sorted_under_max_purchase_cost.remove(action)
                            actions_data_sorted_under_max_purchase_cost.sort(key=lambda x: x[2], reverse=True)
                            must_break = True
                            print('CHANGED ACTION !')
                            break
                if best_action == best_portfolio[0]:
                    print('OK')
                    must_break_while_loop = True

    # TODO -> 2nd STEP : look for each element in best_portfolio (from right to left) if last action can be replaced by another with better befenit value regarding the max cost = action cost + remaining space
    #  Maybe then, try to restart process each time there is replacement because remaining space normally reduce so new oportunites can appear

    # Best portfolio / O(1)
    return best_portfolio

    # Overall Complexity = O(n) + 2 * O(1) + O(n*log(n)) => O(n*log(n))


if __name__ == '__main__':
    pass
