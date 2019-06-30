from graph_old import *


class Graph2:

    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, v, w):
        self.vertices[v] = w

    def add_vertices(self, v_list):
        self.vertices = v_list

    def add_edge(self, v1, v2, w):
        self.edges[v1][v2] = w
        self.edges[v2][v1] = w

    def add_edges(self, v, e_dict):
        self.edges[v] = e_dict

    def add_edges(self, e_list):
        self.edges = e_list

    def get_vertices(self):
        return self.vertices

    def get_adjacent_of(self, v):
        return self.edges[v]

    def __str__(self):
        for v, w in enumerate(self.vertices):
            print(str(v) + '(' + str(w) + ')' + " -> " + str(self.edges[v]))

    def dijkstra(self, initial):
        visited = {initial: 0}
        path = defaultdict(list)

        nodes = set(self.vertices)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None: # min_node -> vertice com menor distancia da fonte
                break  # se min_node ta vazio eh porque acabou
            nodes.remove(min_node)  # remove da lista dos vertices a serem visitados
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = current_weight + self.edges[min_node] + self.vertices[edge]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(min_node)
        return path, visited


def input_vertices():
    v = []
    vertices_weights = input().split(" ")
    vertices_weights = list(map(int, vertices_weights))
    for i in range(n):
        v.append(vertices_weights[i])
    return v


def input_adj(num_vertices):
    adj = defaultdict(list)
    for e in range(num_vertices):
        edge_weights = input().split(" ")
        edge_weights = list(map(int, edge_weights))
        for i, w in enumerate(edge_weights):
            if w != -1:
                adj[e].append({i: w})
    return adj


# -------------------------------------------------------------------------------------------------------------------- #


print("Problema dos Caminhos Mínimos de Fonte única com Pesos nos Vértices e nas Arestas")

n = int(input())
target_vertices = list(map(int, input().split(" ")))
vertices = input_vertices()
adj_list = input_adj(n)

print("vertice (weight) -> [neighbor: weight]")
for v, w in enumerate(vertices):
    print(str(v) + '(' + str(w) + ')' + " -> " + str(adj_list[v]))

g = Graph2()
g.add_vertices(vertices)
g.add_edges(adj_list)

print("adj")
adj = g.get_adjacent_of(1)
print(adj)
print(adj.__getitem__(0).keys())
print(adj.__getitem__(1))

print("A: ")
print(g.__str__())
