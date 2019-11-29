
def powerset(items):
    result = [[]]
    
    for item in items:
        newset = [r+[item]for r in result]
        result.extend(newset)
    return result

def knapsack_brute_force(items, capacity):
    knapsack = []
    best_value = 0
    output = ['0' for i in range(len(items))]
    
    for element in powerset(items):
        set_weight = sum([e[1] for e in element])
        set_value = sum([e[2] for e in element])
        if set_value > best_value and set_weight <= capacity:
    
            knapsack = element
            
    for i in range(0, len(items)):
        if items[i] in knapsack:
            output[i] = 1
    #print('l', output)
            
    return output

'''if __name__ == '__main__':
    n = 5
    data = build_items(n)
    output = ['0' for i in range(n)]
    max_w = 10
    output = knapsack_brute_force(data, max_w)
    print(output)'''
    