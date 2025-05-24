PILHA

Você vai implementar um programa que simule o botão back (voltar) de um browser. As entradas são endereços da Internet que foram acessados pelo usuário (sequência de caracteres sem espaço) e o caractere B. Quando o caractere B for encontrado, o último endereço acessado deve ser impresso. Caso não haja mais endereços para acessar, a mensagem “Vazio” deve ser impressa.
O programa é encerrado com quando o caractere ‘E’. Neste ponto você deve limpar a pilha, caso a pila tenha elementos imprima ‘@’ para cada elemento que você limpar. Caso o programa acabe e a pilha já esteja vazia imprima ‘!’.

Entrada
A entrada contém uma série de casos de teste, um por linha. Cada caso é constituído de uma String (conjunto de caracteres) com tamanho n (1 < n < 60). A entrada encerra quando receber o caractere ‘E’. Caso a entrada seja o caracter ‘B’ um endereço deve ser retirado da pilha. Caso a entrada seja diferente desta, o valor deverá ser adicionado na pilha.

Saída
A saída deverá ser impressa conforme os exemplos fornecidos abaixo. Cada saída possui uma relação com a operação solicitada, e ao final de cada uma deve haver uma quebra de linha.
Obs: Você receberá um conjunto de entradas e saídas. Lembre-se que para encaminhar os elementos a sua solução você pode utilizar os direcionadores de entrada do shell. Ex. Se seu programa se chama ‘solucao’ e seus arquivos de entrada e saída, ‘entrada1.in’ e ‘saida1.out’ respectivamente, você pode utilizar os seguintes comandos para verificar se a solução está ok
./solucao < entrada1.in > saidaPrograma.out
diff saidaPrograma.out saida1.out
Obs2: Se você estiver utilizando Windows, tome cuidado com as quebras de linha.

Exemplo 1 (entradas em azul, saídas em vermelho)
www.eu.com
www.uffs.edu.br
lequipe.fr
B
B
g1.com.br
B
B
B
E
lequipe.fr
www.uffs.edu.br
g1.com.br
www.eu.com
Vazio
!

Exemplo 2 (entradas em azul, saídas em vermelho)
chipofftheoldwalk.com.br
B
B
B
B
putwalkinit.com.gm
onthegamepage.info
inthegameofthefather.info.br
B
B
B
B
B
rudehilariousblog.info.br
walkfree.gov.eu
B
chipofftheoldwalk.com.br
Vazio
Vazio
Vazio
inthegameofthefather.info.br
onthegamepage.info
putwalkinit.com.gm
Vazio
Vazio
walkfree.gov.eu
@