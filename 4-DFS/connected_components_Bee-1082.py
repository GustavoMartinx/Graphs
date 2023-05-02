from string import ascii_lowercase

def dfs_visit(graph, u, color, components):
    
    color[u] = 'g'
    
    # adicionar u no vetor que informa os elementos de um componente
    components.append(u)

    for v in graph[u]:
        if color[v] == 'w':
            dfs_visit(graph, v, color, components)
    
    color[u] = 'b'

def dfs(graph, n_connected_components):

    color = {}
    components = []

    for v in graph:
        color[v] = 'w'

    for u in graph:
        if color[u] == 'w':
            
            components.clear()
            n_connected_components += 1
            dfs_visit(graph, u, color, components)
            components.sort()
            for vertex in components:
                print(f"{vertex},", end='')
            print()

    return n_connected_components

def addEdge(graph, vertex_X, vertex_Y):

    if vertex_Y not in graph[vertex_X]:
        graph[vertex_X].append(vertex_Y)
    
    if vertex_X not in graph[vertex_Y]:
        graph[vertex_Y].append(vertex_X)


n = input()
n = int(n)
case_test = 1
while n:
    vertex, edges = input().split()
    vertex = int(vertex)
    edges = int(edges)
    graph = {}
    # pega as letras 'a' até vertex
    letters = ascii_lowercase[:vertex]
    n_connected_components = 0

    for letter in letters:
        graph[letter] = []

    # creating graph/adjacency list
    while edges != 0:
        
        X, Y = input().split()

        # creating edge in graph
        addEdge(graph, X, Y)

        edges -= 1

    print(f"Case #{case_test}:")
    n_connected_components = dfs(graph, n_connected_components)
    print(f"{n_connected_components} connected components")
    print()

    case_test += 1
    n_connected_components = 0
    n -= 1