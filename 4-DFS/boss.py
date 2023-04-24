def ask(graph, start):
    
    color = {}
    queue = []
    minor_age = 101

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
            print(graph[u])
            
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



def change(graph, start, objective):
    
    predecessor = {}
    distance = {}
    color = {}
    queue = []

    # initialization
    for vertex in graph:
        color[vertex] = 'W'         # W = white | B = black | G = gray
        distance[vertex] = -1       # -1 = undefined
        predecessor[vertex] = None  # None = undefined

    color[start] = 'G'
    distance[start] = 0
    
    # enqueuing the start vertex
    queue.append(start)

    u = None
    while queue:
        
        # dequeuing
        u = queue.pop(0)
        
        # traverse the list of adjacent vertices of the dequeued vertex
        for v in graph[u]:
            if color[v] == 'W':
                color[v] = 'G'
                distance[v] = distance[u] + 1

                if v == objective:     # objective = "saida" or "*"
                    return distance[v] # distance between objective and start

                predecessor[v] = u
                queue.append(v)
                
        color[u] = 'B'

    return predecessor



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

        # criando dicionário com chaves de 1 a N e valores recebidos por meio de uma lista dado pelo usuário
        entry_age = input().split()
        for i in range(vertex_employees):
            graph.age[str(i+1)] = int(entry_age[i])


        # creating graph and adjacency list
        while edges_management != 0:

            edge = input().split()
            # adj_X management adj_Y
            adj_X, adj_Y = edge

            # creating edge in graph
            graph.addEdge(adj_X, adj_Y)

            edges_management -= 1
        
        
        # inverting the directions of the edges
        for u in graph.graph:
            graph.graph_inverted[u] = {}
        print("graph_inverted pre: ", graph.graph_inverted)
        
        for u in graph.graph:
            for v in graph.graph[u]:
                graph.addEdgeInverted(v, u)
            

        print("graph orig: ", graph.graph)
        print("graph_inverted: ", graph.graph_inverted)

        while instructions != 0:
            
            instruction = input().split()
            
            if instruction[0] == "P":
                # pergunta
                ask(graph.graph_inverted, instruction[1])
            #else:
                # Troca
                # change(graph.graph, instruction[1], instruction[2])

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

