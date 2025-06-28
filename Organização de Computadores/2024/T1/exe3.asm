	.data
vector:	.word 	-5, 4, 2, -11, 9
quebra_linha: .ascii "\n"
	.text

main:
	la t0, vector		# lê endereço do vetor
	la t1, quebra_linha
	li a1, 16		# Tamanho do deslocamento máximo
	li a2, 0		# Tamanho do deslocamento mínimo
	j condicao

condicao:
	bgt a2, a1, fim		# a2 = deslocamento atual | a1 = deslocamento máximo
corpo:
	li a7, 1
	lw a0, 0(t0)
	ecall
	li a7, 4
	la a0, quebra_linha
	ecall
atualiza:
	addi a2, a2, 4
	addi t0, t0, 4
	j condicao
	
fim:
	li a7, 10
	ecall