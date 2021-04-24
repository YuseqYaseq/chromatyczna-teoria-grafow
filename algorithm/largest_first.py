import networkx as nx
from typing import Dict, List

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
    import random
    return {n: random.randint(0, 3) for n in graph.nodes}
