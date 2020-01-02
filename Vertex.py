class Vertex:
    number = 0
    weight = 0.0
    adjacents = []

    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
        self.adjacents = []

    def add_adjacent(self, vertex):
        self.adjacents.append(vertex)

    def __repr__(self):
        return str(self.number)
