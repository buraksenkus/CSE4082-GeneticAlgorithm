from Chromosome import Chromosome
import numpy as np
import random


class MatingPool:
    size = 0
    population = []
    total_fitness = 0

    def __init__(self, size):
        self.size = size
        self.population = []
        self.total_fitness = 0

    def create_initial_population(self):
        for i in range(0, self.size):
            array = np.random.randint(2, size=1000)
            self.population.append(Chromosome(array))

    def get_total_selection_prob(self):
        total_selection_prob = 0
        for chromosome in self.population:
            total_selection_prob += chromosome.get_selection_prob(self)
        return total_selection_prob

    # Each chromosome has a selection prob. and this func. creates new population by these probabilities
    def select_pool_by_probabilities(self):
        new_population = []
        for i in range(0, self.size):
            value = random.random() * self.get_total_selection_prob()  # A random value for selection
            prob_range = 0
            for chromosome in self.population:
                prob_range += chromosome.get_selection_prob(self)
                if prob_range >= value:  # If we are in correct region, select it
                    new_population.append(chromosome)
                    break
        self.population = new_population

    def crossover(self, crossover_prob):
        index = 0
        while index <= len(self.population) - 2:
            value = random.random()  # A random value for crossover
            if value <= crossover_prob:  # Crossover will be made
                crossover_point = random.randint(1, len(self.population[index].genes) - 2)
                parent1_1 = self.population[index].genes[:crossover_point]
                parent1_2 = self.population[index].genes[crossover_point:]
                parent2_1 = self.population[index + 1].genes[:crossover_point]
                parent2_2 = self.population[index + 1].genes[crossover_point:]
                offspring_1 = np.concatenate([parent1_1, parent2_2])
                offspring_2 = np.concatenate([parent2_1, parent1_2])
                self.population[index].genes = offspring_1
                self.population[index + 1].genes = offspring_2
            index += 2

    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):
            if arr[j].get_selection_prob(self) > pivot.get_selection_prob(self):
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def repair(self, graph):
        self.total_fitness = 0
        for i in range(0, len(self.population)):
            # if i % 50 == 0:
            #     print("Chromosome", i)
            chromosome = self.population[i]
            chromosome.repair(graph)
            self.total_fitness += chromosome.calculate_fitness(graph)

    def mutate(self, mutation_prob):
        for chromosome in self.population:
            for i in range(len(chromosome.genes)):
                value = random.random()  # a random value for each bit of each chromosome that to compare mutation probability
                if value < mutation_prob:  # if random value is smaller than mutation probability flip bit
                    # flip bit
                    if chromosome.genes[i] == 0:
                        chromosome.genes[i] = 1
                    else:
                        chromosome.genes[i] = 0
