def hamilton_cycle(graph):
    n = graph.size
    visited = [False] * (n + 1)
    path = [-1] * n
    start_vertex = 1

    def hamiltonian(v, visited_count):
        visited[v] = True
        path[visited_count - 1] = v
        visited_count += 1

        # Iteracja po sąsiadach wierzchołka v
        for neighbor in graph.adj_list[v]:
            # Jeśli odwiedzono wszystkie wierzchołki i wraca do startowego, mamy cykl
            if neighbor == start_vertex and visited_count == n + 1:
                return True
            if not visited[neighbor]:
                if hamiltonian(neighbor, visited_count):
                    return True

        # Cofanie (backtracking)
        visited[v] = False
        path[visited_count - 2] = -1
        return False

    # Rozpoczęcie przeszukiwania
    if hamiltonian(start_vertex, 1):
        path.append(start_vertex)
        return path
    else:
        return None
