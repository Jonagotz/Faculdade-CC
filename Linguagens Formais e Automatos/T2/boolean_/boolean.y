%{
#include <stdio.h>
#include <string.h>

#define YYSTYPE int

int yylex(void);
int yyerror(const char *s);
%}

%token TRUE FALSE
%token AND OR NOT

%%

input:
    | input line
    ;

line:
      '\n'
    | expr '\n' { printf("Resultado: %s\n", $1 ? "TRUE" : "FALSE"); }
    | error '\n' { yyerror("Expressão inválida"); yyerrok; }
    ;

expr:
      TRUE         { $$ = 1; }                     
    | FALSE        { $$ = 0; }                     
    | expr AND expr { $$ = $1 && $3; }             
    | expr OR expr  { $$ = $1 || $3; }             
    | NOT expr      { $$ = !$2; }                  
    | '(' expr ')'  { $$ = $2; }                   
    ;

%%

#include <ctype.h>

int yylex(void) {
    int c;

    while ((c = getchar()) == ' ' || c == '\t')
        ;

    if (isalpha(c)) {
        char buffer[16];
        int i = 0;

        do {
            buffer[i++] = c;
            c = getchar();
        } while (isalpha(c) && i < 15);
        buffer[i] = '\0';

        ungetc(c, stdin);

        if (strcmp(buffer, "TRUE") == 0) return TRUE;
        if (strcmp(buffer, "FALSE") == 0) return FALSE;
        if (strcmp(buffer, "AND") == 0) return AND;
        if (strcmp(buffer, "OR") == 0) return OR;
        if (strcmp(buffer, "NOT") == 0) return NOT;

        return 0; 
    }

    if (c == EOF) return 0;
    return c;
}

/* Função para reportar erros */
int yyerror(const char *s) {
    printf("Erro: %s\n", s);
    return 0;
}

int main(void) {
    printf("Digite expressões booleanas (ex.: TRUE AND NOT FALSE):\n");
    return yyparse();
}
