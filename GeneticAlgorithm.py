import numpy as np
from Chromosome import Chromosome
from Vertex import Vertex


class GeneticAlgorithm:
    file = ""
    generations = 0
    population_size = 0
    crossover_prob = 0.0
    mutation_prob = 0.0
    population = []
    CROSSOVER_POINT = 500
    number_of_nodes = 0
    number_of_edges = 0
    graph = []

    def __init__(self, file, generations, population_size, crossover_prob, mutation_prob):
        self.generations = generations
        self.population_size = population_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.population = []
        try:
            with open(file) as fp:
                for i, line in enumerate(fp):
                    if i == 0:  # Reading number of vertices
                        try:
                            self.number_of_nodes = int(line.strip())
                        except ValueError:
                            print("First line of the input file must specify the number of vertices!")
                            exit(0)
                    elif i == 1:  # Reading number of edges
                        try:
                            if "." in line:
                                self.number_of_edges = int(line.strip().split(".")[0])
                            elif "," in line.strip():
                                self.number_of_edges = int(line.strip().split(",")[0])
                            else:
                                self.number_of_edges = int(line.strip())
                        except ValueError:
                            print("Second line of the input file must specify the number of edges!")
                            exit(0)
                    elif self.number_of_nodes + 2 > i >= 2:  # Reading vertices and their weights
                        tokens = line.strip().split(" ")
                        if "," in tokens[1]:
                            value = str(tokens[1]).replace(",", ".")
                        self.graph.append(Vertex(i-2, float(value)))
                    else:  # Reading edges
                        vertices = line.strip().split(" ")
                        first_vertex = self.graph[int(vertices[0])]
                        second_vertex = int(vertices[1])
                        first_vertex.add_adjacent(second_vertex)
        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

    def create_initial_population(self):
        for i in range(0, self.population_size):
            array = np.random.randint(2, size=1000)
            self.population.append(Chromosome(array))

    def crossover(self, parent1, parent2):  # TODO........
        print()

    def repair_all(self):
        for chromosome in self.population:
            indices_to_be_flipped = chromosome.is_feasible(self.graph)
            if len(indices_to_be_flipped) > 0:
                chromosome.repair(indices_to_be_flipped)

    def run(self):
        self.create_initial_population()
        for i in range(0, self.generations):
            self.repair_all()
