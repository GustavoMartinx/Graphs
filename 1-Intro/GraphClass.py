class Graph:
    
    # Constructor
    def __init__(self, N):
        # N: quantidade de vértices presentes neste grafo
        self.N = N

        # Matriz de Adjacência: (tamanho: N x N)
        ''' Matriz booleana com colunas e linhas indexadas pelos vértices. Se adj[][] é uma tal matriz então, para cada vértice v e cada vértice w,
        adj[v][w] = 1   se v-w é um arco  e
        adj[v][w] = 0   em caso contrário.
        Assim, a linha v da matriz adj[][] representa as arestas que saem no vértice v e a coluna w representa as arestas que entram no vértice w '''
        self.adjMatrix = [ [0 for i in range(N)] for j in range(N)]

        # Dicionário (chave-posiçãoDaMatriz: valor-nomeAresta)
        self.pesos = {}

    
    # Para alterar o valor de N (qte vértices)
    def setN(self, N):
        self.N = N


    # Adiciona uma Aresta Direcionada que sai do vértice u para o vértice v
    def addEdge(self, u, v, w = ''):
        
        # adiciona uma aresta direcionada que sai de u e vai pra v (com o peso w, se existir)
        if w == '':
            # inserir valor 1 na posição da matriz [u][v] (sai de u, vai pra v) - contrario não.
            self.adjMatrix[u][v] = 1

        elif w != '':
            self.adjMatrix[u][v] = 1
            # inserir peso de w no valor do dict, cuja chave será linha coluna da adjMatrix
            self.pesos[f'{u} + {v}'] = w

        

    # Imprime a qte de Vértices
    def getN(self):
        return self.N
    
    # Imprime a adjMatrix
    def getAdjMatrix(self):
        return self.adjMatrix
    
    # Imprime os pesos das arestas
    def getPesos(self):
        for matPosition in self.pesos.keys():
            print(f'{matPosition}: {self.pesos[matPosition]}')
            # Linha + Coluna: "Peso_da_aresta"


    # Acessa o Grau de Entrada de um Vértice
    def getInDegree(self, V):
        count = 0
        
        if self.N <= 1:
            if self.adjMatrix[0][0] == 1:
                count += 1
                return count
            else:
                return count
        else:
            
            for i in range(self.N): 
                count += self.adjMatrix[i][V]

            return count

    # Acessa o Grau de Saída de um Vértice
    def getOutDegree(self, V):
        count = 0
        
        if self.N <= 1:

            if self.adjMatrix[0][0] == 1:
                count += 1
                return count
            else:
                return count
        else:

            for i in range(self.N): 
                count += self.adjMatrix[V][i]

            return count
        

    # Acessa o Grau de um Vértice
    def getDegree(self, V):
        OutDegree = self.getOutDegree(V)
        InDegree = self.getInDegree(V)

        return (InDegree + OutDegree)




# ---------------- Test 1 ----------------
g1 = Graph(1)

g1.addEdge(0,0)

print(g1.getInDegree(0), g1.getOutDegree(0), g1.getDegree(0)) # output: 1 1 2


# ---------------- Test 2 ----------------
g2 = Graph(2)

g2.addEdge(0,1)

print(g2.getInDegree(0), g2.getOutDegree(1), g2.getInDegree(1),g2.getOutDegree(0)) # output: 0 0 1 1
