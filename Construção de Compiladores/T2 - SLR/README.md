# Projeto: Reconhecedor Sintático

## Objetivo
Construção de um analisador sintático para reconhecimento de uma linguagem hipotética cujos tokens foram definidos no Projeto 1.

---

### Etapa 1 (70% da nota):

- Construir as regras sintáticas da linguagem: GLC;
- Aplicar eliminação de inúteis e fatoração na GLC;
- Construção do conjunto de itens válidos, transições e follow;
- Construção da tabela de parsing SLR ou LALR
  - SLR Parser Generator (http://jsmachines.sourceforge.net/machines/slr.html)
  - GoldParser (http://www.goldparser.org/)
- Implementação do algoritmo de mapeamento da tabela para reconhecimento sintático
- Gerenciamento da tabela de símbolos (suporte para as próximas etapas)
- Integrar procedimentos (ações semânticas – TDS) para os seguintes itens:
  - Tratamento de erros (pelo menos o tipo de erro e linha de ocorrência)
  - Adição de atributos aos símbolos (id de tokens reconhecidos)
  - Valores nos atributos
- Entrada: fita de saída do reconhecedor léxico
- Saída: aceite ou mensagem(ns) de erro(s) sintático(s)
- Adicionar informações na tabela de símbolos para uso nas etapas subsequentes (a definir em cada projeto)

---

### Etapa 2 (10% da nota):

- Definir uma característica semântica cujas informações adicionadas na TS sejam suficientes para a análise
- Implementar a análise semântica da característica especificada
- Entrada: código / tabela de símbolos
- Saída: aceite ou mensagem(ns) de erro(s) semântico(s)

---

### Etapa 3 (10% da nota):

- Cada redução de uma produção (reconhecimento de uma estrutura sintática) é seguida de uma chamada a uma ação que gera o correspondente trecho de código intermediário com os respectivos rótulos dos identificadores, constantes, etc.
- Basta aplicar a geração de código intermediário para uma das regras sintáticas (demonstração)
- Entrada: reconhecimento de uma estrutura sintática conforme regras de produção
- Saída: código intermediário

---

### Etapa 4 (10% da nota):

- Aplicar uma estratégia de otimização de código sobre o código intermediário gerado na etapa anterior
- Entrada: código intermediário
- Saída: código intermediário otimizado

---

## Texto

Elaborar texto entre 2 e 5 páginas contendo:

- Título, autores e instituição
- Resumo: breve apresentação do teor do texto
- Introdução: Contextualização sobre reconhecedores sintáticos (propósitos, aplicação e características), apresentação de problema e objetivo do trabalho.
- Referencial teórico: Breve explanação sobre os conceitos, técnicas e/ou teoremas fundamentais para o desenvolvimento do trabalho.
- Implementação e resultados: Apresentação dos detalhes de especificação/implementação do analisador sintático e estudo de caso para validação.
- Conclusões: O que foi feito, dificuldades, resultados finais e perspectivas para continuidade do trabalho (por exemplo, sugerir alterações futuras para utilizar a implementação no ensino de compiladores).