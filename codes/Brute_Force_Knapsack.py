from random import random

def build_items(n):
    res = []
    for i in range(0, n):
        res.append((i, 1 + int(9*random()), 1+int(9* random())))
    #print(res)
    return res
    
def powerset(items):
    res = [[]]
    
    for item in items:
        newset = [r+[item]for r in res]
        res.extend(newset)
    return res

def knapsack_brute_force(items, max_weight, output):
    knapsack = []
    best_weight = 0
    best_value = 0

    for item_set in powerset(items):
        set_weight = sum([e[1] for e in item_set])
        set_value = sum([e[2] for e in item_set])
        if set_value > best_value and set_weight <= max_weight:
            best_value = set_value
            best_weight = set_weight
            knapsack = item_set
            
    for i in range(0, len(items)):
        if items[i] in knapsack:
            output[i] = 1
    #print('l', output)
            
    return output, knapsack, best_weight, best_value

if __name__ == '__main__':
    n = 5
    data = build_items(n)
    output = ['0' for i in range(n)]
    max_w = 10
    output, kn, opt_w, opt_v = knapsack_brute_force(data, max_w, output)
    print(output)
    