# Imports
from typing import List, Dict, Any, Callable
from core.algorithms.bruteforce import bruteforce_algorithm as bf_algo
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy as greedy_algo
from core.algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic as dyn_algo
from core.algorithms.optimised_algorithm_dynamic_v2 import optimised_algorithm_dynamic_v2 as dyn_algo_v2
from core.algorithms.optimised_algorithm_dynamic_v3 import optimised_algorithm_dynamic_v3 as dyn_algo_v3
from core.algorithms.algorithm_tools import get_csv_data, get_time_func, get_ram_peak_func
from matplotlib import pyplot as plt

# CONSTANTS
ACTIONS_DATA_CSV = 'resources/Actions_data/Performance_data/data.csv'
ACTIONS_DATA = get_csv_data(ACTIONS_DATA_CSV)
# ANALYSIS
time = {'function': get_time_func, 'title': 'Time Performance Analysis', 'ylabel': 'Time (s)'}
ram = {'function': get_ram_peak_func, 'title': 'RAM Performance Analysis', 'ylabel': 'RAM Peak (MB)'}


def chart_performance_analysis(analysis: Dict[str, Any], algorithms: List[Callable], data_size: int = 20,
                               data_step: int = 1,
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


def performance_comparison(algorithm: Callable, data_size: int = 1000):
    """Function to compare results and performance of an algorithm vs dyn_algo"""

    # Init
    display = lambda x: print(f'''-----------------------------------
/// -- {x['algorithm_name']} -- //
-----------------------------------
Paramètre à maximiser : {x['parameter_to_maximize']}
Temps d'éxécution : {x['algorithm_durantion']}
RAM peak : {x['algorithm_RAM_peak']} MB
-----------------------------------''')

    # Dynamic algorithm details
    dyn_algo_results = {'algorithm_name': 'optimised_algorithm_dynamic',
                        'parameter_to_maximize': 245,
                        'algorithm_durantion': 2.43,
                        'algorithm_RAM_peak': 63.39}

    display(dyn_algo_results)

    # Compared algorithm details
    compared_algo_duration = get_time_func(algorithm)(actions=ACTIONS_DATA[:data_size])
    compared_algo_RAM_peak = get_ram_peak_func(algorithm)(actions=ACTIONS_DATA[:data_size])
    compared_algo_parameter_to_maximize = round(algorithm(actions=ACTIONS_DATA[:data_size]).parameter_to_maximize, 2)

    compared_algo_results = {'algorithm_name': algorithm.__name__,
                             'parameter_to_maximize': compared_algo_parameter_to_maximize,
                             'algorithm_durantion': compared_algo_duration,
                             'algorithm_RAM_peak': compared_algo_RAM_peak}

    display(compared_algo_results)

    print('===================================')

    comparison_results = {'algorithm_name': 'COMPARISON RESULTS',
                          'parameter_to_maximize': f"{round((compared_algo_results['parameter_to_maximize'] / dyn_algo_results['parameter_to_maximize'] - 1) * 100, 2)} %",
                          'algorithm_durantion': f"{round((compared_algo_results['algorithm_durantion'] / dyn_algo_results['algorithm_durantion'] - 1) * 100, 2)} %",
                          'algorithm_RAM_peak': f"{round((compared_algo_results['algorithm_RAM_peak'] / dyn_algo_results['algorithm_RAM_peak'] - 1) * 100, 2)} %"}

    display(comparison_results)
