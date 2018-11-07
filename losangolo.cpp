#include <stdio.h>
#include <stdlib.h>

main()
{
     // Declaração de Variaveis
     int N; // Numero de Linhas e Colunas
     int i; // Incremento do FOR
     int menu; // Selecção do MENU ( 0 ou 1 )
     int espc; // Variavel para os espaços antes do losango
     int chars; // Variavel para os asteriscos
     do
     {
     fflush(stdin); // Limpa a memoria do teclado
     system("cls");
     // ABRE O MENU COM PRINTF's
     printf("  --------------------------------------------------------------------------- \n");
     printf(" |                            DESENHAR LOSANGO                               |\n");
     printf("  --------------------------------------------------------------------------- \n\n");

     printf("   MENU\n");
     printf("   -------------------------------------------------------------------------\n\n");
     printf("   1\t-    DESENHAR LOSANGO\n\n");
     printf("   0\t-    SAIR\n\n");

     printf("   ESCOLHA: ");
     scanf("%d", &menu); // Apanha a escolha do utilizador

     // SWITCH para descubrir qual o menu que o utilizador quer aceder
     switch(menu)
     {
      case 1: // Caso 'DESENHAR LOSANGO'
           do{
            printf("\n   INTRODUZA AS LINHAS: ");
            fflush(stdin);// Limpa a memoria do teclado
            scanf("%d", &N);

            if(N%2 == 0 || N < 5) // VERIFICA se o numero e impar ou se e maior que 5
                   printf("\n\n   O NUMERO TEM QUE SER IMPAR E SUPERIOR A 4...\n");
            } while (N%2 == 0 || N < 5 ); // VERIFICA se o numero e impar ou se e maior que 5

            espc = N / 2;
            chars = 1;

            printf("\n\n");

            // Linhas de Cima da Central

            do {
            for ( i = espc; i > 0; i-- ) printf("  "); // Espaços
            for ( i = chars; i > 0; i-- ) // Asteriscos
            {
                    printf("* ");       
            }
            printf("\n"); // Enter no final de cada linha

            espc--; // os espaços diminuem a medida que as linhas aumentam
            chars=chars+2; // os asteriscos aumentam em 2 a medida que as linhas aumentam

            } while ( espc > 0 ); // quando o espaço for '0' ele passa a linha do meio e as de baixo

            // Linha Central e Linhas Abaixo

            do {
            for ( i = espc; i > 0; i-- ) printf("  "); // Espaços
            for ( i = chars; i > 0; i-- ) // Asteriscos
            {
                    printf("* ");

            }
            printf("\n"); // Enter no final de cada linha
            espc++;  // os espaços aumentam a medida que as linhas diminuem
            chars=chars-2; // os asteriscos diminuem em 2 a medida que as linhas diminuem

            } while ( espc <= N / 2 ); // Quando o espaço for menor que o numero de linhas a dividir por 2 ele PARA

            printf("\n\n   ");

            system("pause"); // Espera que o utilizador carregue no ENTER para voltar ao menu

            break; // FIM CASO 'DESENHAR LOSANGO'

      case 0: // CASO 'SAIR'
           break; // FIM CASO 'SAIR'

      default: // CASO o Comando esteja invalido
              printf("\n  Comando Invalido\n  ");
              system("pause");

      // FIM CASO DEFAULT
     }

     } while(menu != 0); // Enquanto a variavel menu nao estiver a 0, ele abre sempre o menu
}
