import random
from myMemory import *
from collections import Counter

class GeneticKnapsack:
    def __init__(self):
        self.populationSize = 100
        self.generations = 50
        self.items = None
        self.capacity = None

    def solve(self, items, capacity):
        self.items = items
        self.capacity = capacity
        generation = 1
        population = self.spawn_starting_population()
        
        Memory.updateMemory(2*self.generations) #for loop, and inside population is updated.

        for g in range(0, self.generations):
            #print("Generation %d with %d" % (generation, len(population)))
            population = sorted(population, key=lambda x: self.fitness(x), reverse=True)
            fitnesses = [self.fitness(x) for x in population]
            for i in fitnesses:
                if fitnesses.count(i) > 0.9 * len(population):
                    break
            #print('best score;', self.fitness(population[0]))     
            population = self.evolve_population(population)
            generation += 1

        Memory.updateMemory(self.populationSize)
        population = sorted(population, key=lambda x: self.fitness(x), reverse=True)
        Memory.updateMemory(2)
        #print(population[0], self.fitness(population[0]))
        return([items[i][0] for i in range(len(population[0])) if population[0][i]])

    def fitness(self, target):
        total_value = 0
        total_weight = 0
        index = 0
        Memory.updateMemory(len(target))
        for i in target:        
            if index >= len(self.items):
                break
            if (i == 1):
                Memory.updateMemory(2)
                total_value += self.items[index][2]
                total_weight += self.items[index][1]
            index += 1
            
        while total_weight > self.capacity:
            r = random.randint(0, len(target) - 1)
            if target[r] == 1:
                target[r] = 0
                total_weight -= self.items[r][1]
                total_value -= self.items[r][2]
        else:
            return total_value

    def spawn_starting_population(self):
        Memory.updateMemory(self.populationSize)
        return [self.spawn_individual() for x in range (0, self.populationSize)]

    def spawn_individual(self):
        Memory.updateMemory(len(self.items))
        return [random.randint(0,1) for x in range (0,len(self.items))]

    def mutate(self, target):
        """
        Changes a random element of the permutation array from 0 -> 1 or from 1 -> 0.
        """ 
        r = random.randint(0,len(target)-1)
        Memory.updateMemory(len(target))
        if target[r] == 1:
            target[r] = 0
        else:
            target[r] = 1
    '''
    def evolve_population(self, pop):
        parent_eligibility = 0.2
        mutation_chance = 0.1

        parent_length = int(parent_eligibility*len(pop))

        Memory.updateMemory(1) #slicing assumed to be O(1)
        parents = pop[:parent_length]

        # Breeding! Close the doors, please.
        children = []
        desired_length = len(pop) - len(parents)
        while len(children) < desired_length :
            Memory.updateMemory(6)
            male = pop[random.randint(0,len(parents)-1)]
            female = pop[random.randint(0,len(parents)-1)]        
            half = len(male)//2
            child = male[:half] + female[half:] # from start to half from father, from half to end from mother
            if mutation_chance > random.random():
                self.mutate(child)
            children.append(child)
        Memory.updateMemory(len(children))
        parents.extend(children)
        return parents
    '''
    def evolve_population(self, pop):
        parent_eligibility = 0.2
        mutation_chance = 0.1
        parent_lottery = 0.05

        parent_length = int(parent_eligibility*len(pop))

        Memory.updateMemory(2) #slicing assumed to be O(1)
        parents = pop[:parent_length]
        nonparents = pop[parent_length:]

        # Parent lottery!
        Memory.updateMemory(len(nonparents))
        for np in nonparents:
            if parent_lottery > random.random():
                Memory.updateMemory(1)
                parents.append(np)

        # Mutation lottery... I guess?
        Memory.updateMemory(len(parents))
        for p in parents:
            if mutation_chance > random.random():
                self.mutate(p)

        # Breeding! Close the doors, please.
        children = []
        desired_length = len(pop) - len(parents)
        while len(children) < desired_length :
            Memory.updateMemory(6)
            male = pop[random.randint(0,len(parents)-1)]
            female = pop[random.randint(0,len(parents)-1)]        
            half = len(male)//2
            child = male[:half] + female[half:] # from start to half from father, from half to end from mother
            if mutation_chance > random.random():
                self.mutate(child)
            children.append(child)
        Memory.updateMemory(len(children))
        parents.extend(children)
        return parents


'''
if __name__ == "__main__":
    solver = GeneticKnapsack()
    items = [[i, random.randint(0, 10),random.randint(0, 15)] for i in range(5)]
    capacity = 10
    print(items)
    solver.solve(items, capacity)
'''