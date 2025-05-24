#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct site
{
    char dom[61];
    struct site *next;
};
typedef struct site Site;

typedef struct
{
    Site *top;
} Stack;

int esta_vazio(Stack *stack);

void bota(Stack *stack, char dom[61]);

void livra(Stack *stack, char *dom);

int popula(Stack *stack, char *dom);


int main()
{
    Stack *stack = malloc(sizeof(Stack));
    stack->top = NULL;

    while (1)
    {
        char dom[61];
        scanf("%s", dom);

        if (strcmp(dom, "E") == 0)
        {
            livra(stack, dom);
            break;
        }
        else if (strcmp(dom, "B") == 0)
        {

            if (!esta_vazio(stack))
                popula(stack, dom);
        }
        else
            bota(stack, dom);
    }

    return 0;
}

void bota(Stack *stack, char *dom)
{

    Site *newElement = malloc(sizeof(Site));

    newElement->next = NULL;
    strcpy(newElement->dom, dom);
    newElement->next = stack->top;
    stack->top = newElement;
}

int esta_vazio(Stack *stack)
{
    if (stack->top == NULL)
    {
        printf("Vazio!\n");
        return 1;
    }
    return 0;
}

int popula(Stack *stack, char *dom)
{
    Site *aux;
    char *aux2;

    aux = stack->top;
    stack->top = stack->top->next;
    aux2 = aux->dom;
    printf("%s\n", aux2);
    free(aux);
    return *aux2;
}

void livra(Stack *stack, char *dom)
{
    Site *aux = stack->top, *prev;

    while (aux != NULL)
    {
        prev = aux;
        aux = aux->next;
        free(prev);
    }

    if (stack->top != NULL)
    {
        for (aux = stack->top; aux != NULL; aux = aux->next)
        {
            printf("@\n");
        }
        free(stack);
    }
    else
        printf("!\n");
}