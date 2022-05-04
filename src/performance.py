# Imports
from algorithms.bruteforce import get_best_portfolio as bt_algo
from algorithms.optimised_algorithm_v1 import get_best_portfolio as ov1_algo
from algorithms.optimised_algorithm_v1_2 import get_best_portfolio as ov2_algo
from algorithms.optimised_algorithm_v1_3 import get_best_portfolio as ov3_algo
from algorithms.algorithm_tools import get_time_func, get_ram_peak_func
import matplotlib.pyplot as plt
import math

# CONSTANTS
ACTIONS_DATA = 'resources/Actions_data/Performance_data'
INPUT = [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]


def o_nlogn_exemple(n):
    """Function to simulate O(nlog(n)) function"""
    for i in range(n):  # O(n) iteration
        # O(log(n) algorithm
        # Create a list with n elements
        data = list(range(n))
        # Choose a value for worst case
        value = (len(data) - 1) - 1
        # Init
        left = 0
        right = len(data) - 1
        # Searching Loop
        while left <= right:
            middle = (left + right) // 2
            if value < data[middle]:
                right = middle - 1
            elif value > data[middle]:
                left = middle + 1
            else:
                return middle
        raise ValueError('Value is not in the list')


def o_n2_exemple(n):
    """Function to simulate O(n^2) function"""
    if n <= 1:
        return n
    return o_n2_exemple(n - 1) + o_n2_exemple(n - 2)


def algorithm_time_performance_graph(algorithm, title):
    """Function that return a plot with time performance of the algorithm"""

    # Init
    time_results_algorithm = []
    time_results_nlogn = []
    time_results_n2 = []

    # Iteration
    for n in INPUT:
        time_results_algorithm.append(get_time_func(algorithm)(ACTIONS_DATA + '/actions_data_' + str(n) + '.csv'))
        time_results_nlogn.append(get_time_func(o_nlogn_exemple)(n))
        time_results_n2.append(get_time_func(o_n2_exemple)(n))
    # Plot algorithm performance
    plt.plot(INPUT, time_results_algorithm)

    # Plot O(nlog(n))
    plt.plot(INPUT, time_results_nlogn)

    # Plot O(2^n)
    plt.plot(INPUT, time_results_n2)

    plt.ylabel('time')
    plt.xlabel('number of data entries')
    plt.title(title)
    plt.legend([title, 'O(nlog(n))', 'O(2^n)'])
    plt.show()

def algorithm_ram_peak_performance_graph(algorithm, title):
    """Function that return a plot with RAM peak performance of the algorithm"""

    # Init
    ram_peak_results_algorithm = []
    ram_peak_results_nlogn = []
    ram_peak_results_n2 = []

    # Iteration
    for n in INPUT:
        ram_peak_results_algorithm.append(get_ram_peak_func(algorithm)(ACTIONS_DATA + '/actions_data_' + str(n) + '.csv'))
        ram_peak_results_nlogn.append(get_ram_peak_func(o_nlogn_exemple)(n))
        ram_peak_results_n2.append(get_ram_peak_func(o_n2_exemple)(n))
    # Plot algorithm performance
    plt.plot(INPUT, ram_peak_results_algorithm)

    # Plot O(nlog(n))
    plt.plot(INPUT, ram_peak_results_nlogn)

    # Plot O(2^n)
    plt.plot(INPUT, ram_peak_results_n2)

    plt.ylabel('RAM peak (MB)')
    plt.xlabel('number of data entries')
    plt.title(title)
    plt.legend([title, 'O(nlog(n))', 'O(2^n)'])
    plt.show()