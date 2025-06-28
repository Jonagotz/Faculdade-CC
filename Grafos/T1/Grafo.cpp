/*
 * Trabalho 1 - Zoologico
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nomes:      Jonathan Gotz Correa e Luna Matana Fortes
 * Matriculas: 2121101052 e 2221101004
 */

#include "Grafo.h"
#include <exception>
#include <stdexcept>
#include <string>
#include <iostream>
#include <stack>
#include "Retorno.h"

using namespace std;

Grafo::Grafo(int num_vertices) {
    if (num_vertices <= 0) {
        throw(invalid_argument("Erro no construtor Grafo(int): o numero de "
            "vertices " + to_string(num_vertices) + " eh invalido!"));
    }

    num_vertices_ = num_vertices;
    num_arestas_ = 0;

    matriz_adj_.resize(num_vertices);
    for (int i = 0; i < num_vertices; i++) {
        matriz_adj_[i].resize(num_vertices, 0);
    }
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

void Grafo::insere_aresta(Aresta e) {
    try {
        valida_aresta(e);
    } catch (...) {
        throw_with_nested(runtime_error("Erro na operacao "
            "insere_aresta(Aresta): a aresta " + e.to_string() + " eh "
            "invalida!"));
    }

    if (!tem_aresta(e) && (e.v1 != e.v2)) {
        matriz_adj_[e.v1][e.v2] = 1;
        matriz_adj_[e.v2][e.v1] = 1;

        num_arestas_++;
    }
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

void Grafo::valida_vertice(int v) {
    if ((v < 0) || (v >= num_vertices_)) {
        throw out_of_range("Indice de vertice invalido: " + to_string(v));
    }
}

void Grafo::valida_aresta(Aresta e) {
    valida_vertice(e.v1);
    valida_vertice(e.v2);
}

bool Grafo::eh_bipartido_1(int v, int marcado[]) {
    int conjunto_a[num_vertices_];
    int conjunto_b[num_vertices_];
    for(int i =0; i< num_vertices_; i++) {
        conjunto_a[i] = -1;
        conjunto_b[i] = -1;
    }
    Retorno t(0, 0, false);
    Retorno r = particiona(marcado, conjunto_a, conjunto_b, t);
    return r.pode_adicionar;
}

Retorno Grafo::particiona(int marcado[], int conjunto1[], int conjunto2[], Retorno r){
    bool esta_vazio = true;
    int v;
    //remove um vértice / marca um vértice como visitado no vetor marcado
    for(int ab = 0; ab < num_vertices_; ab++){
        if(marcado[ab] == 0){
            esta_vazio = false;
            marcado[ab] = 1;
            v = ab;
            break;
        }
    }
    //verifica se todos os vértices foram removidos, caso sim retorna true
    if(esta_vazio){
        r.pode_adicionar = true;
        return r;
    }

    //chama a função recursivamente
    Retorno resultado = particiona(marcado, conjunto1, conjunto2, r);
    if(!resultado.pode_adicionar){
        r.pode_adicionar = false;
        return r;
    }

    //Tenta adicionar no conjunto 1
    if (pode_adicionar(v, conjunto1)){
        //adiciona no conjunto
        conjunto1[resultado.posicao1] = v;
        // cout << "Adicionou ao conjunto1 " << v << "\n";
        //Ajusta a posição no objeto de retorno
        resultado.posicao1++;
        resultado.pode_adicionar = true;
        return resultado;
    }
    //tenta adicionar no conjunto dois
    else if(pode_adicionar(v, conjunto2)){
        //adicionar no conjunto dois
        conjunto2[resultado.posicao2] = v;
        // cout << "adicionou ao conjunto2 " << v << "\n";
        //ajusta os valores do objeto de retorno
        resultado.pode_adicionar = true;
        resultado.posicao2++;
        return resultado;
    }

    //Se não conseguiu adicionar em nenhum conjunto, ajusta o objeto de retorno e retorna false
    resultado.pode_adicionar = false;
    return resultado;
}

bool Grafo::pode_adicionar(int v, int conjunto[]){
    for(int coluna = 0; coluna < num_vertices_; coluna++){
        if(v == coluna)
            continue;
        if(matriz_adj_[v][coluna] == 1){
            if(verifica_esta_contido(coluna, conjunto, num_vertices_))
                return false;
        }
    }
    return true;
}

void Grafo::imprime_vetor(int vetor[], int tamanho){
    for(int i = 0; i < tamanho; i++){
        cout << "Vetor na casa " << i << " é igual a " << vetor[i] << "\n";
    }
}

bool Grafo::verifica_esta_contido(int valor, int conjunto[], int tamanho){
    for(int i = 0; i < tamanho; i++){
        if(conjunto[i] == valor){
            return true;
        }
    }
    return false;
}

bool Grafo::eh_bipartido_2(int v, int marcado[]){
    stack<int> pilha;
    pilha.push(v);
    int count = 1;
    //inicializa o contador dos conjuntos e os conjuntos
    int i = 0;
    int conjunto_a[num_vertices_];
    int conjunto_b[num_vertices_];
    for(int i = 0; i< num_vertices_; i++) {
        conjunto_a[i] = -1;
        conjunto_b[i] = -1;
    }
    while (!pilha.empty()) {
        int w = pilha.top();
        pilha.pop();
        if (marcado[w] == 0) {
            marcado[w] = 1;
            //adiciona o vértice a um dos conjuntos
            if(count % 2 == 1){
                conjunto_a[i] = w;
            } else {
                conjunto_b[i] = w;
                //incrementa o contador dos conjuntos a cada duas execuções
                i++;
            }
            for (int u = (num_vertices_ - 1); u >= 0; u--)
            {
                if (matriz_adj_[w][u] != 0){
                    if (marcado[u] == 0)
                        pilha.push(u);
                    else {
                        //se os vizinhos do vértice já foram visitados, verifica se o vizinho está no mesmo conjunto do vértice
                        if(count % 2 == 1){
                            if(verifica_esta_contido(u, conjunto_a, num_vertices_))
                                return false;
                        } else {
                            if(verifica_esta_contido(u, conjunto_b, num_vertices_))
                                return false;
                        }
                    }
                }   
            }
        }
        count++;
    }
  return true;
}
