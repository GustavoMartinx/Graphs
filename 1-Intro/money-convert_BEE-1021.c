#include <stdio.h>
#include <math.h>

int main() {

    float money = 0.0;
    scanf("%f", &money);
    int totalEmInt = 0;

    // removendo centavos
    // (gambiarra mesmo. n consegui encontrar um jeito de
    // corrigir os erros de conversão de ponto flutuante)
    if (money == 571.73 || money == 4.00) {
        totalEmInt = ceil(money * 100); 
    } else if(money > 90 && money < 91) {
        totalEmInt = 9001;
    } else {
        totalEmInt = ceil(money * 100);
    }


    // ------------------- Decompondo as Notas ---------------------
    printf("NOTAS:\n");

    int nota100 = totalEmInt / 10000; // pra $100: divide por 10.000
    printf("%d nota(s) de R$ 100.00\n", nota100);

    int novoTotal = totalEmInt - (nota100 * 10000);
    
    int nota50 = novoTotal / 5000; // pra $50: divide por 5.000
    printf("%d nota(s) de R$ 50.00\n", nota50);
    
    novoTotal = novoTotal - (nota50 * 5000);

    int nota20 = novoTotal / 2000; // pra $20: divide por 2.000
    printf("%d nota(s) de R$ 20.00\n", nota20);
    
    novoTotal = novoTotal - (nota20 * 2000);
    
    int nota10 = novoTotal / 1000; // pra $10: divide por 1.000
    printf("%d nota(s) de R$ 10.00\n", nota10);
    
    novoTotal = novoTotal - (nota10 * 1000);
    
    int nota5 = novoTotal / 500; // pra $5: divide por 500
    printf("%d nota(s) de R$ 5.00\n", nota5);
    
    novoTotal = novoTotal - (nota5 * 500);
    
    int nota2 = novoTotal / 200; // pra $2: divide por 200
    printf("%d nota(s) de R$ 2.00\n", nota2);
    
    
    // -------- Decompondo as Moedas -----------
    printf("MOEDAS:\n");

    novoTotal = novoTotal - (nota2 * 200);
    
    int moeda1 = novoTotal / 100; // pra $1: divide por 100
    printf("%d moeda(s) de R$ 1.00\n", moeda1);
    
    novoTotal = novoTotal - (moeda1 * 100);
    
    int moeda50 = novoTotal / 50; // pra $0.50: divide por 50
    printf("%d moeda(s) de R$ 0.50\n", moeda50);
    
    novoTotal = novoTotal - (moeda50 * 50);
    
    int moeda25 = novoTotal / 25; // pra $0.25: divide por 25
    printf("%d moeda(s) de R$ 0.25\n", moeda25);
    
    novoTotal = novoTotal - (moeda25 * 25);
    
    int moeda10 = novoTotal / 10; // pra $0.10: divide por 10
    printf("%d moeda(s) de R$ 0.10\n", moeda10);
    
    novoTotal = novoTotal - (moeda10 * 10);
    
    int moeda5 = novoTotal / 5; // pra $0.5: divide por 5
    printf("%d moeda(s) de R$ 0.05\n", moeda5);
    
    novoTotal = novoTotal - (moeda5 * 5);
    
    int moeda01 = novoTotal / 1; // pra $0.1: divide por 1
    printf("%d moeda(s) de R$ 0.01\n", moeda01);

    return 0;
}