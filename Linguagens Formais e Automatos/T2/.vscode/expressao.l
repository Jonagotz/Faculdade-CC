%{
#include "expressao.tab.h" // Cabeçalho gerado pelo Bison
%}

%option noyywrap

%%

"TRUE"      { return TRUE; }
"FALSE"     { return FALSE; }
"AND"       { return AND; }
"OR"        { return OR; }
"NOT"       { return NOT; }
"("         { return LPAREN; }
")"         { return RPAREN; }
"exit"      { return EXIT; }
[ \t\n]+    { /* Ignorar espaços, tabs e quebras de linha */ }
.           { printf("Caractere inválido: %s\n", yytext); }

%%