class Vertex:
    number = 0
    weight = 0.0
    adjacents = {}

    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
        self.adjacents = {}

    def add_adjacent(self, vertex):
        self.adjacents[vertex] = 1

    def is_adjacent_with(self, vertex):
        return vertex in self.adjacents

    def is_better_than(self, graph, vertex):
        if len(graph[self.number].adjacents) > len(graph[vertex].adjacents):
            return True
        elif len(graph[self.number].adjacents) == len(graph[vertex].adjacents) and graph[self.number].weight < graph[vertex].weight:
            return True
        return False

    # Checks whether all of the adjacents of a vertex is 1
    def all_adjacents_one(self, chromosome, graph):
        for adjacent in graph[self.number].adjacents:
            if chromosome.genes[adjacent] == 0:
                return False
        return True

    def __repr__(self):
        return str(self.number)
