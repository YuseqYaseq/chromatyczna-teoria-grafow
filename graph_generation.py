from typing import Optional
import networkx as nx
import numpy as np


def get_clique(n: int) -> nx.Graph:
    """
    Create a clique with n nodes
    :param n: number of nodes
    :return: generated graph
    """
    return nx.generators.complete_graph(n)


def get_cycle(n: int) -> nx.Graph:
    """
    Create a cycle with n nodes
    :param n: number of nodes
    :return: generated graph
    """
    return nx.generators.cycle_graph(n)


def get_random_tree(n: int, seed: Optional[int] = None) -> nx.Graph:
    """
    Create a random tree graph
    :param n: number of nodes in the tree
    :param seed: seed for the random number generator
    :return: generated graph
    """
    return nx.generators.trees.random_tree(n, seed)


def get_ba_graph(n: int, m: int, seed: Optional[int] = None) -> nx.Graph:
    """
    Create Barabasi-Albert graph.
    :param n: number of nodes
    :param m: number of edges to attach from a new node to existing nodes
    :param seed: seed for the random number generator
    :return: generated graph
    """
    return nx.generators.random_graphs.barabasi_albert_graph(n, m, seed)


def get_ws_graph(n: int, k: int, p: float, seed: Optional[int] = None) -> nx.Graph:
    """
    Returns a Watts–Strogatz small-world graph.
    :param n: The number of nodes
    :param k: Each node is joined with its k nearest neighbors in a ring topology.
    :param p: The probability of rewiring each edge
    :param seed: seed for the random number generator
    :return: generated graph
    """
    return nx.generators.watts_strogatz_graph(n, k, p, seed)


def get_random_n_graph(n: int, m_low: float, m_high: float, seed: Optional[int] = None) -> nx.Graph:
    """
    Generate random graph with n nodes and between m_low * n and m_high * n randomly assigned edges.
    :param n: Number of nodes
    :param m_low: at least int(m_low * n) edges will be created
    :param m_high: at most int(m_high * n) edges will be created
    :param seed: seed for the random number generator
    :return:
    """
    np.random.seed(seed)
    edges = np.random.randint(0, n, size=(np.random.randint(m_low * n, m_high * n), 2))
    return nx.Graph(edges.tolist())
