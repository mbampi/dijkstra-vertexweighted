from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges


def show_graph(g):
    gr = nx.Graph()
    gr.add_nodes_from(g.get_nodes())
    gr.add_edges_from(g.get_edges())
    nodes = ['a', 1, 'c', 'b', 'e', 'd', 2]
    edges = [("a", "c"), ("c", "d"), ("a", 1), (1, "d"), ("a", 2)]
    nx.draw(gr, node_color="red", with_labels=True)
    plt.show()


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)
    return path
