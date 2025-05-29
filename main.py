from representation import AdjacencyList
from hamilton_gen import Hamilton
from non_hamilton_gen import Non_Hamilton
from hamilton_cycle import hamilton_cycle
from euler_cycle import fleury
import sys


def main():
    is_heredoc = sys.stdin.isatty()
    if "--hamilton" in sys.argv:
        nodes = int(input("Nodes> "))
        saturation = int(input("Saturation(30 or 70)> "))
        edges = Hamilton.generate(nodes, saturation)
        graph = AdjacencyList(nodes)
        print(edges)

    elif "--non-hamilton" in sys.argv:
        nodes = int(input("Nodes> "))
        edges = Non_Hamilton.generate(nodes)
        graph = AdjacencyList(nodes)

    else:
        nodes = 4
        saturation = 70
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        graph = AdjacencyList(nodes)

    for edge in edges:
        u, v = edge
        graph.add(u, v)

    sys.stdin = open("/dev/tty")

    while True:
        cmd = input("action> ").strip().lower()
        if cmd == "print":
            graph.display()
        if cmd == "hamilton":
            print(f"Hammilton cycle: {hamilton_cycle(graph)}")
        elif cmd == "euler":
            start = int(input("insert starting node> "))
            print(f"Euler cycle: {fleury(graph, start)}")

        elif cmd == "exit":
            print("Koniec programu")
            break


if __name__ == "__main__":
    main()
