/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */

#include "Aresta.h"
#include <string>

using namespace std;

 Aresta::Aresta(int v1, int v2) : v1(v1), v2(v2) {
 }

string Aresta::to_string() {
    return std::to_string(v1) + " " + std::to_string(v2);
}
