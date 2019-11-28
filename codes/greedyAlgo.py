def greedyAlgo(weightValue,capacity):
    """
    :param weightValue: a list of tuples(item,weight,value)
    :param capacity: the capacity of the sack
    :return: knapsack,a list of items in the sack
    """
    ratios_weight_value = []
    ratios_index = list(range(len(weightValue)))
    knapsack =[]
    for i in range(len(weightValue)):
        ratios_weight_value.append(weightValue[i][2]/weightValue[i][1])  #taking out value to weight ratio
    ratios_index.sort(key=lambda i: ratios_weight_value[i], reverse=True)  #keeping track of the ratio indexes after sorting

    for i in ratios_index:    #going to the index with max ratio first
        if weightValue[i][1] <= capacity:
            capacity -= weightValue[i][1]
            knapsack.append(weightValue[i][0])
    return knapsack



print(greedyAlgo([("a",10,60),("b",40,40),("c",20,100),("d",30,120)],50))

