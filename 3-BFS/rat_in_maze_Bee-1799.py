def BFS(graph, start, objective):
    
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
        
        # Quantidade de Vértices presentes neste grafo
        #self.V = V
        
        # Quantidade de Arestas (Edges) presentes neste grafo
        #self.E = E

        # Lista (Dicionário) de Adjacência
        self.graph = {}


    # Adiciona uma Aresta (Edge) - adiciona vértice na lista de adjacência
    def addEdge(self, vertex_X, vertex_Y):
        
        if vertex_X not in self.graph:             # se vertex_X nao existir no dic
            self.graph[vertex_X] = [vertex_Y]           # adiciona-o e cria-se sua lista de adj
        elif vertex_Y not in self.graph[vertex_X]: # se vertex_Y nao estiver na lista de adjacência de vertex_X
            self.graph[vertex_X].append(vertex_Y)       # adiciona-o na sua já existente lista de adj
        
        if vertex_Y not in self.graph:             # se vertex_Y nao existir no dic
            self.graph[vertex_Y] = [vertex_X]           # adiciona-o e cria-se sua lista de adj
        elif vertex_X not in self.graph[vertex_Y]: # se vertex_X nao estiver na lista de adjacência de vertex_Y
            self.graph[vertex_Y].append(vertex_X)       # adiciona-o na sua já existente lista de adj


    # Imprime a quantidade de Vértices
    # def getV(self):
    #     return self.V
    
    # Imprime a quantidade de Arestas (Edges)
    # def getE(self):
    #     return self.E
    




# ---------------- Test 1 ----------------

N_entry = input()
N_entry_split = N_entry.split()
vertex, edges = N_entry_split

# converting str to int
vertex = int(vertex)
edges = int(edges)

graph = Graph()

while edges != 0:

    E_entry = input()
    V_entry_split = E_entry.split()
    adj1, adj2 = V_entry_split

    # creating edge in graph
    graph.addEdge(adj1, adj2)

    edges -= 1

dist_1 = None
dist_1 = BFS(graph.graph, "Entrada", "*")

dist_2 = None
dist_2 = BFS(graph.graph, "*", "Saida")

print(dist_1+dist_2)








# ========== dictionary manipulation ===============

# vetor_de_dic = [{'a': 1, 'b': 2, 'c': 3, 'd': 4,'e': 5, 'f': 6}]

# acessando um dicionário dentro do vetor
# print(vetor_de_dic[0]['f'])

# inserindo um novo elemento num dicionario que está dentro de um vetor
# vetor_de_dic[0]['g'] = 7

# alterando um elemento de um dicionario que está dentro de um vetor
# vetor_de_dic[0]['g'] = 8

# adicionando um novo dicinário em uma nova posição do vetor
# vetor_de_dic.append({'h': 10})

# adicionando um dicionário como valor de uma chave de um dicionário
# vetor_de_dic.append({'vertice_2': {'e_sua_lista': 11, 'de_adj': 12}})
# print(vetor_de_dic)
# vetor_de_dic[2]['vertice_2'] = {'e_sua_lista': 11, 'de_adj': 12, 'manipulada': 13}
# print(vetor_de_dic)

# adicionando um elemento por meio de uma variável em um dicionario
# inputVariable = input()
# vetor_de_dic[1][inputVariable] = -1
# print(vetor_de_dic)


# para vetor de cor, utilizaremos outro dicionário
# cor[vertice_x] = 'B'  # cor do vertice_x é Branco

# para vetor de predecessor (pai) de um vértice, utilizar outro dicionário
# predecessor[vertice_x] = 'pai-de-x'

# para vetor de distancia, utilizaremos outro dicionário
# distancia[vertice_x] = Z  # distancia de um vertice_x em relacao ao vertice inicial é Z  |  esses dics estão dentro do BFS


# criando um dicionario cujo valor é uma lista de vertices adjacentes
# grafo = {'vertice_1': ['adj1', 'adj2'], 'vertice_2': ['adj3', 'adj4']}


# iterando por um dicionario
# dicionario_grafo = {'vertice_1': {'e_sua_lista': 1, 'de_adj': 2}, 'vertice_2': {'e_sua_lista': 3, 'de_adj': 4}}

# print(dicionario_grafo)

# for vertex in dicionario_grafo:
#     print(dicionario_grafo[vertex])

#     for list_adj in dicionario_grafo[vertex]:
#         print(dicionario_grafo[vertex][list_adj])

# adicionando uma nova chave no dicionario (representando um novo vertice)
# dicionario_grafo['vertice_3'] = {'e_sua_lista': 5, 'de_adj': 6}

# rat: criando uma aresta com (lista de adj) dicionarios em python
# input -> var_vertice_x, var_vertice_y
# dicionario_grafo['vertice_X'] = {'adjacente_Y': 1}
# dicionario_grafo['vertice_Y'] = {'adjacente_X': 1}

# print(dicionario_grafo)

# for vertex in dicionario_grafo:
#     print(dicionario_grafo[vertex])

#     for list_adj in dicionario_grafo[vertex]:
#         print(dicionario_grafo[vertex][list_adj])

# verificando o tamanho do dicionario (não preciso, é dado como input)
# print(dicionario_grafo.__len__())

# predecessor = {}
# for vertex in dicionario_grafo:
#     predecessor[vertex] = None
# print(predecessor)
