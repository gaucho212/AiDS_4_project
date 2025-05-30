import random


def generate_hamilton(n, density):
    # Tworzy cykl hamiltona
    edges = []
    vertices = list(range(1, n + 1))
    random.shuffle(vertices)
    for i in range(n):
        edges.append((vertices[i], vertices[(i + 1) % n]))

    total_possible_edges = n * (n - 1) // 2
    target_edges = int(total_possible_edges * (density / 100))
    current_edges = len(edges)
    existing_edges = set(edges)

    # Liczy stopnie wierzchołków
    degrees = {v: 0 for v in vertices}
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    while current_edges < target_edges:
        # Wybiera trzy losowe wierzchołki do utworzenia trójkąta
        u, v, w = random.sample(vertices, 3)
        if (
            (u, v) not in existing_edges
            and (v, u) not in existing_edges
            and (v, w) not in existing_edges
            and (w, v) not in existing_edges
            and (w, u) not in existing_edges
            and (u, w) not in existing_edges
        ):
            edges.append((u, v))
            edges.append((v, w))
            edges.append((w, u))
            existing_edges.add((u, v))
            existing_edges.add((v, u))
            existing_edges.add((v, w))
            existing_edges.add((w, v))
            existing_edges.add((w, u))
            existing_edges.add((u, w))
            degrees[u] += 2
            degrees[v] += 2
            degrees[w] += 2
            current_edges += 3

    # Sprawdza czy stopnie wszystkich wierzchołków są parzyste
    for node in vertices:
        if degrees[node] % 2 != 0:
            # Dodaje krawędź od wierzchołka o stopniu nieparzystym do losowego wierzchołka
            potential_nodes = []
            for v in vertices:
                if v != node and (node, v) not in existing_edges:
                    potential_nodes.append(v)
            if potential_nodes:
                chosen = random.choice(potential_nodes)
                edges.append((node, chosen))
                existing_edges.add((node, chosen))
                existing_edges.add((chosen, node))
                degrees[node] += 1
                degrees[chosen] += 1

    return edges
