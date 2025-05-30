import random


def generate_hamilton(n, density):
    """
    Generates a list of edges for a graph with a Hamiltonian cycle and a given edge density.
    Additional edges are added as triangles (cycles of 3 vertices) to vertices with odd degrees.

    Parameters:
        n (int): Number of vertices (must be greater than 10).
        density (int): Desired edge density as a percentage (e.g., 70 for 70%).

    Returns:
        list[tuple]: A list of edges representing the graph.
    """
    if n <= 10:
        raise ValueError("Number of vertices must be greater than 10.")

    if not (30 <= density <= 70):
        raise ValueError("Density must be between 30 and 70 (as a percentage).")

    # Step 1: Create a Hamiltonian cycle
    edges = []
    vertices = list(range(1, n + 1))  # Start vertices from 1 instead of 0
    for i in range(n):
        edges.append((vertices[i], vertices[(i + 1) % n]))

    # Step 2: Add additional edges as triangles to achieve the desired density
    total_possible_edges = n * (n - 1) // 2
    target_edges = int(
        total_possible_edges * (density / 100)
    )  # Correct density calculation
    current_edges = len(edges)
    existing_edges = set(edges)

    # Calculate initial degrees
    degrees = {v: 0 for v in vertices}
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    while current_edges < target_edges:
        # Randomly select 3 distinct vertices
        u, v, w = random.sample(vertices, 3)
        if (
            (u, v) not in existing_edges
            and (v, u) not in existing_edges
            and (v, w) not in existing_edges
            and (w, v) not in existing_edges
            and (w, u) not in existing_edges
            and (u, w) not in existing_edges
        ):
            # Add the edges of the triangle
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

    # Step 3: Ensure all vertex degrees are even
    for node in vertices:
        if degrees[node] % 2 != 0:
            # Add an edge to another random node to make the degree even
            potential_nodes = [
                v for v in vertices if v != node and (node, v) not in existing_edges
            ]
            if potential_nodes:
                chosen = random.choice(potential_nodes)
                edges.append((node, chosen))
                existing_edges.add((node, chosen))
                existing_edges.add((chosen, node))
                degrees[node] += 1
                degrees[chosen] += 1

    return edges
