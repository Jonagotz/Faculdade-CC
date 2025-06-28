/*
 * Trabalho 2 - Coloração de grafos
 *
 * GEN254 - Grafos - 2025/1
 *
 * Nome:      Jonathan Götz Correa e Marco Lunardi
 * Matricula: 2121101052 e 2221101054
 */

#ifndef ARESTA_H

#define ARESTA_H

#include <string>

class Aresta {
public:
    const int v1;
    const int v2;

    Aresta(int v1, int v2);

    std::string to_string();
};

#endif /* ARESTA_H */
