import numpy
import random


class Chromosome:
    genes = None
    fitness = 0

    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def is_feasible(self, graph):
        flip_list = []
        ''' numpy.where function finds indices of elements which have value of 0. So,
        it is enough to just looking their edges. '''
        flip_candidates = numpy.where(self.genes == 0)[0]
        while len(flip_candidates) > 0:
            index = random.randint(0, len(flip_candidates) - 1)  # Pick a random vertex from the list
            vertex = flip_candidates[index]
            if self.all_adjacents_one(vertex, graph, flip_list):
                flip_candidates = numpy.setdiff1d(flip_candidates, numpy.array([vertex]))
            else:
                flip_list.append(vertex)  # Add this vertex to the flip list
                # Since all of this vertex's adjacents will be removed from flip_candidates list, we have to check all
                # and their adjacents as well
                for vertex1 in graph[vertex].adjacents:
                    if flip_list.__contains__(vertex1):
                        continue
                    for vertex2 in graph[vertex1].adjacents:
                        if flip_list.__contains__(vertex2):
                            continue
                        if self.genes[vertex1] == 0 and self.genes[vertex2] == 0:
                            random_for_flip = random.randint(0, 1)
                            if random_for_flip == 0:
                                flip_list.append(vertex1)
                                break
                            else:
                                flip_list.append(vertex2)
                # Remove vertices which will be flipped and adjacents of the base vertex
                removing = numpy.concatenate([numpy.array(graph[vertex].adjacents), numpy.array(flip_list)])
                flip_candidates = numpy.setdiff1d(flip_candidates, removing)
        return flip_list

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

    # Checks whether all of the adjacents of a vertex is 1 or will be 1
    def all_adjacents_one(self, vertex, graph, flip_list):
        for adjacent in graph[vertex].adjacents:
            if self.genes[adjacent] == 0 and not flip_list.__contains__(adjacent):
                return False
        return True

    # MWVCP is a minimization problem. So, it is needed to select low fitness with high prob.
    def get_selection_prob(self, mating_pool):
        return mating_pool.total_fitness / self.fitness
