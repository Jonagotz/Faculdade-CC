/*
 * Trabalho 2 - Coloração de grafos
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nome:      Jonathan Götz Correa e Marco Lunardi
 * Matricula: 2121101052 e 2221101054
 */

#include "Grafo.h"
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

Grafo::Grafo(int num_vertices) : num_vertices_(num_vertices) {
    matriz_adj_.resize(num_vertices, vector<int>(num_vertices, false));
}

int Grafo::num_vertices() {
    return num_vertices_;
}

int Grafo::num_arestas() {
    return num_arestas_;
}

bool Grafo::tem_aresta(Aresta e) {
    if (matriz_adj_[e.v1][e.v2] != 0) {
        return true;
    }
    return false;
}

void Grafo::remove_aresta(Aresta e) {
    try {
        valida_aresta(e);
    } catch (...) {
        throw_with_nested(runtime_error("Erro na operacao "
            "remove_aresta(Aresta): a aresta " + e.to_string() + " eh "
            "invalida!"));
    }

    if (tem_aresta(e)) {
        matriz_adj_[e.v1][e.v2] = 0;
        matriz_adj_[e.v2][e.v1] = 0;

        num_arestas_--;
    }
}

void Grafo::valida_vertice(int v) {
    if ((v < 0) || (v >= num_vertices_)) {
        throw out_of_range("Indice de vertice invalido: " + to_string(v));
    }
}

void Grafo::valida_aresta(Aresta e) {
    valida_vertice(e.v1);
    valida_vertice(e.v2);
}

void Grafo::insere_aresta(Aresta e) {
    if (e.v1 >= 0 && e.v1 < num_vertices_ && e.v2 >= 0 && e.v2 < num_vertices_ && e.v1 != e.v2) {
        matriz_adj_[e.v1][e.v2] = 1;
        matriz_adj_[e.v2][e.v1] = 1;
    }
}

void Grafo::imprime() {
    cout << "\n" << "O grafo possui as seguintes conexões/arestas" << "\n";
    for (int v = 0; v < num_vertices_; v++) {
        cout << v << ":";
        for (int u = 0; u < num_vertices_; u++) {
            if (matriz_adj_[v][u] != 0) {
                cout << " " << u;
            }
        }
        cout << "\n";
    }
}

void Grafo::ConstroiColoracao_1() {

    vector<int> cores(num_vertices_, 0);
    
    for (int u = 0; u < num_vertices_; u++) {
        vector<bool> usadas(num_vertices_ + 1, false);

        for (int v = 0; v < num_vertices_; v++) {
            if (matriz_adj_[u][v] != 0 && cores[v] != 0) {
                usadas[cores[v]] = true;
            }
        }

        int cor = 1;
        while (usadas[cor]) {
            cor++;
        }
        cores[u] = cor;
    }

    int numero_de_cores = 0;
    for (int i = 0; i < cores.size(); i++) {
        if (cores[i] > numero_de_cores) {
        numero_de_cores = cores[i];
        }
    }

    cout << "Numero de cores: " << numero_de_cores << endl;

    vector<vector<int>> vertices_por_cor(numero_de_cores + 1);
    for (int i = 0; i < num_vertices_; ++i) {
        if (cores[i] != 0) {
            vertices_por_cor[cores[i]].push_back(i);
        }
    }

    for (int i = 1; i <= numero_de_cores; ++i) {
        cout << "Cor " << i << ":";
        for (int j = 0; j < vertices_por_cor[i].size(); j++) {
            cout << " " << vertices_por_cor[i][j];
        }
        cout << endl;
    }
}

void Grafo::ConstroiColoracao_2() {
    
    vector<int> graus(num_vertices_, 0);
    for (int v = 0; v < num_vertices_; ++v) {
        for (int u = 0; u < num_vertices_; ++u) {
            if (matriz_adj_[v][u] != 0) {
                graus[v]++;
            }
        }
    }

    vector<int> vertices_ordenados(num_vertices_);
    for (int i = 0; i < num_vertices_; ++i) vertices_ordenados[i] = i;

    sort(vertices_ordenados.begin(), vertices_ordenados.end(), [&](int i, int j) {
        if (graus[i] != graus[j])
            // ordenando os vértices por grau decrescente
            return graus[i] > graus[j];
        return i < j;
    });

    vector<int> cores(num_vertices_, 0);
    for (int i = 0; i < num_vertices_; ++i) {
        int u = vertices_ordenados[i];
        vector<bool> usadas(num_vertices_ + 1, false);

        for (int v = 0; v < num_vertices_; ++v) {
            if (matriz_adj_[u][v] != 0 && cores[v] != 0) {
                usadas[cores[v]] = true;
            }
        }

        int cor = 1;
        while (usadas[cor]) {
            cor++;
        }
        cores[u] = cor;
    }

    int numero_de_cores = 0;
    for (int i = 0; i < cores.size(); i++) {
        if (cores[i] > numero_de_cores) {
            numero_de_cores = cores[i];
        }
    }

    cout << "Numero de cores: " << numero_de_cores << endl;

    vector<vector<int>> vertices_por_cor(numero_de_cores + 1);
    for (int i = 0; i < num_vertices_; ++i) {
        if (cores[i] != 0) {
            vertices_por_cor[cores[i]].push_back(i);
        }
    }

    for (int i = 1; i <= numero_de_cores; ++i) {
        cout << "Cor " << i << ":";
        for (int j = 0; j < vertices_por_cor[i].size(); j++) {
            cout << " " << vertices_por_cor[i][j];
        }
        cout << endl;
    }
}