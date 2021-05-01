import networkx as nx
from typing import Dict, List
import numpy as np
from algorithm.no_colours_remaining_exception import NoColoursRemainingException
from metrics import timer


@timer
def smallest_last(graph: nx.Graph, m: List[int]) -> Dict[int, int]:
    """
    Smallest Last colouring algorithm
    :param graph: graph
    :param m: mapping of available number of each colour
    :return: mapping node->colour
    :raises NoColoursRemainingException: when m threshold couldn't be achieved
    """
    max_c = len(m) - 1
    ct = {}
    cv = np.zeros(len(m))
    dv = []

    copy_G = graph.copy()
    while len(copy_G.nodes) > 0:
        min_d_node = list(copy_G.nodes)[0]
        min_d = copy_G.degree[min_d_node]
        for node in list(copy_G.nodes):
            if min_d > copy_G.degree[node]:
                min_d = copy_G.degree[node]
                min_d_node = node
        dv.append(min_d_node)
        copy_G.remove_node(min_d_node)

    for i in range(len(dv)-1, -1, -1):
        c = {}
        for u in graph.neighbors(dv[i]):
            if u in ct:
                c[ct[u]] = True
        color = 0
        while color in c or cv[color] >= m[color]:
            color += 1
            if color > max_c:
                raise NoColoursRemainingException
        ct[dv[i]] = color
        cv[color] += 1

    return ct
