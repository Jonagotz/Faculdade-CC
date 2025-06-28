	.data
S:	.ascii ""
B:	.ascii ""	
	.text

main:
	li a7, 8
	li a1, 10
	li t0, 0
	la a0, S
	ecall
	j condicao

condicao:
	add    t1, t0, a0    # Add the byte offset for str[i]
   	lb     t2, 0(t1)     # Dereference str[i]
   	beqz   t2, fim        # if str[i] == 0, break for loop
corpo:
	li a7, 4
	la t3, B
	sb t2, 0(t3)
	la a0, B
	ecall
	j fim
atualiza:
	addi a2, a2, 4
	addi t0, t0, 4
	j condicao
	
fim:
	li a7, 10
	ecall