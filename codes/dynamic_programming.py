from myMemory import *

def knapsack01_dp(items, limit):
    n= len(items)
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]
    Memory.updateMemory(n**2) # created 2-D list
    for j in range(1, len(items) + 1):
        Memory.updateMemory(1)
        item, wt, val = items[j-1]
        for w in range(1, limit + 1):
            if wt > w:
                Memory.updateMemory(1)  # 1 access to table memory
                table[j][w] = table[j-1][w]
            else:
                Memory.updateMemory(2)  # 2 access for comparing 2 table values
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        Memory.updateMemory(1) # 1 access to table memory on each iteration
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            Memory.updateMemory(1)
            item, wt, val = items[j-1]
            Memory.updateMemory(1) # each append takes access to memory
            result.append(item)
            # result.append(items[j-1])
            w -= wt
 
    return result

"""
items = [("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10)]

bagged = knapsack01_dp(items, 400)
print(bagged)
"""