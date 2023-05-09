time = 0

def dfs_visit(graph, u, color, predecessor):
    
    time += 1
    D, F = {}
    D[u] = time
    color[u] = 'g'

    for v in graph[u]:
        if color[v] == 'w':
            predecessor[v] = u
            dfs_visit(graph, v, color, predecessor)
    
    color[u] = 'b'
    time += 1
    F[u] = time

def dfs(graph):

    color = {}
    predecessor = {}

    for v in graph:
        color[v] = 'w'
        predecessor[v] = None
    
    time = 0

    for u in graph:
        if color[u] == 'w':
            dfs_visit(graph, u, color, predecessor)
