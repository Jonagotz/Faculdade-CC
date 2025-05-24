#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/readFile.h"

#define TABLE_DIC "../data/table.dic"
#define ATT_DIC "../data/att.dic"

int readFile(const char *nomeLog) {
    FILE *tableFile = fopen(TABLE_DIC, "r");
    FILE *attFile;
    TableDicEntry tableEntry;
    Atributo atributos[100];
    int num_atributos = 0;
    int found = 0;

    if (tableFile == NULL) {
        perror("Erro ao abrir table.dic");
        return -1;
    }

    while (fscanf(tableFile, "%d %19s %19s", &tableEntry.id_arquivo, tableEntry.nome_log, tableEntry.nome_fisico) != EOF) {
        if (strcmp(nomeLog, tableEntry.nome_log) == 0) {
            found = 1;
            attFile = fopen(ATT_DIC, "r");
            if (attFile == NULL) {
                perror("Erro ao abrir att.dic");
                fclose(tableFile);
                return -1;
            }

            while (fscanf(attFile, "%d %19s %c %c %d", &atributos[num_atributos].id_arquivo_att,
                          atributos[num_atributos].nome_att, &atributos[num_atributos].tipo,
                          &atributos[num_atributos].opcional, &atributos[num_atributos].tamanho) != EOF) {
                if (atributos[num_atributos].id_arquivo_att == tableEntry.id_arquivo) {
                    num_atributos++;
                }
            }
            fclose(attFile);

            printData(tableEntry.nome_fisico, atributos, num_atributos);
            break;
        }
    }

    fclose(tableFile);
    if (!found) {
        printf("Nome lógico não encontrado.\n");
        return -1;
    }

    return 0;
}

void printData(const char *nomeFisico, Atributo *atributos, int num_atributos) {
    FILE *dataFile = fopen(nomeFisico, "r");
    if (dataFile == NULL) {
        perror("Erro ao abrir o arquivo de dados");
        return;
    }

    int totalWidth = 0;
    for (int i = 0; i < num_atributos; i++) {
        totalWidth += atributos[i].tamanho + 3;
    }

    printf("+");
    for (int i = 0; i < totalWidth; i++) printf("-");
    printf("+\n");

    printf("|");
    for (int i = 0; i < num_atributos; i++) {
        printf(" %-*s |", atributos[i].tamanho, atributos[i].nome_att);
    }
    printf("\n");

    printf("+");
    for (int i = 0; i < totalWidth; i++) printf("-");
    printf("+\n");

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), dataFile)) {
        char *token = buffer;
        printf("|");
        for (int i = 0; i < num_atributos; i++) {
            char value[100] = {0};
            strncpy(value, token, atributos[i].tamanho);
            value[atributos[i].tamanho] = '\0';

            for (int j = 0; j < atributos[i].tamanho; j++) {
                if (value[j] == '\n' || value[j] == '\r') {
                    value[j] = '\0';
                    break;
                }
            }

            printf(" %-*s |", atributos[i].tamanho, value);
            token += atributos[i].tamanho;
        }
        printf("\n");
    }

    printf("+");
    for (int i = 0; i < totalWidth; i++) printf("-");
    printf("+\n");

    fclose(dataFile);
}
