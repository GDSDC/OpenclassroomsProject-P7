# Imports
from typing import List, Dict, Any, Callable
from algorithms.bruteforce import bruteforce_algorithm as bf_algo
from algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy as greedy_algo
from algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic as dyn_algo
from algorithms.optimised_algorithm_dynamic_v2 import optimised_algorithm_dynamic_v2
from algorithms.optimised_algorithm_dynamic_v3 import optimised_algorithm_dynamic_v3
from algorithms.algorithm_tools import get_csv_data, get_time_func, get_ram_peak_func
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


def performance_comparison(algorithm: Callable):
    """Function to compare results and performance of an algorithm vs dyn_algo"""

    # Init
    data_size: int = 1000
    display = lambda x: print(f'''-----------------------------------
/// -- {x['algorithm_name']} -- //
-----------------------------------
Valeur après 2 ans : {x['value_after_two_years']}
Temps d'éxécution : {x['algorithm_durantion']}
RAM peak : {x['algorithm_RAM_peak']} MB
-----------------------------------''')

    # Dynamic algorithm details
    dyn_algo_results = {'algorithm_name': 'optimised_algorithm_dynamic',
                        'value_after_two_years': 745,
                        'algorithm_durantion': 2.92,
                        'algorithm_RAM_peak': 63.67}

    display(dyn_algo_results)

    # Compared algorithm details
    compared_algo_duration = get_time_func(algorithm)(actions=ACTIONS_DATA[:data_size])
    compared_algo_RAM_peak = get_ram_peak_func(algorithm)(actions=ACTIONS_DATA[:data_size])
    compared_algo_value_after_two_year = algorithm(actions=ACTIONS_DATA[:data_size]).value_after_two_years

    compared_algo_results = {'algorithm_name': algorithm.__name__,
                             'value_after_two_years': compared_algo_value_after_two_year,
                             'algorithm_durantion': compared_algo_duration,
                             'algorithm_RAM_peak': compared_algo_RAM_peak}

    display(compared_algo_results)

    print('===================================')

    comparison_results = {'algorithm_name': 'COMPARISON RESULTS',
                          'value_after_two_years': f"{round((compared_algo_results['value_after_two_years'] / dyn_algo_results['value_after_two_years'] - 1) * 100,2)} %",
                          'algorithm_durantion': f"{round((compared_algo_results['algorithm_durantion'] / dyn_algo_results['algorithm_durantion'] - 1) * 100,2)} %",
                          'algorithm_RAM_peak': f"{round((compared_algo_results['algorithm_RAM_peak'] / dyn_algo_results['algorithm_RAM_peak'] - 1) * 100,2)} %"}

    display(comparison_results)