def ask(graph, start):
    
    color = {}
    queue = []
    minor_age = 101
    flag = False

    # initialization
    for vertex in graph:
        color[vertex] = 'W'          # W = white | B = black | G = gray
        for adj in graph[vertex]:
            color[adj] = 'W'         # para os vertices que n possuem adj

    color[start] = 'G'
    
    # enqueuing the start vertex
    queue.append(start)

    u = None
    while queue:
        
        # dequeuing
        u = queue.pop(0)
        
        # print("u:", u)
        # print(graph)
        
        # traverse the list of adjacent vertices of the dequeued vertex
        for v in graph[u]:
            #print(graph[u])
            
            if color[v] == 'W':
                color[v] = 'G'

                if graph[u][v] < minor_age:
                    minor_age = graph[u][v]
                    flag = True

                queue.append(v)
                
        color[u] = 'B'

    #print("color:", color)

    if flag == False:
        minor_age = "*"
        print(minor_age)
    else:
        print(minor_age)



def change(graph, X, Y):
    '''
    O objetivo desta função é trocar os vértices X e Y de posição entre si em um grafo direcionado.
    Para tal, busca-se alterar tanto os vértices diretamente predecessores de X e Y quanto seus vértices diretamente adjacentes/subsequentes
    '''
    
    # Encontrando (onde? no grafo original) os predecessores do vértice X/Y no grafo invertido
    # por meio da lista de adj do vértice X/Y no grafo original
    pred_X = graph.graph[X].copy()         # graph.graph[X] é a lista de adj (um dict) do vértice X no grafo original
    adj_X = graph.graph_inverted[X].copy() # graph_inverted[X] é a lista de adj do vértice X no grafo invertido
    
    pred_Y = graph.graph[Y].copy()         # graph.graph[Y] é a lista de adj (um dict) do vértice Y no grafo original
    adj_Y = graph.graph_inverted[Y].copy() # graph_inverted[Y] é a lista de adj do vértice Y no grafo invertido

    # testando se estou obtendo o dict esperado
    print("--- obtendo o dict esperado? ---")
    print("pred_X: ", pred_X)
    print("pred_Y: ", pred_Y)
    
    print("adj_X: ", adj_X)
    print("adj_Y: ", adj_Y)

    
    # Troca X <---> Y no grafo Invertido
    print("--- troca no invertido pred ---")
    for v in pred_X:
        if X in graph.graph_inverted[v]:
            print("deletado: ", X, graph.graph_inverted[v][X])
            del graph.graph_inverted[v][X]
        print(f"L Adj de {v} sem X ({X}): ", graph.graph_inverted[v])

    for v in pred_Y:
        if Y in graph.graph_inverted[v]:
            print("deletado: ", Y, graph.graph_inverted[v][Y])
            del graph.graph_inverted[v][Y]
        print(f"L Adj de {v} sem Y ({Y}): ", graph.graph_inverted[v])

    for v in pred_X:
        print(f"adicionando {Y} na L Adj de {v}")
        graph.addEdgeInverted(v, Y)
        print(f"nova aresta {Y} em {graph.graph_inverted[v]}")

    for v in pred_Y:
        print(f"adicionando {X} na L Adj de {v}")
        graph.addEdgeInverted(v, X)
        print(f"nova aresta {X} em {graph.graph_inverted[v]}")

    
    print("--- adjs ---")

    print("limpando ", graph.graph_inverted[X])
    graph.graph_inverted[X].clear()
    print("limpo: ", graph.graph_inverted[X])
    
    print("limpando ", graph.graph_inverted[Y])
    graph.graph_inverted[Y].clear()
    print("limpo: ", graph.graph_inverted[Y])
    
    print(f"adicionando adj_Y ({adj_Y}) em X (antes): ", graph.graph_inverted[X])
    graph.graph_inverted[X] = adj_Y
    print("adicionando adj_Y em X (dps): ", graph.graph_inverted[X])

    print(f"adicionando adj_X ({adj_X}) em Y (antes): ", graph.graph_inverted[Y])
    graph.graph_inverted[Y] = adj_X
    print("adicionando adj_X em Y (dps): ", graph.graph_inverted[Y])



    # Troca X <---> Y no grafo Original

    for v in adj_X:
        if X in graph.graph[v]:
            del graph.graph[v][X]

    for v in adj_Y:
        if Y in graph.graph[v]:
            del graph.graph[v][Y]

    for v in adj_X:
        graph.addEdge(v, Y)

    for v in adj_Y:
        graph.addEdge(v, X)

    
    graph.graph[X].clear()
    
    graph.graph[Y].clear()

    graph.graph[X] = pred_Y
    
    graph.graph[Y] = pred_X



class Graph:
    
    # Constructor
    def __init__(self):

        # Lista (Dicionário) de Adjacência
        self.graph = {}

        # Lista (Dicionário) de Adjacência com arestas invertidas
        self.graph_inverted = {}

        # dicionario de idades
        self.age = {}


    # Adiciona uma Aresta (Edge) Direcionada - adiciona vértice na lista de adjacência
    # vertex_X management vertex_Y    ==>    but we'll revert this insertion: Y -> X
    def addEdge(self, vertex_X, vertex_Y):

        if vertex_X not in self.graph:                              # se vertex_X nao existir no dic
            self.graph[vertex_X] = {vertex_Y: self.age[vertex_Y]}       # adiciona-o e cria-se sua lista de adj
        elif vertex_Y not in self.graph[vertex_X]:                  # se vertex_Y nao estiver na lista de adjacência de vertex_X
            self.graph[vertex_X][vertex_Y] = self.age[vertex_Y]         # adiciona-o na sua já existente lista de adj


    def addEdgeInverted(self, vertex_X, vertex_Y):

        if vertex_X not in self.graph_inverted:                                 # se vertex_X nao existir no dic
            self.graph_inverted[vertex_X] = {vertex_Y: self.age[vertex_Y]}          # adiciona-o e cria-se sua lista de adj
        elif vertex_Y not in self.graph_inverted[vertex_X]:                     # se vertex_Y nao estiver na lista de adjacência de vertex_X
            self.graph_inverted[vertex_X][vertex_Y] = self.age[vertex_Y]            # adiciona-o na sua já existente lista de adj



# --------------- Test ---------------
while True:
    try:

        entry1_split = input().split()
        vertex_employees, edges_management, instructions = entry1_split

        # converting str to int
        vertex_employees = int(vertex_employees)    # N = Vertices | Empregados
        edges_management = int(edges_management)    # M = Arestas | Gerência Direta
        instructions = int(instructions)            # I = Instruções

        # instantiate graph
        graph = Graph()

        # criando dicionário auxiliar com chaves de 1 a N e valores recebidos por
        # meio de uma lista dada pelo usuário
        entry_age = input().split()
        for i in range(vertex_employees):

            # atribuindo cada idade a seu funcionario em um dict auxiliar
            graph.age[str(i+1)] = int(entry_age[i])

            # criando grafo/lista de adjacência
            graph.graph[str(i+1)] = {}

            # criando grafo/lista de adjacência invertido
            graph.graph_inverted[str(i+1)] = {}

        # print("graph pre: ", graph.graph)
        # print("graph_inverted pre: ", graph.graph_inverted)

        # creating graph and adjacency list
        while edges_management != 0:

            edge = input().split()
            # adj_X management adj_Y
            adj_X, adj_Y = edge

            # creating edge in graph
            graph.addEdge(adj_X, adj_Y)

            edges_management -= 1
        
        
        # inverting the directions of the edges
        # for u in graph.graph:
        #     graph.graph_inverted[u] = {}
        
        for u in graph.graph:
            for v in graph.graph[u]:
                graph.addEdgeInverted(v, u)
            

        print("graph orig: ", graph.graph)
        print("graph_inverted: ", graph.graph_inverted)

        while instructions != 0:
            
            instruction = input().split()
            
            if instruction[0] == "P":
                # Pergunta
                ask(graph.graph_inverted, instruction[1])
            else:
                # Troca
                change(graph, instruction[1], instruction[2])
        
            print("graph orig: ", graph.graph)
            print("graph_inverted: ", graph.graph_inverted)

            instructions -= 1
        

        # desalocar tudo pq vai vir novo caso de teste

    except EOFError:
        break






# distance_input_cheese = None
# key = "*"
# while key != "Entrada":
#     key = predecessor[key]
#     distance_input_cheese += 1

# # para verificar se foi contabilizado
# print(distance_input_cheese)

