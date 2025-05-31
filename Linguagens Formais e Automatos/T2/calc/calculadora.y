/* Calculadora com precedencia de operadores */
%{
#define YYSTYPE double
#include <math.h>
#include <stdio.h>
int yylex(void);  
int yyerror(const char *s);  
%}

%token NUM

%% /* Regras Gramaticais e Ações Semânticas */
input: /* vazio */
 | input line
;

line: '\n'
 | E '\n' { printf ("\t%.10g\n", $1); }
 | error '\n' { yyerrok; }
;

E:
E '+' T { $$ = $1 + $3; }
 | E '-' T { $$ = $1 - $3; }
 | T { $$ = $1; }
;

T: T '*' F { $$ = $1 * $3; }
 | T '/' F { $$ = $1 / $3; }
 | T '^' F { $$ = pow($1,$3); }
 | F { $$ = $1; }
;

F: NUM { $$ = $1; }
 | '(' E ')' { $$ = $2; }
;

%%

#include <ctype.h>
int yylex(void)
{
    int c;
    /* pula espaços em branco */
    while ((c = getchar()) == ' ' || c == '\t')
        ;

    /* processa numeros */
    if (c == '.' || isdigit(c))
    {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUM;
    }

    /* retorna end-of-file */
    if (c == EOF)
        return 0;

    /* retorna o caractere */
    return c;
}

/* Função chamada pelo yyparse quando ocorre algum erro */
int yyerror(const char *s)
{
    printf("%s\n", s);
}

int main(void)
{
    return yyparse();
}
