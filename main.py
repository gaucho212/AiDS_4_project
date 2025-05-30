from representation import AdjacencyList
from hamilton_gen import generate_hamilton
from non_hamilton_gen import generate_non_hamilton
from hamilton_cycle import hamilton_cycle
from euler_cycle import fleury
import sys


def main():
    # Sprawdzenie, czy dane wejściowe pochodzą z heredoc
    is_heredoc = not sys.stdin.isatty()

    # Funkcja zastępcza dla input() w przypadku heredoc
    def silent_input(prompt=""):
        if is_heredoc:
            return sys.stdin.readline().strip()
        else:
            return input(prompt)

    if "--hamilton" in sys.argv:
        while True:
            try:
                nodes = int(silent_input("Nodes> "))
                if nodes < 10:
                    if not is_heredoc:
                        print("Insert correct amount of nodes greater than 10")
                    continue
                break
            except ValueError:
                if not is_heredoc:
                    print("Please enter a valid integer for nodes.")

        while True:
            try:
                saturation = int(silent_input("Saturation(30 or 70)> "))
                if saturation not in [30, 70]:
                    if not is_heredoc:
                        print("Insert correct value of saturation: 30 or 70")
                    continue
                break
            except ValueError:
                if not is_heredoc:
                    print("Please enter a valid integer for saturation.")

        edges = generate_hamilton(nodes, saturation)
        graph = AdjacencyList(nodes)

    elif "--non-hamilton" in sys.argv:
        while True:
            try:
                nodes = int(silent_input("Nodes> "))
                if nodes < 10:
                    if not is_heredoc:
                        print("Insert correct amount of nodes greater than 10")
                    continue
                break
            except ValueError:
                if not is_heredoc:
                    print("Please enter a valid integer for nodes.")

        edges = generate_non_hamilton(nodes)
        graph = AdjacencyList(nodes)

    else:
        nodes = 4
        saturation = 70
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        graph = AdjacencyList(nodes)

    for edge in edges:
        u, v = edge
        graph.add(u, v)

    while True:
        try:
            cmd = silent_input("action> ").strip().lower()
            if cmd == "print":
                graph.display()
            elif cmd == "hamilton":
                print(f"Hammilton cycle: {hamilton_cycle(graph)}")
            elif cmd == "euler":
                start = 1
                print(f"Euler cycle: {fleury(graph, start)}")
            elif cmd == "exit":
                if not is_heredoc:
                    print("Exiting..")
                break
            else:
                if not is_heredoc:
                    print("Unknown command. Try again.")
        except EOFError:
            sys.stdin = open("/dev/tty")
            continue


if __name__ == "__main__":
    main()
