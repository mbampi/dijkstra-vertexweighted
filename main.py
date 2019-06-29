from graph_v2 import *


def get_line_input():
    #return a list with input values
    return list(map(int, input().split(" ")))

def check_size(l , n):
    if(len(l) != n):
        raise KeyError('tamanho incompativel')

def create_vertices(graph,weights,n):
    for i in range(0,n):
        graph.add_vertex(i,weights[i])
    
def edge2graph(graph,n):
    for i in range(0,n):
        pass




def create_graph(n):
    graph = Graph()
    v_weights = get_line_input()
    check_size(v_weights,n)
    create_vertices(graph,v_weights,n)
    print(graph.get_vertices())
    #edge2graph(graph,n)

 


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    print("Problema dos Caminhos Mínimos de Fonte única com Pesos nos Vértices e nas Arestas")

    n = int(input())
    target_vertices = get_line_input()    
    create_graph(n)