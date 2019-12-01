import math
import random
from myMemory import *
ALPHA = 2.5




def annealing_algorithm(list_of_tuples, capacity, init_temp=100, steps=100):
    Memory.updateMemory(len(list_of_tuples))
    weight_cost = [(i[1], i[2]) for i in list_of_tuples]
    number = len(list_of_tuples)
    start_sol = init_solution(weight_cost, capacity)
    best_cost, solution = simulate(start_sol, weight_cost, capacity, init_temp, steps)
    Memory.updateMemory(number)
    best_combination = [0] * number
    list_of_selected = []
    Memory.updateMemory(len(solution))
    for idx in solution:
        list_of_selected.append(list_of_tuples[idx][0])
    return list_of_selected


def init_solution(weight_cost, max_weight):
    """Used for initial solution generation.
    By adding a random item while weight is less max_weight
    """
    solution = []
    Memory.updateMemory(len(weight_cost))
    allowed_positions = list(range(len(weight_cost)))
    while len(allowed_positions) > 0:
        idx = random.randint(0, len(allowed_positions) - 1)
        Memory.updateMemory(1)
        selected_position = allowed_positions.pop(idx)
        if get_cost_and_weight_of_knapsack(solution + [selected_position], weight_cost)[1] <= max_weight:
            solution.append(selected_position)
        else:
            break
    return solution


def get_cost_and_weight_of_knapsack(solution, weight_cost):
    """Get cost and weight of knapsack - fitness function
    """
    cost, weight = 0, 0
    for item in solution:
        Memory.updateMemory(2)
        weight += weight_cost[item][0]
        cost += weight_cost[item][1]
    return cost, weight


def moveto(solution, weight_cost, max_weight):
    """All possible moves are generated"""
    moves = []
    for idx, _ in enumerate(weight_cost):
        Memory.updateMemory(len(solution))
        if idx not in solution:
            Memory.updateMemory(len(solution))
            move = solution[:]
            Memory.updateMemory(1)
            move.append(idx)
            if get_cost_and_weight_of_knapsack(move, weight_cost)[1] <= max_weight:
                Memory.updateMemory(1)
                moves.append(move)
    for idx, _ in enumerate(solution):
        Memory.updateMemory(len(solution))
        move = solution[:]
        Memory.updateMemory(1)
        del move[idx]
        Memory.updateMemory(len(moves))
        if move not in moves:
            Memory.updateMemory(1)
            moves.append(move)
    return moves


def simulate(solution, weight_cost, max_weight, init_temp, steps):
    """Simulated annealing approach for Knapsack problem"""
    temperature = init_temp

    best = solution
    best_cost = get_cost_and_weight_of_knapsack(solution, weight_cost)[0]

    current_sol = solution
    while True:
        current_cost = get_cost_and_weight_of_knapsack(best, weight_cost)[0]

        for i in range(0, steps):
            moves = moveto(current_sol, weight_cost, max_weight)
            idx = random.randint(0, len(moves) - 1)
            Memory.updateMemory(1)
            random_move = moves[idx]
            delta = get_cost_and_weight_of_knapsack(random_move, weight_cost)[0] - best_cost
            if delta > 0:
                best = random_move
                best_cost = get_cost_and_weight_of_knapsack(best, weight_cost)[0]
                current_sol = random_move
            else:
                if math.exp(delta / float(temperature)) > random.random():
                    current_sol = random_move

        temperature *= ALPHA
        if current_cost >= best_cost or temperature <= 0:
            break
    return best_cost, best


if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    tuples = [(i, wt[i], val[i]) for i in range(len(val))]
    print(annealing_algorithm(tuples, w))