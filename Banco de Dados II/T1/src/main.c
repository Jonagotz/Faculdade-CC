#include <stdio.h>
#include "../include/readFile.h"

int main(int argc, char *argv[]) {
    if (argc > 1) {
        return readFile(argv[1]);
    } else {
        printf("Falta o parâmetro: nome lógico do arquivo\n");
        return 1;
    }
}
