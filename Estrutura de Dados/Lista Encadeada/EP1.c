#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

typedef struct{
	int dia;
	int mes;
	int ano;
} Data;

struct _aluno{
  char matricula[10];
  char nome[40];
  Data dataNasc;
  float media;
  struct _aluno *next;
};
typedef struct _aluno Aluno;

int Contador(Aluno *first){ 
	int cont=0;
	Aluno *aux;
	for(aux=first; aux!=NULL; aux=aux->next){
		cont += 1;
	}
	return cont;
}

Aluno *deletaAluno(Aluno *first, char *MatDel){ 
	Aluno *aux, *prev = NULL;
	for(aux=first; aux!=NULL; aux=aux->next){
		if ((strcmp(aux->matricula, MatDel)) == 0){
			if (aux == first){ 
				first = aux->next; 
			}else{
				prev->next = prev->next->next;
			}
			free(aux);
		}
		prev = aux;
	}
	return first;
}

void printaAlunos(Aluno *p){ 
	Aluno *aux;
	for (aux=p;aux!=NULL;aux=aux->next){ 
		printf("%s, ", aux->matricula);
		printf("%s, ", aux->nome);
		printf("%d/%d/%d, ",aux->dataNasc.dia, aux->dataNasc.mes, aux->dataNasc.ano);
		printf("%.2f\n",aux->media); 
	}
}

void printaAlunosInverso(Aluno *p){ 
	Aluno *aux;
	if (p==NULL) return;
	aux=p;
	printaAlunosInverso(aux->next);
	printf("%s, ", aux->matricula);
	printf("%s, ", aux->nome);
	printf("%d/%d/%d, ",aux->dataNasc.dia, aux->dataNasc.mes, aux->dataNasc.ano);
	printf("%.2f\n",aux->media); 
}

void reseta(Aluno *p){
	Aluno *aux;
	if (p==NULL) return;
	aux=p;
	reseta(aux->next);
	free(aux);
	printf("-");
}

Aluno *pegaultimo(Aluno *p){
	Aluno *aux = p;
	for (aux=p; aux->next!=NULL; aux=aux->next); 
	return aux; 
}

Aluno *pegaaluno(Aluno *first){
	Aluno *p=malloc(sizeof(Aluno));
	Aluno *aux;
	scanf("%s", p->matricula);
	scanf("%s", p->nome);
	scanf("%d/%d/%d", &p->dataNasc.dia, &p->dataNasc.mes, &p->dataNasc.ano);
	scanf("%f",&p->media);
	p->next=NULL; 
	if (first==NULL)
	{
		first=p;
	} else {
		aux=pegaultimo(first); 
		aux->next=p;
	}
	return first;
}

int menu(){
	int num;
	
	scanf("%d",&num);
	return num;
}

int main(){

  int opcao, c;
	char matDel[10]; 
	Aluno *first=NULL;
	printf("1.Inserir aluno\n2.Deleta aluno\n3.Lista alunos\n4.Lista alunos inversament\n5.Conta quantos alunos\n0.Exit\n");
	opcao=menu();
  while (opcao!=0)
	{
		switch (opcao)
		{

			case 1: first=pegaaluno(first);
							break;
			case 2: if (first==NULL){
	      printf("Lista Vazia!\n");
	      break;
	    }
			scanf("%s", matDel);
			first = deletaAluno(first, matDel);
			break;

			case 3: if (first==NULL){
	      printf("Lista Vazia!\n");
	      break;
	    }
			printaAlunos(first);
			break;
			case 4: if (first==NULL){
	      printf("Lista Vazia!\n");
	      break;
	    }
			printaAlunosInverso(first);
			break;
			case 5: if (first==NULL){
	      printf("Lista Vazia!\n");
	      break;
	    }
			c = Contador(first);
			printf("%d\n", c);
			break;

		}
		opcao=menu(); 
	}
	reseta(first); 
  return 0;
}