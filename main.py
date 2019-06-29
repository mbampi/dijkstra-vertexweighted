from graph import *


def create_graph(n):
    v_weights = list(map(int, input().split(" ")))
    if(len(weights) != n):
        raise KeyError('tamanho incompativel')
    for i in range(0,n):
        

 


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    print("Problema dos Caminhos Mínimos de Fonte única com Pesos nos Vértices e nas Arestas")

    n = int(input())
    target_vertices = list(map(int, input().split(" ")))
    create_graph(n)

    print("vertice (weight) -> [neighbor: weight]")
    #for v, w in enumerate(vertices):
     #   print(str(v) + '(' + str(w) + ')' + " -> " + str(adj_list[v]))
    print(vertices)