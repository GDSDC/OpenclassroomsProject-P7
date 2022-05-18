# Imports
from typing import List
from core.algorithms.algorithm_tools import get_portfolio_cost, get_portfolio_benefit_pct, get_all_combinations
from core.model import MAXIMUM_PURCHASE_COST, Portfolio, Action


# Bruteforce algorithm
def bruteforce_algorithm(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that gets the best portfolio"""

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(actions)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [Portfolio(actions=portfolio) for portfolio in portfolios if
                                 sum([action.cost for action in portfolio]) <= max_cost]

    # Sort them by total benefit /  O(n*log(n))
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost,
                                              key=lambda x: x.parameter_to_maximize,
                                              reverse=True)

    # Best portfolio / O(n) ??
    return portfolios_under_max_cost_sorted[0]

    # Overall Complexity = 2 * O(2^n) + O(n*log(n)) + O(n) => O(2^n)


if __name__ == '__main__':
    pass
