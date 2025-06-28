/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */

 #ifndef RETORNO_H

 #define RETORNO_H
 
 #include "Aresta.h"
 #include <vector>
 
 class Retorno {
 public:
    bool pode_adicionar;
    int posicao1;
    int posicao2;

    Retorno(int pos1, int pos2, bool retorno);

 private:

 };
 
 #endif /* RETORNO_H */