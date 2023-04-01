#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct ABB {
    char chave;
    struct ABB* esq;
    struct ABB* dir;
} ABB;

int index_pre = 0;

ABB* ABB_Criar(char chave) {

    ABB* novo = (ABB*) calloc(1, sizeof(ABB));

    novo->chave = chave;
    novo->dir = NULL;
    novo->esq = NULL;
    
    return novo;
}

void ABB_Inserir(ABB** A, char chave) {

    if((*A) == NULL) {
        *A = ABB_Criar(chave);
        return;
    }
    
    if(chave < (*A)->chave) {

        ABB_Inserir(&(*A)->esq, chave);

    } else {
        ABB_Inserir(&(*A)->dir, chave);
    }
}

void ABB_ImprimirPrefixa(ABB *A) {
    if(A == NULL)
        return;
    printf("%c ", A->chave);
    ABB_ImprimirPrefixa(A->esq);
    ABB_ImprimirPrefixa(A->dir);
}

void ABB_ImprimirInfixa(ABB *A) {
    if(A == NULL)
        return;
    ABB_ImprimirInfixa(A->esq);
    printf("%c ", A->chave);
    ABB_ImprimirInfixa(A->dir);
}

void ABB_ImprimirPosfixa(ABB *A) {
    if(A == NULL)
        return;
    ABB_ImprimirPosfixa(A->esq);
    ABB_ImprimirPosfixa(A->dir);
    printf("%c", A->chave);
}

void ABB_FreeNode(ABB* node) {
    if(node == NULL) {
        return;
    }
    ABB_FreeNode(node->esq);
    ABB_FreeNode(node->dir);
    free(node);
    node = NULL;
}

void buildTree(char* pre_order, char* in_order, ABB** abb, short int i, short int f) {

    // Caso Base
    if(i > f) { // indices inicio > fim 
        return;
    }

    // Pegando primeiro elemnto do percurso prefixa (elemento raíz)
    char Root_FirstPRE = pre_order[index_pre++]; // A
    
    // Inserindo elemento raiz na árvore
    ABB_Inserir(abb, Root_FirstPRE);

    if(i == f) {
       return; 
    }

    // encontrando elemento raíz na string in_order (para separar as duas subárvores esq e dir)
    // obtendo a posição (index) do elem raiz na string IN_order
    short int k;
    short int rootPositionIN = -1;

    for(k = 0; in_order[k] != '\0'; k++) {
        
        if(in_order[k] == Root_FirstPRE) {
            rootPositionIN = k;
            break;
        }
    }


    // subarvore/substr esquerda: de i (inicio) ate pos-1    
    // chamada recursiva para reconstruir a subarvore esquerda
    buildTree(pre_order, in_order, &((*abb)->esq), i, (rootPositionIN - 1));
    
    
    // substring/subarvore direita: pos + 1 ate f (fim)
    // chamada recursiva para reconstruir a subarvore direita
    buildTree(pre_order, in_order, &((*abb)->dir), (rootPositionIN + 1), f);
}



int main() {

    // fazer leitura da(s) entrada(s)
    short int c = 0;  // C <= 2000
    scanf("%hd ", &c);

    while(c > 0) {

		// Alocações para as entradas
        index_pre = 0;
		int comando = 0;
		char prefixo[55];
		char infixo[55];
        
        scanf("%d %s %s", &comando, prefixo, infixo);

        // Costruindo a árvore a partir das duas entradas prefixa e infixa
        ABB *abb = NULL;

        buildTree(prefixo, infixo, &abb, 0, (comando - 1));
        
        // Verificando se a arvore foi construída corretamente
        // printf("imprimindo arvore Pre:\n");
        // ABB_ImprimirPrefixa(abb);
        // printf("\n");

        // // printf("\nimprimindo arvore In:\n");
        // ABB_ImprimirInfixa(abb);
        // printf("\n");

        // aplica percurso posfixo imprimindo a saída
        // printf("\nimprimindo arvore Pos:\n");
        ABB_ImprimirPosfixa(abb);
        printf("\n");
        

        // desaloca todos elem inseridos na arvore e inputs
        // free(abb);

        c--;
    }
    return 0;
    
    // casos de teste:
    // 8 ABEFCDGH EBFADGCH 
    // 3 abc cba
    // 6 ABCDEF CBAEDF
}