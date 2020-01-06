import numpy
import random


class Chromosome:
    genes = None
    fitness = 0

    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def is_feasible(self, graph):  # TODO: Burası tam doğru değil. 0 olanların komuşlarına bakılacak......
        indices_to_be_flipped = []
        ''' numpy.where function finds indices of elements which have value of 0. So,
        it is enough to just looking their edges. '''
        indices_of_zeros = numpy.where(self.genes == 0)[0]
        while len(indices_of_zeros) > 0:
            index = random.randint(0, len(indices_of_zeros) - 1)  # Pick a random vertex from the list
            vertex = indices_of_zeros[index]
            indices_to_be_flipped.append(vertex)  # Add this vertex to the flip list
            # Remove vertex and its adjacents from the zero list
            indices_of_zeros = numpy.setdiff1d(indices_of_zeros, numpy.concatenate([numpy.array([vertex]), numpy.array(graph[vertex].adjacents)]))
        return indices_to_be_flipped

    def repair(self, indices_to_be_flipped):  # Flips the bits which specified in indices_to_be_flipped
        for index in indices_to_be_flipped:
            self.genes[index] = 1

    def calculate_fitness(self, graph):
        self.fitness = 0
        indices_of_ones = numpy.where(self.genes == 1)[0]
        for index in indices_of_ones:
            vertex = graph[index]
            self.fitness += vertex.weight
        return self.fitness

    def all_adjacents_one(self, vertex, graph):
        for adjacent in graph[vertex].adjacents:
            if self.genes[adjacent.number] == 0:
                return False
        return True

    # MWVCP is a minimization problem. So, it is needed to select low fitness with high prob.
    def get_selection_prob(self, mating_pool):
        return mating_pool.total_fitness / self.fitness # TODO
