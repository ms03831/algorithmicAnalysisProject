import sys
from myMemory import *

def powerset(items):
    result = [[]]
    
    Memory.updateMemory(len(items))
    for item in items:
        newset = [r+[item]for r in result]
        result.extend(newset)
        
        Memory.updateMemory(len(result))
        Memory.updateMemory(len(newset))
        
    return result

def knapsack_brute_force(items, capacity):
    knapsack = []
    bestValue = 0
    
    Memory.updateMemory(len(items))
    output = ['0' for i in range(len(items))]
    
   
    powSet = powerset(items)
    
    Memory.updateMemory(len(powSet))
    
    for element in powSet:
        Memory.updateMemory(len(element)*2)
        
        setWeight = sum([e[1] for e in element])
        setValue = sum([e[2] for e in element])
        
        if setValue > bestValue and setWeight <= capacity:
            knapsack = element
    
    Memory.updateMemory(len(items))
    for i in range(0, len(items)):
        
        Memory.updateMemory(len(knapsack))
        if items[i] in knapsack:
            Memory.updateMemory(1)
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
    
