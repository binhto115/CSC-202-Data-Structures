from __future__ import annotations
import sys


def is_two_colorable(edge_list: list[list[str]]) -> bool:
    """Determine if the given graph is two-colorable.

    The graph is specified as a list of edges, where each edge is a list
    of two vertices.  The result will be True if the given graph is two
    colorable, and False otherwise.

    Args:
        edge_list: the graph to analyze, given as a list of edges

    Returns:
        True if the given graph is two-colorable, False otherwise
    """
    adjacency_list = {}
    for lst in edge_list:
        if lst == []:
            return True
        edge1 = lst[0]
        edge2 = lst[1]
        if edge1 not in adjacency_list:
            adjacency_list[edge1] = []
        if edge2 not in adjacency_list:
            adjacency_list[edge2] = []
        adjacency_list[edge1].append(edge2)
        adjacency_list[edge2].append(edge1)

    colors = {}
    visited_neighbors = []

    for curr_vertex in adjacency_list:
        if curr_vertex not in visited_neighbors:
            colors[curr_vertex] = "Red"
            visited_neighbors.append(curr_vertex)
        for vertex in adjacency_list[curr_vertex]:
            if vertex not in visited_neighbors:
                if colors[curr_vertex] == "Red":
                    colors[vertex] = "Blue"
                elif colors[curr_vertex] == "Blue":
                    colors[vertex] = "Red"
                visited_neighbors.append(vertex)
            if colors[curr_vertex] == colors[vertex]:
                return False
    return True


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print("usage: python3 two_colorable.py <filename>", file=sys.stderr)
        sys.exit(1)

    with open(argv[1], encoding="utf8") as file:
        edge_list = [line.split() for line in file]

    print(is_two_colorable(edge_list))


if __name__ == "__main__":
    main(sys.argv)
