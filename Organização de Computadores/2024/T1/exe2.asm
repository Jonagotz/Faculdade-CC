	.data
A:      .word   10
S:      .ascii  ""

	.text

main:
    	la a0, S
    	li a1, 10  # Supondo que o tamanho máximo da string seja 10 caracteres
    	jal palindromo
	
    	# Verificando o resultado
    	beqz a0, nao_palindromo
    	# Se a0 != 0, então é um palíndromo
    	li a7, 10
    	ecall
	
nao_palindromo:
    	# Se a0 == 0, então não é um palíndromo
    	li a7, 11
    	ecall

palindromo:
    	# Argumentos:
    	# a0: Endereço inicial da string
    	# a1: Tamanho da string

    	# Setup inicial
    	add a2, a0, a1  # Endereço final da string
    	addi a1, a1, -1 # Decrementa o tamanho para começar no último caractere

    condicao_loop:
        blt a0, a2, fim # Verifica se já chegamos ao final da string
        beq a0, a2, palindromo_found # Se já percorremos toda a string, é um palíndromo

        lb t0, 0(a0)    # Caractere atual
        lb t1, 0(a1)    # Caractere correspondente ao final

        bne t0, t1, nao_palindromo # Se os caracteres não são iguais, não é palíndromo

        addi a0, a0, 1  # Avança para o próximo caractere
        addi a1, a1, -1 # Retrocede para o caractere anterior
        j condicao_loop

    palindromo_found:
        li a0, 1 # Retorna 1 em a0 (é um palíndromo)
        ret

    fim:
        li a0, 0 # Se chegamos aqui, não é um palíndromo
        ret
