#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct ABB {
    char chave;
    struct ABB* esq;
    struct ABB* dir;
} ABB;


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

ABB* ABB_Buscar(ABB *A, char chave) {
    if(A == NULL){
        return NULL;
    }
    if(A->chave == chave){
        return A;
    }
    if(chave < A->chave){
        return ABB_Buscar(A->esq, chave);
    }
    return ABB_Buscar(A->dir, chave);
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
    printf("%c ", A->chave);
}

int main() {

    char comand[8];

    ABB* abb = NULL;

    while(scanf("%[^\n]%*c", comand) != EOF) {

        comand[strlen(comand)] = '\0';

        if(comand[0] == 'I' && comand[1] == ' ') {
            
            ABB_Inserir(&abb, comand[2]);
        
        } else if(comand[0] == 'P' && comand[1] == ' ') {
            
            ABB* busca = NULL;
            busca = ABB_Buscar(abb, comand[2]);

            if(busca == NULL) {
                printf("%c nao existe\n", comand[2]);
            } else {
                printf("%c existe\n", comand[2]);
            }

        } else if(comand[0] == 'I' && comand[1] == 'N') {
        
            ABB_ImprimirInfixa(abb);
            printf("\b\n");
        
        } else if(comand[1] == 'R') {

            ABB_ImprimirPrefixa(abb);
            printf("\b\n");

        } else if(comand[1] == 'O') {
            
            ABB_ImprimirPosfixa(abb);
            printf("\b\n");
        }
    }
    return 0;
}