# Imports
from .algorithm_tools import get_portfolio_cost, get_portfolio_benefit_pct, get_all_combinations, \
    MAXIMUM_PURCHASE_COST, Portfolio, Action


# Bruteforce algorithm
def bruteforce_algorithm(data) -> Portfolio:
    """Function that gets the best portfolio"""

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(data)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [portfolio for portfolio in portfolios if
                                 get_portfolio_cost(portfolio) <= MAXIMUM_PURCHASE_COST]

    # Sort them by total benefit /  O(n*log(n))
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost,
                                              key=lambda x: get_portfolio_benefit_pct(x) * get_portfolio_cost(x),
                                              reverse=True)

    # Best portfolio / O(1)
    # TODO: revoir O
    repartition = [1 if action in portfolios_under_max_cost_sorted[0] else 0 for action in data]
    return Portfolio(data=[Action(item) for item in data],repartition=repartition)

    # Overall Complexity = 2 * O(2^n) + O(n*log(n)) + O(1) => O(2^n)


if __name__ == '__main__':
    pass
