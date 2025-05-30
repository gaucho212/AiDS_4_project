import random


def generate_non_hamilton(nodes):
    edges = []
    # Generowanie cyklu Hamiltona
    vertices = list(range(1, nodes + 1))
    random.shuffle(vertices)
    for i in range(len(vertices) - 2):
        u, v = vertices[i], vertices[i + 1]
        edges.append((u, v))

    disconnected_vertex = vertices[-1]

    max_edges = nodes * (nodes - 1) // 2
    target_edges = int(max_edges * 0.5)

    all_possible_edges = [
        (i, j) for i in range(1, nodes + 1) for j in range(i + 1, nodes + 1)
    ]
    for edge in edges:
        if edge in all_possible_edges:
            all_possible_edges.remove(edge)
        elif edge[::-1] in all_possible_edges:
            all_possible_edges.remove(edge[::-1])

    filtered_edges = []
    for edge in all_possible_edges:
        if disconnected_vertex not in edge:
            filtered_edges.append(edge)
    all_possible_edges = filtered_edges

    random.shuffle(all_possible_edges)

    while len(edges) < target_edges:
        for u, v in all_possible_edges[:]:
            edges.append((u, v))
            all_possible_edges.remove((u, v))
            if (v, u) in all_possible_edges:
                all_possible_edges.remove((v, u))
    return edges
