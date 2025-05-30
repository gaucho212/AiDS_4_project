import math
from hamilton_gen import generate_hamilton
from non_hamilton_gen import generate_non_hamilton


def graph_to_tikz(edges, nodes, radius=3.0):

    header = (
        "% Generated TikZ graph\n"
        "\\documentclass{article}\n"
        "\\begin{document}\n"
        "\\begin{tikzpicture}[>=stealth', shorten >=1pt, auto, node distance=2cm]\n"
    )

    coords = {}
    nodes_defs = []
    for i in range(1, nodes + 1):
        angle = 2 * math.pi * (i - 1) / nodes
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        coords[i] = (x, y)
        nodes_defs.append(f"\\node (N{i}) at ({x:.2f},{y:.2f}) {{{i}}};")

    edges_defs = []
    for u, v in edges:
        edges_defs.append(f"\\draw (N{u}) -- (N{v});")

    footer = "\\end{tikzpicture}\n" "\\end{document}"

    tikz_code = [header] + nodes_defs + edges_defs + [footer]
    return "\n".join(tikz_code)


def export_tikz(edges, nodes, radius=3.0):
    """
    Write the TikZ code for a graph to a .tex file.

    Parameters:
        filename (str): Output .tex file path.
        edges (list of tuple): Graph edges.
        nodes (int): Number of vertices.
        radius (float): Radius for node placement.
    """
    tikz = graph_to_tikz(edges, nodes, radius)
    with open("grapf.tex", "w+") as f:
        f.write(tikz)
    print(f"TikZ code exported to {"grapf.tex"}")
