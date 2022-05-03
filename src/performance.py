# Imports
from algorithms.bruteforce import get_best_portfolio as bt_algo
from algorithms.optimised_algorithm_v1 import get_best_portfolio as ov1_algo
from algorithms.optimised_algorithm_v1_2 import get_best_portfolio as ov2_algo
from algorithms.optimised_algorithm_v1_3 import get_best_portfolio as ov3_algo
from algorithms.algorithm_tools import get_time_func
import matplotlib.pyplot as plt
import math

# CONSTANTS
ACTIONS_DATA = 'resources/Actions_data/Performance_data'
INPUT = [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# Functions
def o_nlogn_exemple(n):
    """Function to simulate O(nlog(n)) function"""
    # TODO : code the right function
    a = []
    for i in range(n):
        a.append(i)


def o_n2_exemple(n):
    """Function to simulate O(n^2) function"""
    # TODO : code the right function
    a = []
    for i in range(n):
        for j in range(n):
            a.append(j)


def algorithm_time_performance_graph(algorithm, title):
    """Function that return a plot with time performance of the algorithm function in argument"""

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
