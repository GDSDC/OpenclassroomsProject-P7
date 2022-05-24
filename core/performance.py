# Imports
from typing import List, Dict, Any, Callable
from core.algorithms.bruteforce import bruteforce_algorithm as bf_algo
from core.algorithms.optimised_algorithm_greedy import optimised_algorithm_greedy as greedy_algo
from core.algorithms.optimised_algorithm_dynamic import optimised_algorithm_dynamic as dyn_algo
from core.algorithms.optimised_algorithm_dynamic_v2 import optimised_algorithm_dynamic_v2 as dyn_algo_v2
from core.algorithms.algorithm_tools import get_csv_data, get_time_func, get_ram_peak_func
from core.model import Portfolio, MAXIMUM_PURCHASE_COST
from matplotlib import pyplot as plt

# CONSTANTS
ACTIONS_DATA_CSV_PATH = 'resources/Actions_data/Performance_data/data.csv'
ACTIONS = get_csv_data(ACTIONS_DATA_CSV_PATH)
# ANALYSIS
time = {'function': get_time_func, 'title': 'Time Performance Analysis', 'ylabel': 'Time (s)'}
ram = {'function': get_ram_peak_func, 'title': 'RAM Performance Analysis', 'ylabel': 'RAM Peak (MB)'}


def chart_performance_comparison(analysis: Dict[str, Any], algorithms: List[Callable], data_size: int = 20,
                                 data_step: int = 1):
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
            results[algorithm.__name__].append(analysis_function(algorithm)(actions=ACTIONS[:n]))

    # Plotting
    for algorithm in algorithms:
        plt.plot(data_number, results[algorithm.__name__])

    # Plot Formatting
    plt.ylabel(analysis['ylabel'])
    plt.xlabel('number of data entries (n)')
    plt.title(f'{analysis["title"]} - n={data_size}')
    plt.legend([algorithm.__name__ for algorithm in algorithms])
    plt.grid()
    plt.show()


def chart_performance_analysis(algorithm: Callable, data_size: int = 20,
                               data_step: int = 1):
    """Function that return a plot with performance of the algorithms"""

    # Init
    data_number = list(range(5, data_size + 1, data_step))
    time_results = []
    delta_results = []

    # Iteration
    for n in data_number:
        time_results.append(get_time_func(algorithm)(actions=ACTIONS[:n]))
        # delta_n is the difference in percentage for parameter_to_maximize between algorithm and dyn_algo
        a1 = algorithm(actions=ACTIONS[:n])
        a2 = dyn_algo(actions=ACTIONS[:n])
        delta_n = - (a1.parameter_to_maximize /
                     a2.parameter_to_maximize - 1) * 100
        delta_results.append(delta_n)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(data_number, time_results, color='green')
    ax.set_xlabel('number of data entries (n)', fontsize=14)
    ax.set_ylabel('time (s)', color='green', fontsize=14)
    ax.set_ylim(ymin=0, ymax=max(time_results) if max(time_results) != 0 else None)
    ax.legend(['time'], loc='lower center')

    ax2 = ax.twinx()
    ax2.plot(data_number, delta_results, color='red')
    ax2.set_ylabel('delta (%)', color='red', fontsize=14)
    ax2.legend(['delta'], loc='lower right')

    # Plot Formatting
    plt.title(f'Performance Analysis - n = {data_size} \n{algorithm.__name__}')
    plt.grid()
    plt.show()


def dyn_algo_v2_step_performance_analysis(data_size: int = 1000, algo_max_step: int = 5,
                                          algo_min_step: int = 1, step: int = 1):
    """Function that return time and delta performance for differents algo_step"""

    # Init
    algo_steps = list(range(algo_min_step, algo_max_step + 1, step))
    time_results = []
    delta_results = []
    a2 = dyn_algo(actions=ACTIONS[:data_size])

    # Iteration
    for step in algo_steps:
        time_results.append(get_time_func(dyn_algo_v2)(actions=ACTIONS[:data_size], step=step))
        # delta_n is the difference in percentage for parameter_to_maximize between algorithm and dyn_algo
        a1 = dyn_algo_v2(actions=ACTIONS[:data_size], step=step)
        delta_n = - (a1.parameter_to_maximize /
                     a2.parameter_to_maximize - 1) * 100
        delta_results.append(delta_n)

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(algo_steps, time_results, color='green')
    ax.set_xlabel('Algorithm Step Value', fontsize=14)
    ax.set_ylabel('time (s)', color='green', fontsize=14)
    ax.set_ylim(ymin=0, ymax=max(time_results) if max(time_results) != 0 else None)
    ax.set_xlim(xmin=algo_min_step)
    ax.legend(['time'], loc='lower center')
    ax.grid(axis="x")

    ax2 = ax.twinx()
    ax2.plot(algo_steps, delta_results, color='red')
    ax2.set_ylabel('delta (%)', color='red', fontsize=14)
    ax2.legend(['delta'], loc='lower right')
    ax2.grid(axis="y")

    # Plot Formatting
    plt.title(
        f'Algorithm Step Performance Analysis - n = {data_size} - '
        f'fonds = {MAXIMUM_PURCHASE_COST} \n{dyn_algo_v2.__name__}')
    plt.xticks(list(range(algo_min_step, algo_max_step + 1)))
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
                        'algorithm_durantion': 2.92,
                        'algorithm_RAM_peak': 108.53}

    display(dyn_algo_results)

    # Compared algorithm details
    compared_algo_duration = get_time_func(algorithm)(actions=ACTIONS[:data_size])
    compared_algo_ram_peak = get_ram_peak_func(algorithm)(actions=ACTIONS[:data_size])
    compared_algo_parameter_to_maximize = round(
        algorithm(actions=ACTIONS[:data_size]).parameter_to_maximize, 2)

    compared_algo_results = {'algorithm_name': algorithm.__name__,
                             'parameter_to_maximize': compared_algo_parameter_to_maximize,
                             'algorithm_durantion': compared_algo_duration,
                             'algorithm_RAM_peak': compared_algo_ram_peak}

    display(compared_algo_results)

    print('===================================')

    comparison_results = {'algorithm_name': 'COMPARISON RESULTS',
                          'parameter_to_maximize': f"{round((compared_algo_results['parameter_to_maximize'] / dyn_algo_results['parameter_to_maximize'] - 1) * 100, 2)} %",
                          'algorithm_durantion': f"{round((compared_algo_results['algorithm_durantion'] / dyn_algo_results['algorithm_durantion'] - 1) * 100, 2)} %",
                          'algorithm_RAM_peak': f"{round((compared_algo_results['algorithm_RAM_peak'] / dyn_algo_results['algorithm_RAM_peak'] - 1) * 100, 2)} %"}

    display(comparison_results)
