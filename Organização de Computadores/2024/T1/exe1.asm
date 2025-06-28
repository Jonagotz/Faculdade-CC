	.data
A:	.word 	0
B:	.word   0
C:	.word	0

	.text
	
main:
	jal ler_variaveis
	jal busca_maior
	
ler_variaveis:
	li	a7, 5
	ecall
	la	t0, A
	sw	a0, 0(t0)
	
	li	a7, 5
	ecall
	la	t0, B
	sw	a0, 0(t0)
	
	li	a7, 5
	ecall
	la	t0, C
	sw	a0, 0(t0)
	
	la	t0, A
	lw	a0, 0(t0)
	
	la	t0, B
	lw	a1, 0(t0)
	
	la	t0, C
	lw	a2, 0(t0)
	ret
	
busca_maior:
	la t0, A
	la t1, B
	la t2, C
	
	lw a0, 0(t0)
	lw a1, 0(t1)
	lw a2, 0(t2)
	
	bgt a0, a1, verifica_a
	bgt a1, a0, verifica_b
	bgt a2, a0, verifica_c
	j not_triangulo
	
verifica_a:
	bgt a0, a2, retorna_a
	j retorna_c
	
retorna_a:
	add a0, a0, zero
	j verifica_triangulo
	
verifica_b:
	bgt a1, a2, retorna_b
	j retorna_c
	
retorna_b:
	add a0, a1, zero
	lw a1, 0(t0)
	j verifica_triangulo
	
verifica_c:
	bgt a2, a1, retorna_c
	j retorna_b

retorna_c:
	add a0, a2, zero
	lw a2, 0(t0)
	j verifica_triangulo

verifica_triangulo:
	add a1, a1, a2
	blt a0, a1, triangulo
	j not_triangulo

not_triangulo:
	li a7, 1
	li a0, 0
	ecall
	j end
	
triangulo:
	li a7, 1
	li a0, 1
	ecall
	j end

end:
	li a7, 10
	ecall
