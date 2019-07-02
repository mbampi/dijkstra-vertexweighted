from graph import *


# Python 3.7

def get_line_input():
    # return a list with input values
    return list(map(int, input().split(" ")))


def check_size(l, n):
    # raise key error if input size is incompatible
    if len(l) != n:
        raise KeyError('tamanho incompativel')


def create_vertices(graph, weights, n):
    # create n vertices using a list of indexed weights
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
    # get the cli input
    graph = Graph()
    v_weights = get_line_input()
    check_size(v_weights, n)
    create_vertices(graph, v_weights, n)
    edge2graph(graph, n)

    return graph


def generate_output(result, target_vertices, w):
    output = ""

    for tv in target_vertices:
        output += str(result[tv - 1] + w) + " "
    return output


# ------------------------------------------------------------------------------------------------------------------- #
# Python 3.7

if __name__ == '__main__':
    print("Problema dos Caminhos Minimos de Fonte unica com Pesos nos Vertices e nas Arestas")
    n = int(input())
    target_vertices = get_line_input()
    graph = input2graph(n)
    # print(graph)
    res = dijkstra(graph)
    w = graph.get_source_weight()
    out = generate_output(res, target_vertices, w)
    print(out)
