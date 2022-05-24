# Imports
from core.algorithms.algorithm_tools import get_all_combinations
from core.model import MAXIMUM_PURCHASE_COST, Portfolio, Action
from typing import List

# Bruteforce algorithm
def bruteforce_algorithm(actions: List[Action], max_cost: int = MAXIMUM_PURCHASE_COST) -> Portfolio:
    """Function that gets the best portfolio"""

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(actions)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [portfolio for portfolio in portfolios if portfolio.cost <= max_cost]

    # Best portfolio / O(2^n)
    return max(portfolios_under_max_cost, key=lambda x: x.parameter_to_maximize)

    # Overall Complexity = 3 * O(2^n) => O(2^n)


if __name__ == '__main__':
    pass
