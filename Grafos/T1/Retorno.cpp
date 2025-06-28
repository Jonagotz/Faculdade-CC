/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */

 
 #include "Retorno.h"
 #include <exception>
 #include <stdexcept>
 #include <string>
 #include <iostream>
 #include <stack>
 
 using namespace std;

 Retorno::Retorno(int pos1, int pos2, bool retorno){
   posicao1 = pos1;
   posicao2 = pos2;
   pode_adicionar = retorno;
}