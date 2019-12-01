from myTime import *
from myMemory import *
from MemoryFunctions import *
from greedyAlgo import *
from dynamic_programming import *
from bruteForceKnapsack import *
from SimulatedAnnealing import *
from geneticKnapsack import *
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np

sns.set_style("darkgrid", {"axes.facecolor": ".9", "lines.linewidth": 2.5})



class TestCases:
    def __init__(self):
        self.n = [10, 25, 50, 100, 500, 1000]#, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
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
        self.averageCase = None
        self.bestCase = None
        self.worstCase = None

    def analyze(self, varyingCapacity = 1):
        times = [[[] for i in range(len(self.functions))] for itr in range(10)]
        memories = [[[] for i in range(len(self.functions))] for itr in range(10)]
        size = list(TestCases().n)
       	for itr in range(10):
	        if varyingCapacity:
	            cases = self.tests.testsVaryingCapacity
	            for n in cases:
	                print(n, "here")
	                test_case  = cases[n]
	                for i in range(len(self.functions)):
	                    func = self.functions[i]
	                    self.timeAnalyzer.start()
	                    try:
	                        func(test_case[0], test_case[1])
	                    except RecursionError:
	                        print("Skipping")
	                    self.timeAnalyzer.stop()
	                    times[itr][i].append(self.timeAnalyzer.elapsedTime)
	                    self.timeAnalyzer.reset()
	                    memories[itr][i].append(Memory.memoryFootprint)
	                    Memory.resetMemory()
	
        times_ = dict()
        memories_ = dict()
       	for i, j in enumerate(self.functions):
       		times_[self.names[i]] = [times[itr][i] for itr in range(10)]
       		memories_[self.names[i]] = [memories[itr][i] for itr in range(10)]
       	
       	self.averageCaseTime = {i:[] for i in self.names}
        self.bestCaseTime = {i:[] for i in self.names}
        self.worstCaseTime = {i:[] for i in self.names}
        self.averageCaseMem = {i:[] for i in self.names}
        self.bestCaseMem = {i:[] for i in self.names}
        self.worstCaseMem = {i:[] for i in self.names}

       	for i, j in enumerate(self.functions):
       		self.averageCaseTime[self.names[i]] = np.mean(np.array(times_[self.names[i]]), axis=0)
       		self.bestCaseTime[self.names[i]] = np.min(np.array(times_[self.names[i]]), axis=0)
       		self.worstCaseTime[self.names[i]] = np.max(np.array(times_[self.names[i]]), axis=0)
       		self.averageCaseMem[self.names[i]] = np.mean(np.array(memories_[self.names[i]]), axis=0)
       		self.bestCaseMem[self.names[i]] = np.min(np.array(memories_[self.names[i]]), axis=0)
       		self.worstCaseMem[self.names[i]] = np.max(np.array(memories_[self.names[i]]), axis=0)


        for i in range(len(self.functions)):
            plt.plot(size, self.averageCaseTime[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Time: Average Case")
        plt.show()

        for i in range(len(self.functions)):
            plt.plot(size, self.worstCaseTime[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Time: Worst Case")
        plt.show()

        for i in range(len(self.functions)):
            plt.plot(size, self.bestCaseTime[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Time: Best Case")
        plt.show()

        for i in range(len(self.functions)):
            plt.plot(size, self.averageCaseMem[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Memory: Average Case")
        plt.show()

        for i in range(len(self.functions)):
            plt.plot(size, self.worstCaseMem[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Memory: Worst Case")
        plt.show()

        for i in range(len(self.functions)):
            plt.plot(size, self.bestCaseMem[self.names[i]], label = self.names[i])
        plt.legend()
        plt.title("Empirical Memory: Best Case")
        plt.show()

        



Analyze().analyze()

