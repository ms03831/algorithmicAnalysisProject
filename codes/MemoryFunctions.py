"""
Given weights and values of n items, put these items in a knapsack of
 capacity W to get the maximum total value in the knapsack.
Note that only the integer weights 0-1 knapsack problem is solvable
 using dynamic programming.
"""
import sys
from myMemory import *
sys.setrecursionlimit(3000)

def Memory_Function(list_of_tuples, total_capacity):
    """
    :param list_of_tuples: a list of tuples(item,weight,value)
    :param total_capacity: the capacity of the sack
    :return: knapsack,a list of items in the sack
    """
    Memory.updateMemory(len(list_of_tuples) * 3) ## as we constructed 3 lists of len(list of tuples)
    item_names = [i[0] for i in list_of_tuples]
    item_wt = [i[1] for i in list_of_tuples]
    item_cost = [i[2] for i in list_of_tuples]
    n = len(list_of_tuples)
    F = [[0] * (total_capacity + 1)] + [[0] + [-1 for i in range(total_capacity + 1)] for j in range(n + 1)]
    Memory.updateMemory(len(F) * len(F[0])) #total entries in matrix
    (MF_knapsack(n, item_wt, item_cost, total_capacity, F))
    #print(F, "F")
    optimal_set = set()
    i = total_capacity
    j = n
    _construct_solution(F, item_wt, j, i, optimal_set)
    solution = []
    for i in optimal_set:
        Memory.updateMemory(1)
        solution.append(item_names[i-1])
    return solution


def MF_knapsack(i, wt, val, j, F):
    """
    This code involves the concept of memory functions. Here we solve the subproblems which are needed
    unlike the below example
    F is a 2D array with -1s filled up
    """
    Memory.updateMemory(1) # 1 access to memory F[i][j]
    if F[i][j] < 0:
        Memory.updateMemory(1) #wt[i-1]
        if j < wt[i - 1]:
            val = MF_knapsack(i - 1, wt, val, j, F)
        else:
            Memory.updateMemory(1) #val[i-1]
            val = max(
                MF_knapsack(i - 1, wt, val, j, F),
                MF_knapsack(i - 1, wt, val, j - wt[i - 1], F) + val[i - 1]
            )
        Memory.updateMemory(1)
        F[i][j] = val
    return F[i][j]


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights
    Parameters
    ---------
    dp: list of list, the table of a solved integer weight dynamic programming problem
    wt: list or tuple, the vector of weights of the items
    i: int, the index of the  item under consideration
    j: int, the current possible maximum weight
    optimal_set: set, the optimal subset so far. This gets modified by the function.
    Returns
    -------
    None
    """
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        Memory.updateMemory(2) #d[i-1][j], dp[i][j]
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            Memory.updateMemory(2) #addition on set and wt[i-1]
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)

if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    tuples = [(i, wt[i], val[i]) for i in range(len(val))]
    print(Memory_Function(tuples, w))
