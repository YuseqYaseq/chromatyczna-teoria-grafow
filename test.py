from pathlib import Path
from typing import Union, Optional, List
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
from typing import Dict

from graph_generation import get_cycle, get_clique, get_ws_graph,\
    get_ba_graph, get_random_tree, get_random_n_graph
from algorithm import dsatur, largest_first, smallest_last, NoColoursRemainingException
from tqdm import tqdm
import yaml

from metrics import num_used_colours


class ParseError(SyntaxError):
    pass


class GraphsTestCasesIterator:
    """
    Iterates over all test cases provided in config_path and generates each graph.
    """
    def __init__(self, config_path: Union[str, Path], seed: Optional[int] = None):
        with open(config_path) as file:
            self.test_cases = yaml.safe_load(file)
            self.seed = seed

    def __len__(self):
        return len(self.test_cases)

    def __iter__(self):
        try:
            for test_case in self.test_cases:
                g_name = list(test_case.keys())[0]
                config = test_case[g_name]
                colours = config['colours']
                if g_name == 'cycle':
                    graph = get_cycle(config['n'])
                elif g_name == 'clique':
                    graph = get_clique(config['n'])
                elif g_name == 'tree':
                    graph = get_random_tree(config['n'], self.seed)
                elif g_name == 'ba':
                    graph = get_ba_graph(config['n'], config['m'], self.seed)
                elif g_name == 'ws':
                    graph = get_ws_graph(config['n'], config['k'], config['p'], self.seed)
                elif g_name == 'random_n_graph':
                    graph = get_random_n_graph(config['n'], config['m_low'], config['m_high'], self.seed)
                else:
                    raise ParseError(f'Unknown graph {g_name}')
                yield g_name, graph, colours
        except KeyError as e:
            raise ParseError(str(e))


def are_results_correct(g: nx.Graph, m: List[int], result: Dict[int, int]):
    """
    Verifies that graph colouring results are correct
    :param g: graph
    :param m: colouring thresholds
    :param result: algorithm results
    :return: True if results are correct; False otherwise
    """
    # check that the colouring is correct
    for n in g.nodes:
        neighbours = g.neighbors(n)
        for neighbour in neighbours:
            if result[n] == result[neighbour]:
                return False

    # check that less than len(m) colours were used
    possible_colours = len([i for i in m if i > 0])
    used_colours = num_used_colours(result)
    if used_colours > possible_colours:
        return False

    # check that m thresholds are satisfied
    for colour, threshold in enumerate(m):
        used_c = len([i for i in result.values() if i == colour])
        if used_c > threshold:
            return False

    return True


def run_tests(test_cases_path: Union[str, Path], verbose: bool, seed: Optional[int] = None):

    results = {
        'algorithm': [],
        'time': [],
        'num_used_colours': [],
        'completed': [],
        'graph': [],
    }
    gen = GraphsTestCasesIterator(test_cases_path, seed)
    if verbose:
        gen = tqdm(gen)

    for g_name, g, m in gen:
        for f in [dsatur, largest_first, smallest_last]:
            try:
                results['graph'].append(g_name)
                results['algorithm'].append(f.__name__)
                result, time = f(g, m)

                if verbose:
                    draw_graph(g, result)

                if not are_results_correct(g, m, result):
                    raise RuntimeError(f'Implementation of {f.__name__} failed on a graph {g_name} and mapping {m}')

                n_colours = num_used_colours(result)
                results['time'].append(time)
                results['completed'].append(True)
                results['num_used_colours'].append(n_colours)
            except NoColoursRemainingException:
                results['time'].append(None)
                results['completed'].append(False)
                results['num_used_colours'].append(None)
    return pd.DataFrame(results)


def draw_graph(g: nx.Graph, colouring: Dict[int, int]):
    colouring = dict(sorted(colouring.items()))
    sorted_g = nx.Graph()
    sorted_g.add_nodes_from(sorted(g.nodes(data=True)))
    sorted_g.add_edges_from(g.edges)
    colour_map = {i: c for i, c in enumerate(['blue', 'green', 'orange', 'red', 'purple', 'yellow'])}
    colouring = [colour_map[c] for i, c in colouring.items()]
    nx.draw_networkx(sorted_g, node_color=colouring)
    plt.show()
