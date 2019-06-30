from graph_v2 import *


def get_line_input():
    # return a list with input values
    return list(map(int, input().split(" ")))


def check_size(l, n):
    if len(l) != n:
        raise KeyError('tamanho incompativel')


def create_vertices(graph, weights, n):
    for i in range(0, n):
        graph.add_vertex(i, weights[i])


def edge2graph(graph, n):
    vertices = graph.get_vertices_raw()
    for vertex in vertices:
        edge_weight = get_line_input()
        check_size(edge_weight, n)
        pos = 0  # position counter
        for weight in edge_weight:
            if weight != -1:
                graph.add_edge([vertex, vertices[pos]], weight)
            pos = pos + 1


def input2graph(n):
    graph = Graph()
    v_weights = get_line_input()
    check_size(v_weights, n)
    create_vertices(graph, v_weights, n)
    edge2graph(graph, n)

    return graph


def generate_output(result, target_vertices):
    output = ""
    for tv in target_vertices:
        output += str(res[tv - 1]) + " "
    return output


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    print("Problema dos Caminhos Mínimos de Fonte única com Pesos nos Vértices e nas Arestas")
    n = int(input())
    target_vertices = get_line_input()
    graph = input2graph(n)
    # print(graph)
    (path, res) = dijkstra(graph)
    out = generate_output(res, target_vertices)
    print(out)

