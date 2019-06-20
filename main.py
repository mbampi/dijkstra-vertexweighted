from graph import *


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

