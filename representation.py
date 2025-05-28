class AdjacencyList:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[] for _ in range(size + 1)]

    def add(self, u, v):
        self.adj_list[u].append(v)

    def display(self):
        for i in range(1, len(self.adj_list)):
            print(f"{i}: {self.adj_list[i]}")
