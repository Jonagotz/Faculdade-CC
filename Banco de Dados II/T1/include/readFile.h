#ifndef READFILE_H
#define READFILE_H

typedef struct {
    int id_arquivo;
    char nome_log[20];
    char nome_fisico[20];
} TableDicEntry;

typedef struct {
    int id_arquivo_att;
    char nome_att[20];
    char tipo;
    char opcional;
    int tamanho;
} Atributo;

int readFile(const char *nomeLog);
void printData(const char *nomeFisico, Atributo *atributos, int num_atributos);

#endif 
