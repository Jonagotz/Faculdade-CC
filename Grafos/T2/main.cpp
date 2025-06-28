/*
 * Trabalho 2 - Coloração de grafos
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nome:      Jonathan Götz Correa e Marco Lunardi
 * Matricula: 2121101052 e 2221101054
 */


 #include <iostream>
 #include "Grafo.h"
 #include "Aresta.h"

 using namespace std;
 
 void print_exception(const exception &e, int level = 0) {
    cerr << "exception: " << string(level, ' ') << e.what() << "\n";
    try {
        rethrow_if_nested(e);
    } catch(const std::exception& nested_exception) {
        print_exception(nested_exception, (level + 2));
    }
}
 
 int main() {
    
    try {
        int num_vertices, num_arestas;
    
        cin >> num_vertices >> num_arestas;
    
        Grafo g(num_vertices);
    
        int u, v;
        for (int i = 0; i < num_arestas; ++i) {
            cin >> u >> v;
            g.insere_aresta(Aresta(u, v));
        }
    
        char comando;
        cin >> comando;

        if (comando == 'P') {
            g.ConstroiColoracao_1();
        } else if (comando == 'A') {
            g.ConstroiColoracao_1();
            g.ConstroiColoracao_2();
        }
    }
    catch (const exception &e) {
        print_exception(e);
    }

    return 0;
}
