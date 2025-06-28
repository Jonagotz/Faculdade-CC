	.data
A:	.word 	10
S: 	.ascii ""

	.text

main:
	la t0, 0(S)
	j ler_string

ler_string:
	li a7, 8
	la a1, A
	ecall
	j condicao

condicao:
	beqz  a0, fim
corpo:
	lb t0, 0(a0)
	bne 0(a0), 
atualiza:
	addi a0, a0, 1
	addi a1, a1, -1
	j condicao
fim:
	li a7, 10
	ecall
	