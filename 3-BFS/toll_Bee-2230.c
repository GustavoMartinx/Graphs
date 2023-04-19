#include <stdlib.h>
#include <stdio.h>


// Define the node struct for the linked list and queue
struct Node {
    int data;
    struct Node* next;
} typedef Node;

typedef struct queue {
    Node* start;
    Node* end;
    int qtde;
} Queue;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to add a node to the linked list
void addNodeList(Node** head, int data) {
    
    Node* newNode = createNode(data);
    
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* lastNode = *head;
        while (lastNode->next != NULL) {
            if (lastNode->data == data) {
                return;
            }
            lastNode = lastNode->next;
        }
        lastNode->next = newNode;
    }
}

// Function to print the linked list
void printList(Node *head) {
    while (head != NULL) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

// Function to free the memory allocated for the linked list
void freeList(Node** head) {
    Node *temp;
    while (*head != NULL) {
        temp = *head;
        *head = (*head)->next;
        free(temp);
    }
}


// ===== QUEUE FUNCTIONS =====
Queue* queue_create() {

    Queue* queue = (Queue*) malloc(sizeof(Queue));
    
    queue->start = NULL;
    queue->end = NULL;
    queue->qtde = 0;
    
    return queue;
}

void enqueue(Queue* q, int element) {

    Node* new = createNode(element);

    if(q->qtde == 0) {  // verificando se a fila está vazia
        q->start = new; // insere novo elem no início
    } else {            // senão, insere no final
        q->end->next = new; // encadeia o novo elem no fim da fila com o antigo último
    }
    q->end = new; // atualiza o ponteiro para último elemento (end) da struct Fila para o novo elem
    q->qtde++;
}

void dequeue(Queue* q, int* out) {

    Node* aux = q->start;
    q->start = q->start->next;
    q->qtde--;
    
    *out = aux->data;
    free(aux);
    
    if(q->start == NULL){        
        q->end = NULL;
    }
}

void queue_destroy(Queue* queue) {

    if(queue->start == NULL) {
        free(queue);
        return;
    }
    Node* current = queue->start;
    Node* next;
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    free(queue);
}

// ====== SELECTION SORT =======
void selectionSort(int* V, int n) {
    int i, j, min_index;

    for (i = 0; i < n-1; i++) {
        min_index = i;
        for (j = i+1; j < n; j++) {
            if (V[j] < V[min_index]) {
                min_index = j;
            }
        }
        int temp = V[min_index];
        V[min_index] = V[i];
        V[i] = temp;
    }

    for (i = 0; i < n-1; i++) {
        printf("%d ", (V[i]+1));
    }
    printf("%d \n\n", (V[n-1]+1));

}


void BFS(Node** vertex, int location, int c, int p) { // location = s = vertice inicial da busca/onde estão

    // cor de cada vértice
    char color[c];      // Branco: vertices não visitados. Cinza: alcaçados mas nao processados. Pretos: processados
    int predecessor[c]; // Vértice predecessor (pai) do vértice
    int distance[c];    // Distância do vértice em relação ao vértice inicial

    Queue* queue = queue_create();

    // inicializa vetor color com branco, dist infinita, pred null
    for(int i = 0; i < c; i++) {
        color[i] = 'B'; // B = Branco
        distance[i] = __INT_MAX__;
        predecessor[i] = -1; // null
    }

    // atribui esses valores para o vertice s/location/onde eles estão
    color[location] = 'C';  // C = Cinza
    distance[location] = 0;
    predecessor[location] = -1; // null
   
    // printf("---- Before ----\n");
    // int count = 0;
    
    // printf("color: ");
    // while(count < c) {
    //     printf("%c ", color[count]);
    //     count++;
    // }

    // count = 0;
    // printf("\ndistance: ");
    // while(count < c) {
    //     printf("%d ", distance[count]);
    //     count++;
    // }

    // count = 0;
    // printf("\npredecessor: ");
    // while(count < c) {
    //     printf("%d ", predecessor[count]);
    //     count++;
    // }

    enqueue(queue, location);

    int u = 0;
    while (queue->qtde != 0) {
        
        // desenfileira elem u
        dequeue(queue, &u);
        
        Node* lastNode = vertex[u]; // lastNode é "head" da lista (primeiro vertice da lista de adj)
        while(lastNode != NULL) {
            
            if (color[lastNode->data] == 'B') { // B = Branco
                color[lastNode->data] = 'C'; // C = Cinza
                distance[lastNode->data] = distance[u] + 1;
                predecessor[lastNode->data] = u;
                enqueue(queue, lastNode->data);
            }
            lastNode = lastNode->next; // incrementa "head" para percorrer lista de adj
        }
        color[u] = 'P'; // P = Preto
    }

    // ----- test ------
    // printf("\n\n---- After  ----\n");
    // count = 0;
    
    // printf("color: ");
    // while(count < c) {
    //     printf("%c ", color[count]);
    //     count++;
    // }

    // count = 0;
    // printf("\ndistance: ");
    // while(count < c) {
    //     printf("%d ", distance[count]);
    //     count++;
    // }

    // count = 0;
    // printf("\npredecessor: ");
    // while(count < c) {
    //     printf("%d ", predecessor[count]);
    //     count++;
    // }

    // count = 0;
    // printf("\nvetorzao: ");
    // while(count < c) {
    //     printf("%p ", vertex[count]);
    //     count++;
    // }
    // printf("\n");

    // distancia <= p: cidades que podem ser visitadas -> de algum modo com predecessor
    int vet[c-1];
    int j = 0;
    for(int i = 0; i < c; i++) {
        if (distance[i] <= p && distance[i] > 0) {
            // i é o vertice (indice) no qual é possível chegar
            // adiciona i em um vet
            vet[j] = i;
            j++;
        }
    }
    selectionSort(vet, j);
}


int main() {

    int c = 0; // qtde de vertices
    int e = 0; // qtde de arestas
    int l = 0; // vertice inicial
    int p = 0; // qtde de pedágios que se pode passar
    int k = 0; // count = e (para liberação de mem)
    int x = 1; // count do Teste (output)
    scanf("%d %d %d %d", &c, &e, &l, &p);
 
    while ((c != 0) || (e != 0) || (l != 0) || (p != 0)) {
        
        // variável contadora (k) para realizar desalocação de memória das listas de adjacencias de cada posição do vetor
        k = e;

        // Criando o vetor de vértices/cidades no qual será armazenado as listas de adjacentes
        Node** vertex = (Node**) calloc(c, sizeof(Node*));
        
        int adj1 = 0;
        int adj2 = 0;

        while (e != 0) {
            
            scanf("%d %d", &adj1, &adj2);

            // manipulando número do vértice para facilitar o manejamento dele no vetor/lista
            adj1--;
            adj2--;
        
            //printf("inserindo: v[%d] = %d\n", adj1, adj2);

            // Atribuindo/relacionando cada posição desse vertor à sua respectiva lista de adjacentes
            addNodeList(&(vertex[adj1]), adj2);
            addNodeList(&(vertex[adj2]), adj1);

            e--;
        }

        // ======= LISTA ADJACÊNCIA =======
        // printf("\nposicao zero\n");
        // printList(vertex[0]);

        // printf("\nposicao um\n");
        // printList(vertex[1]);
        
        // printf("\nposicao dois\n");
        // printList(vertex[2]);
        
        // printf("\nposicao tres\n");
        // printList(vertex[3]);
        
        // printf("\nposicao quatro\n");
        // printList(vertex[4]);

        // ========= QUEUE ===========
        // int element;
        // Queue* q1 = queue_create();
        
        // enqueue(q1, 10);
        // enqueue(q1, 20);
        // enqueue(q1, 30);
        // printf("----- Testing Enqueue -----\n");
        // printList(q1->start); // ate 30
        

        // printf("----- Testing Dequeue -----\n");
        // dequeue(q1, &element);
        // printList(q1->start); // 20 e 30
        
        // queue_destroy(q1);
        
        printf("Teste %d\n", x++);
        // ====== BFS - Busca em Largura =======
        BFS(vertex, l-1, c, p); // c = qtde vertices
        
        // Liberação de memória (Seg Fault)
        // while(k > -1) {
        //     freeList(&(vertex[k]));
        //     k--;
        // }
        // free(vertex);
    
        scanf("%d %d %d %d", &c, &e, &l, &p);
    }
    
    return 0;
}
