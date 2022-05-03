# Imports
from .algorithm_tools import get_portfolio_cost, get_portfolio_benefit_ptc, get_all_combinations, get_csv_data, \
    MAXIMUM_PURCHASE_COST


# Bruteforce algorithm
def get_best_portfolio(data_csv):
    """Function that gets the best portfolio"""
    # Get the actions data / O(n)
    actions_data = get_csv_data(data_csv)

    # Generate all combinations of portfolios / O(2^n)
    portfolios = get_all_combinations(actions_data)

    # Filter portfolios witch total value is under MAXIMUM_PURCHASE_VALUE / O(2^n)
    portfolios_under_max_cost = [portfolio for portfolio in portfolios if
                                 get_portfolio_cost(portfolio) <= MAXIMUM_PURCHASE_COST]

    # Sort them by total benefit /  O(n*log(n))
    portfolios_under_max_cost_sorted = sorted(portfolios_under_max_cost,
                                              key=lambda x: get_portfolio_benefit_ptc(x) * get_portfolio_cost(x),
                                              reverse=True)

    # Best portfolio / O(1)
    return portfolios_under_max_cost_sorted[0]

    # Overall Complexity = O(n) + 2 * O(2^n) + O(n*log(n)) + O(1) => O(2^n)


if __name__ == '__main__':
    pass
