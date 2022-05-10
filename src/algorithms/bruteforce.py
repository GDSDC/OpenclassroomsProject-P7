# Imports
from typing import List
from .algorithm_tools import get_portfolio_cost, get_portfolio_benefit_pct, get_all_combinations
from src.model import MAXIMUM_PURCHASE_COST, Portfolio, Action


# Bruteforce algorithm
def bruteforce_algorithm(data: List[Action]) -> Portfolio:
    """Function that gets the best portfolio"""

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(data)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [portfolio for portfolio in portfolios if
                                 sum([action.cost for action in portfolio]) <= MAXIMUM_PURCHASE_COST]

    # Sort them by total benefit /  O(n*log(n))
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost,
                                              key=lambda x: sum([action.value_after_two_years for action in x]),
                                              reverse=True)

    # Best portfolio / O(n) ??
    return Portfolio(data=portfolios_under_max_cost_sorted[0])

    # Overall Complexity = 2 * O(2^n) + O(n*log(n)) + O(n) => O(2^n)


if __name__ == '__main__':
    pass
