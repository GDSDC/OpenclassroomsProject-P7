from core.model import Action, Portfolio
from core.algorithms.algorithm_tools import display_portfolio, get_csv_data

ACTIONS_1_CSV_PATH = 'resources/backtesting_data/dataset1_PythonP7.csv'
ACTIONS_2_CSV_PATH = 'resources/backtesting_data/dataset2_PythonP7.csv'
ACTIONS_1 = get_csv_data(ACTIONS_1_CSV_PATH)
ACTIONS_2 = get_csv_data(ACTIONS_2_CSV_PATH)

result_1_actions_name = ['Share-GRUT']
result_2_actions_name = ['Share-ECAQ', 'Share-IXCI', 'Share-FWBE', 'Share-ZOFA', 'Share-PLLK', 'Share-YFVZ',
                         'Share-ANFX', 'Share-PATS', 'Share-NDKR', 'Share-ALIY', 'Share-JWGF', 'Share-JGTW',
                         'Share-FAPS', 'Share-VCAX', 'Share-LFXB', 'Share-DWSK', 'Share-XQII', 'Share-ROOM']

portfolio_1_result = Portfolio(actions=[action for action in ACTIONS_1 if action.name in result_1_actions_name])
portfolio_2_result = Portfolio(actions=[action for action in ACTIONS_2 if action.name in result_2_actions_name])
