from Vertex import Vertex
from MatingPool import MatingPool


class GeneticAlgorithm:
    file = ""
    generations = 0
    crossover_prob = 0.0
    mutation_prob = 0.0
    mating_pool = None
    CROSSOVER_POINT = 500
    number_of_nodes = 0
    number_of_edges = 0
    graph = []

    def __init__(self, file, generations, population_size, crossover_prob, mutation_prob):
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.mating_pool = MatingPool(population_size)
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

    def run(self):
        self.mating_pool.create_initial_population()
        for i in range(0, self.generations):
            self.mating_pool.repair(self.graph)
            self.mating_pool.quick_sort(self.mating_pool.population, 0, len(self.mating_pool.population) - 1)
            self.mating_pool.select_pool_by_probabilities()
            self.mating_pool.crossover(self.crossover_prob)
            self.mating_pool.mutate(self.mutation_prob)
