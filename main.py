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
    '''
    keys, values = graph.keys_values()
    print(keys)
    print('\n\n')
    values = list(values)
    print(values)
    print("value[0] = " + str(values[0]))
    print('\n')
    print("value[1] = " + str(values[1]))
    print('\n')
    print("value[2] = " + str(values[2]))
    print('\n')
    print("value[3] = " + str(values[3]))
    print('\n')
    print("value[4] = " + str(values[4]))'''


def input2graph(n):
    graph = Graph()
    v_weights = get_line_input()
    check_size(v_weights, n)
    create_vertices(graph, v_weights, n)
    edge2graph(graph, n)

    return graph


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    print("Problema dos Caminhos Mínimos de Fonte única com Pesos nos Vértices e nas Arestas")
    n = int(input())
    target_vertices = get_line_input()
    graph = input2graph(n)
    vertices = graph.get_vertices()
    print(graph.__str__())
    print("\nvertices= ")
    print(graph.get_vertices())
    print(dijkstra(graph, 0))
