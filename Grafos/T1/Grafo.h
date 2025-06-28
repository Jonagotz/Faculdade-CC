/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */

 #ifndef GRAFO_H

 #define GRAFO_H
 
 #include "Aresta.h"
 #include <vector>
 #include "Retorno.h"
 
 class Grafo {
 public:
    int num_vertices();
    int num_arestas();

    Grafo(int num_vertices);

    bool tem_aresta(Aresta e);

    /** Insere uma aresta no grafo caso a aresta ainda nao exista no grafo e
     * nao seja um laco */
    void insere_aresta(Aresta e);

    /** Remove uma aresta do grafo caso a aresta exista no grafo */
    void remove_aresta(Aresta e);

    void imprime();

    bool eh_bipartido_1(int v, int marcado[]);
   //  bool eh_bipartido_1_2(int v, int marcado[]);
    bool eh_bipartido_2(int v, int marcado[]);
 private:
    int num_vertices_;
    int num_arestas_;
    std::vector<std::vector<int>> matriz_adj_;

    void valida_vertice(int v);
    void valida_aresta(Aresta e);
    bool eh_bipartido_1_aux(int marcado[], int v);
    bool verifica_esta_contido(int valor, int conjunto[], int tamanho);
    Retorno particiona(int marcado[], int conjunto1[], int counjunto2[], Retorno r);
    bool pode_adicionar(int v, int conjunto[]);
    void imprime_vetor(int vetor[], int tamanho);

 };
 
 #endif /* GRAFO_H */