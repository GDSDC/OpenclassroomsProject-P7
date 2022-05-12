# Imports
from typing import List, Dict, Any, Callable
from algorithms.bruteforce import bruteforce_algorithm as bt
from algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy as greedy
from algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic as dyn
from algorithms.algorithm_tools import get_csv_data, get_time_func, get_ram_peak_func
from matplotlib import pyplot as plt

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Performance_data/data.csv'
ACTIONS_DATA = get_csv_data(ACTIONS_DATA_CSV)
# ANALYSIS
time = {'function': get_time_func, 'title': 'Time Performance Analysis', 'ylabel': 'Time (s)'}
ram = {'function': get_ram_peak_func, 'title': 'RAM Performance Analysis', 'ylabel': 'RAM Peak (MB)'}


def performance_analysis(analysis: Dict[str, Any], algorithms: List[Callable], data_size: int = 20, data_step: int = 1,
                         xscale: str = 'linear'):
    """Function that return a plot with performance of the algorithms"""

    # Init
    data_number = list(range(5, data_size + 1, data_step))
    results = {}
    for algorithm in algorithms:
        results[algorithm.__name__] = []
    analysis_function = analysis['function']

    # Iteration
    for algorithm in algorithms:
        for n in data_number:
            results[algorithm.__name__].append(analysis_function(algorithm)(actions=ACTIONS_DATA[:n]))

    # Plotting
    for algorithm in algorithms:
        plt.plot(data_number, results[algorithm.__name__])

    # Plot Formatting
    plt.ylabel(analysis['ylabel'])
    plt.xlabel('number of data entries (n)')
    plt.title(f'{analysis["title"]} - n={data_size}')
    plt.legend([algorithm.__name__ for algorithm in algorithms])
    plt.grid()
    plt.xscale = xscale
    plt.show()
