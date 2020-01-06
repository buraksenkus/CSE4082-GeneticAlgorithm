import numpy
import random


class Chromosome:
    genes = None
    fitness = 0

    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def repair(self, graph):
        ''' numpy.where function finds indices of elements which have value of 0. So,
        it is enough to just looking their edges. '''
        flip_candidates = numpy.where(self.genes == 0)[0]
        while len(flip_candidates) > 0:
            flip_list = []
            index = random.randint(0, len(flip_candidates) - 1)  # Pick a random vertex from the list
            vertex = flip_candidates[index]
            if self.all_adjacents_one(vertex, graph):
                flip_candidates = numpy.setdiff1d(flip_candidates, numpy.array([vertex]))
            else:
                flip_list.append(vertex)  # Add this vertex to the flip list
                self.genes[vertex] = 1
                # Since all of this vertex's adjacents will be removed from flip_candidates list, we have to check all
                # and their adjacents as well
                for vertex1 in graph[vertex].adjacents:
                    if self.genes[vertex1] == 1:
                        continue
                    for vertex2 in graph[vertex1].adjacents:
                        if self.genes[vertex2] == 1:
                            continue
                        if len(graph[vertex1].adjacents) > len(graph[vertex2].adjacents) == 0:
                            flip_list.append(vertex1)
                            self.genes[vertex1] = 1
                            break
                        else:
                            flip_list.append(vertex2)
                            self.genes[vertex2] = 1
                # Remove vertices which will be flipped and adjacents of the base vertex
                removing = numpy.concatenate([numpy.array(graph[vertex].adjacents), numpy.array(flip_list)])
                flip_candidates = numpy.setdiff1d(flip_candidates, removing)

    def calculate_fitness(self, graph):
        self.fitness = 0
        indices_of_ones = numpy.where(self.genes == 1)[0]
        for index in indices_of_ones:
            vertex = graph[index]
            self.fitness += vertex.weight
        return self.fitness

    # Checks whether all of the adjacents of a vertex is 1
    def all_adjacents_one(self, vertex, graph):
        for adjacent in graph[vertex].adjacents:
            if self.genes[adjacent] == 0:
                return False
        return True

    # MWVCP is a minimization problem. So, it is needed to select low fitness with high prob.
    def get_selection_prob(self, mating_pool):
        return mating_pool.total_fitness / self.fitness
