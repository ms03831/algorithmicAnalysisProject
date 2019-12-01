from myMemory import *

def greedyAlgo(weightValue,capacity):
    """
    :param weightValue: a list of tuples(item,weight,value)
    :param capacity: the capacity of the sack
    :return: knapsack,a list of items in the sack
    """
    ratios_weight_value = []
    Memory.updateMemory(1)
    ratios_index = list(range(len(weightValue)))
    Memory.updateMemory(len(weightValue))
    knapsack =[]
    Memory.updateMemory(1)

    for i in range(len(weightValue)):
        ratios_weight_value.append(weightValue[i][2]/weightValue[i][1])  #taking out value to weight ratio
        Memory.updateMemory(1)
    ratios_index.sort(key=lambda i: ratios_weight_value[i], reverse=True)  #keeping track of the ratio indexes after sorting
    Memory.updateMemory(len(weightValue)) # for sort

    for i in ratios_index:    #going to the index with max ratio first
        Memory.updateMemory(1)
        if weightValue[i][1] <= capacity:
            Memory.updateMemory(2)
            capacity -= weightValue[i][1]
            knapsack.append(weightValue[i][0])
    return knapsack



