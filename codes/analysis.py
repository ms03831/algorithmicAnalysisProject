from myTime import *
from myMemory import *
from MemoryFunctions import *
from greedyAlgo import *
from dynamic_programming import *
from bruteForceKnapsack import *
from SimulatedAnnealing import *
from geneticKnapsack import *
import matplotlib.pyplot as plt
import random

class TestCases:
    def __init__(self):
        self.n = [10, 25, 50, 100, 500, 1000, 2000, 3000, 4000, 5000, 10000]
        self.testsVaryingCapacity = dict()
        self.testsConstantCapacity = dict()
        self.__generateTests()

    def __generateTests(self, constant_weight = 1):
        for numberItems in self.n:
            self.testsVaryingCapacity[numberItems] = [
                [(i, random.randint(1, 2 + int(numberItems / 10)), random.randint(1, 2 + int(numberItems / 5)))
                 for i in range(numberItems)],
                random.randint(max(int(numberItems / 10), 20), max(int(numberItems / 5), 100))]
            self.testsConstantCapacity[numberItems] = [
                [(i, random.randint(1, 2 + int(numberItems / 10)), random.randint(1, 2 + int(numberItems / 5)))
                 for i in range(numberItems)], constant_weight]


class Analyze:
    def __init__(self):
        self.functions = [Memory_Function, greedyAlgo, knapsack01_dp, annealing_algorithm, GeneticKnapsack().solve]
        self.names = ["Memory Functions", "Greedy Algo", "DP", "Randomized Algorithm", "Genetic Knapsack"]
        self.tests = TestCases()
        self.timeAnalyzer = MyTime()
        self.memoryAnalyzer = Memory()

    def analyze(self, varyingCapacity = 1):
        times = [[] for i in range(len(self.functions))]
        memories = [[] for i in range(len(self.functions))]
        size = []
        if varyingCapacity:
            cases = self.tests.testsVaryingCapacity
            for n in cases:
                print(n, "here")
                size.append(n)
                test_case  = cases[n]
                for i in range(len(self.functions)):
                    func = self.functions[i]
                    self.timeAnalyzer.start()
                    try:
                        func(test_case[0], test_case[1])
                    except RecursionError:
                        print("Skipping")
                    self.timeAnalyzer.stop()
                    times[i].append(self.timeAnalyzer.elapsedTime)
                    self.timeAnalyzer.reset()
                    memories[i].append(Memory.memoryFootprint)
                    Memory.resetMemory()

        print(size, times, memories)
        for i in range(len(self.functions)):
            plt.plot(size, times[i], label = self.names[i])
        plt.legend()
        plt.show()




Analyze().analyze()

