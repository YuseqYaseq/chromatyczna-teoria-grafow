import networkx as nx
from typing import List, Dict

from algorithm.no_colours_remaining_exception import NoColoursRemainingException
from metrics import timer


@timer
def dsatur(graph: nx.Graph, m: List[int]) -> Dict[int, int]:
    """
    DSatur colouring algorithm
    :param graph: graph
    :param m: mapping of available number of each colour
    :return: mapping node->colour
    :raises NoColoursRemainingException: when m threshold couldn't be achieved
    """

    def argmax_dsat(g: nx.Graph):
        max_ = []
        v_ = -1
        for n in g.nodes:
            if c[n] == -1:
                neighbours = g.neighbors(n)
                unique_colours_ = {c[i] for i in neighbours}
                if len(unique_colours_) > len(max_):
                    max_ = unique_colours_
                    v_ = n
        return v_, max_

    c_max = len([i for i in m if i > 0]) - 1
    c = {n: -1 for n in graph.nodes}
    while -1 in c.values():
        v, neighbour_colors = argmax_dsat(graph)
        for i in range(0, c_max + 1):
            if i not in neighbour_colors and len([j for j in c.values() if j == i]) < m[i]:
                c[v] = i
                break
            if i == c_max:
                raise NoColoursRemainingException()
    return c
