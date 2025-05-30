from representation import AdjacencyList
import copy


# Liczy liczbe wierzchołków osiagalnych z danego wierzchołka
def dfs_count(v, visited, adj_list):
    visited[v] = True
    count = 1
    for neighbor in adj_list[v]:
        if not visited[neighbor]:
            count += dfs_count(neighbor, visited, adj_list)
    return count


# Sprawdza czy krawędź jest mostem
def is_bridge(u, v, adj_list, size):
    # Liczba wierzchołków osiągalnych przed usunięciem krawędzi
    visited = [False] * (size + 1)
    count1 = dfs_count(u, visited, adj_list)

    # Usuwa krawędź (u, v)
    adj_list[u].remove(v)
    adj_list[v].remove(u)

    # Liczba wierzchołków osiągalnych po usunięciu krawędzi
    visited = [False] * (size + 1)
    count2 = dfs_count(u, visited, adj_list)

    # Przywraca krawędź (u, v)
    adj_list[u].append(v)
    adj_list[v].append(u)

    return count1 > count2


# Sprawdza czy graf jest spójny
def is_connected(graph):
    visited = [False] * (graph.size + 1)
    start_vertex = -1

    for vertex in range(1, graph.size + 1):
        if len(graph.adj_list[vertex]) > 0:
            start_vertex = vertex
            break

    if start_vertex == -1:
        return True  # Graf bez krawędzi jest spójny

    # DFS od start_vertex
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for neighbor in graph.adj_list[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    # Sprawdza, czy wszystkie wierzchołki z krawędziami zostały odwiedzone
    for vertex in range(1, graph.size + 1):
        if len(graph.adj_list[vertex]) > 0 and not visited[vertex]:
            return False

    return True


def fleury(graph, start_vertex):

    # Sprawdza, czy graf ma cykl Eulera
    for vertex in range(1, graph.size + 1):
        degree = len(graph.adj_list[vertex])
        if degree % 2 != 0:
            return None  # Graf nie ma cyklu Eulera, jeśli którykolwiek wierzchołek ma nieparzysty stopień

    if not is_connected(graph):
        print("Graf nie jest spójny.")
        return None  # Graf nie ma cyklu Eulera, jeśli nie jest spójny

    # Tworzy kopię grafu
    adj_list_copy = copy.deepcopy(graph.adj_list)

    euler_cycle = []
    current_vertex = start_vertex
    # Znajduje cykl eulera
    while any(len(neighbors) > 0 for neighbors in adj_list_copy):
        for neighbor in adj_list_copy[current_vertex]:
            # Sprawdza, czy krawędź nie jest mostem lub jest jedyną krawędzią
            if len(adj_list_copy[current_vertex]) == 1 or not is_bridge(
                current_vertex, neighbor, adj_list_copy, graph.size
            ):
                euler_cycle.append(current_vertex)
                adj_list_copy[current_vertex].remove(neighbor)
                adj_list_copy[neighbor].remove(current_vertex)
                current_vertex = neighbor
                break

    euler_cycle.append(current_vertex)
    return euler_cycle
