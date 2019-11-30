import random


class GeneticKnapsack:
    def __init__(self):
        self.populationSize = 250
        self.generations = 10
        self.items = [[i, random.randint(0, 10),random.randint(0, 15)] for i in range(10)]
        self.capacity = 20


    def fitness(self, target):
        total_value = 0
        total_weight = 0
        index = 0
        for i in target:        
            if index >= len(self.items):
                break
            if (i == 1):
                total_value += self.items[index][1]
                total_weight += self.items[index][2]
            index += 1
            
        if total_weight > self.capacity:
            return 0
        else:
            return total_value

    def spawn_starting_population(self):
        return [self.spawn_individual() for x in range (0, self.populationSize)]

    def spawn_individual(self):
        return [random.randint(0,1) for x in range (0,len(self.items))]

    def mutate(self, target):
        """
        Changes a random element of the permutation array from 0 -> 1 or from 1 -> 0.
        """ 
        r = random.randint(0,len(target)-1)
        if target[r] == 1:
            target[r] = 0
        else:
            target[r] = 1

    def evolve_population(self, pop):
        parent_eligibility = 0.2
        mutation_chance = 0.08
        parent_lottery = 0.05

        parent_length = int(parent_eligibility*len(pop))
        parents = pop[:parent_length]
        nonparents = pop[parent_length:]

        # Parent lottery!
        for np in nonparents:
            if parent_lottery > random.random():
                parents.append(np)

        # Mutation lottery... I guess?
        for p in parents:
            if mutation_chance > random.random():
                self.mutate(p)

        # Breeding! Close the doors, please.
        children = []
        desired_length = len(pop) - len(parents)
        while len(children) < desired_length :
            male = pop[random.randint(0,len(parents)-1)]
            female = pop[random.randint(0,len(parents)-1)]        
            half = len(male)//2
            child = male[:half] + female[half:] # from start to half from father, from half to end from mother
            if mutation_chance > random.random():
                self.mutate(child)
            children.append(child)

        parents.extend(children)
        return parents


if __name__ == "__main__":
    solver = GeneticKnapsack()
    generation = 1
    population = solver.spawn_starting_population()
    for g in range(0, solver.generations):
        print("Generation %d with %d" % (generation, len(population)))
        population = sorted(population, key=lambda x: solver.fitness(x), reverse=True)
        for i in population:        
            print("%s, fit: %s" % (str(i), solver.fitness(i)))      
        population = solver.evolve_population(population)
        generation += 1
