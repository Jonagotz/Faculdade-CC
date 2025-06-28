/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */
#include "Aresta.h"
#include "Grafo.h"
#include <exception>
#include <string>
#include <iostream>

using namespace std;

void print_exception(const exception &e, int level = 0) {
    cerr << "exception: " << string(level, ' ') << e.what() << "\n";
    try {
        rethrow_if_nested(e);
    } catch(const std::exception& nested_exception) {
        print_exception(nested_exception, (level + 2));
    }
}

void zera_marcado(int marcado[], int tamanho) {
    for (int i = 0; i < tamanho; i++){
        marcado[i] = 0;
    }
}

void verifica_biparticoes(Grafo g) {
    int num_vertices = g.num_vertices();
    int* marcado = new int[num_vertices];
    zera_marcado(marcado, num_vertices);

    if (g.eh_bipartido_1(0, marcado)){
        cout << "SIM" << "\n";
    } else {
        cout << "NAO" << "\n";
    }
    zera_marcado(marcado, num_vertices);
//__________________________________________________//
    if (g.eh_bipartido_2(0, marcado)){
        cout << "SIM" << "\n";
    } else {
        cout << "NAO" << "\n";
    }
}

int main() {
    try {

        int qtd_vertices, qtd_arestas;
        cin >> qtd_vertices >> qtd_arestas;
        
        Grafo g(qtd_vertices);

        for (int i = 0; i < qtd_arestas; i++) {
            int u, v; 
            char w;
            cin >> u >> v >> w;
            if (w != 'N') {
                g.insere_aresta(Aresta(u, v));
            }
        }

        verifica_biparticoes(g);
        // g.imprime();
    }
    catch (const exception &e) {
        print_exception(e);
    }

    return 0;
}
