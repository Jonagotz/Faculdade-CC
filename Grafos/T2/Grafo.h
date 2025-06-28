/*
 * Trabalho 2 - Coloração de grafos
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nome:      Jonathan Götz Correa e Marco Lunardi
 * Matricula: 2121101052 e 2221101054
 */

#ifndef GRAFO_H

#define GRAFO_H

#include "Aresta.h"
#include <vector>
#include <list>

class Grafo {
public:
    /** Constroi um grafo simples que possui o numero de vertices recebido por
     *  parametro e que nao possui arestas */
    Grafo(int num_vertices);

    int num_vertices();
    int num_arestas();

    bool tem_aresta(Aresta e);

    /** Insere uma aresta no grafo caso a aresta ainda nao exista no grafo e
     * nao seja um laco */
    void insere_aresta(Aresta e);

    void remove_aresta(Aresta e);

    void ConstroiColoracao_1();

    void ConstroiColoracao_2();

    void imprime();

private:
    int num_vertices_;
    int num_arestas_;
    std::vector<std::vector<int>> matriz_adj_;

    void valida_vertice(int v);
    void valida_aresta(Aresta e);
};

#endif /* GRAFO_H */
