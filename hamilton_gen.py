import random
from representation import AdjacencyList


class Hamilton(AdjacencyList):
    def generate(nodes, saturation):
        edges = []
        nodes_degree = {i: 0 for i in range(1, nodes + 1)}

        # Generowanie cyklu Hamiltona
        vertices = list(range(1, nodes + 1))
        random.shuffle(vertices)
        for i in range(len(vertices) - 1):
            u, v = vertices[i], vertices[i + 1]
            nodes_degree[u] += 1
            nodes_degree[v] += 1
            edges.append((u, v))
        # Zamknięcie cyklu
        u, v = vertices[-1], vertices[0]
        nodes_degree[u] += 1
        nodes_degree[v] += 1
        edges.append((u, v))

        # Obliczanie maksymalnej liczby krawędzi i docelowej liczby krawędzi
        max_edges = nodes * (nodes - 1) // 2
        target_edges = int(max_edges * (saturation / 100))

        # Lista wszystkich możliwych krawędzi
        all_possible_edges = [
            (i, j) for i in range(1, nodes + 1) for j in range(i + 1, nodes + 1)
        ]
        for edge in edges:
            if edge in all_possible_edges:
                all_possible_edges.remove(edge)
            elif edge[::-1] in all_possible_edges:
                all_possible_edges.remove(edge[::-1])

        random.shuffle(all_possible_edges)

        # Dodawanie krawędzi z priorytetem dla wierzchołków o nieparzystych stopniach
        while len(edges) < target_edges:
            odd_degree_vertices = [v for v in nodes_degree if nodes_degree[v] % 2 == 1]
            if len(odd_degree_vertices) >= 2:
                for u in odd_degree_vertices:
                    for v in odd_degree_vertices:
                        if u != v and (u, v) in all_possible_edges:
                            edges.append((u, v))
                            nodes_degree[u] += 1
                            nodes_degree[v] += 1
                            all_possible_edges.remove((u, v))
                            if (v, u) in all_possible_edges:
                                all_possible_edges.remove((v, u))
                            break
                    else:
                        continue
                    break
            else:
                for u, v in all_possible_edges[:]:
                    if len(edges) >= target_edges:
                        break
                    edges.append((u, v))
                    nodes_degree[u] += 1
                    nodes_degree[v] += 1
                    all_possible_edges.remove((u, v))
                    if (v, u) in all_possible_edges:
                        all_possible_edges.remove((v, u))

        return edges
