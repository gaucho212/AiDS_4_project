# Prof's Review: I would explicitly declare an abstract graph representation with following functions:
# add_edge()
# check_edge()
# get_next_vertices() -> Best if it returns an GraphIterator class object
# print_graph()
# Zasada Dependency Inversion Principle from SOLID


class AdjacencyList:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[] for _ in range(size + 1)]

    def add(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        for i in range(1, len(self.adj_list)):
            print(f"{i}: {self.adj_list[i]}")
