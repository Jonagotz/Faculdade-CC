# Variáveis
CC = gcc
CFLAGS = -I include
BIN_DIR = bin
SRC_DIR = src
INC_DIR = include
DATA_DIR = data

# Nome do executável
TARGET = $(BIN_DIR)/main

# Arquivos fonte e objetos
SRCS = $(SRC_DIR)/main.c $(SRC_DIR)/readFile.c
OBJS = $(SRCS:.c=.o)

# Regras
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Limpeza
clean:
	rm -f $(OBJS) $(TARGET)

# Recriar diretórios se não existirem
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

# Cria o diretório de binário antes de compilar
$(TARGET): $(BIN_DIR) $(OBJS)

.PHONY: all clean
