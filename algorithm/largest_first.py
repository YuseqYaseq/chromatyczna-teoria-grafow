import networkx as nx
from typing import Dict, List
import numpy as np
from algorithm.no_colours_remaining_exception import NoColoursRemainingException
from metrics import timer


@timer
def largest_first(graph: nx.Graph, m: List[int]) -> Dict[int, int]:
    """
    Largest First colouring algorithm
    :param graph: graph
    :param m: mapping of available number of each colour
    :return: mapping node->colour
    :raises NoColoursRemainingException: when m threshold couldn't be achieved
    """

    max_c = len(m)-1
    nodes = list(graph.nodes)
    ct = {}
    cv = np.zeros(len(m))
    vt = []
    dt = []
    for i in range(len(nodes)):
        vt.append(i)
        dt.append(len([u for u in graph.neighbors(nodes[i])]))
        d = dt[i]
        j = i
        while j > 0 and dt[j] < d:
            dt[j] = dt[j - 1]
            vt[j] = vt[j - 1]
            j -= 1
        vt[j] = i
        dt[j] = d

    ct[nodes[vt[0]]] = 0
    cv[0] = 1

    for i in range(1, len(vt)):
        c = {}
        for u in graph.neighbors(nodes[vt[i]]):
            if u in ct:
                c[ct[u]] = True
        color = 0
        while color in c or cv[color] >= m[color]:
            color += 1
            if color > max_c:
                raise NoColoursRemainingException
        ct[nodes[vt[i]]] = color
        cv[color] += 1

    return ct
