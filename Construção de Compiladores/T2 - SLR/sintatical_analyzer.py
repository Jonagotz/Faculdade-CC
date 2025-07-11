import csv
from tabulate import tabulate
from lexical_analyzer import *
from afd import afd

import re
import os

class TreeNode:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def print_tree(self, prefix="", is_last=True):
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(self.label))
        prefix += "    " if is_last else "│   "
        for i, child in enumerate(self.children):
            is_last_child = (i == len(self.children) - 1)
            if isinstance(child, TreeNode):
                child.print_tree(prefix, is_last_child)
            else:
                print(prefix + ("└── " if is_last_child else "├── ") + str(child))

class SintaticalAnalyzer:

    def __init__(self, parsing_table_file):
        self.parsing_table = self.load_parse(parsing_table_file)
        self.state_stack = [0]
        self.symbol_stack = []

        self.symbol_table = {}
        self.current_expression_value = None
        self.current_variable_stack = []
        self.derivation_stack = []

        self.reducoes = {
            0: 1,  # PROGRAM' -> SEQUENCE
            1: 2,  # SEQUENCE -> SEQUENCE STATEMENT
            2: 1,  # SEQUENCE -> STATEMENT  
            3: 5,  # STATEMENT -> let IDENT = STATEMENT ;
            4: 1,  # STATEMENT -> true
            5: 1,  # STATEMENT -> false
            6: 1,  # STATEMENT -> IDENT
            7: 5,  # STATEMENT -> if STATEMENT { STATEMENT }
        }
        self.producoes_goto = {
            0: "PROGRAM'",
            1: "SEQUENCE",
            2: "SEQUENCE",
            3: "STATEMENT",
            4: "STATEMENT",
            5: "STATEMENT",
            6: "STATEMENT",
            7: "STATEMENT",
        }

    def load_parse(self, parsing_table_file):
        parsing_table = {}
        with open(parsing_table_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            for row in reader:
                state = int(row[0])
                parsing_table[state] = {}
                for index, action in enumerate(row[1:], 1):
                    if action:
                        parsing_table[state][headers[index]] = action

        return parsing_table

    def parse(self, tokens):
        log_tabela = []
        self.input_stack = tokens + [{'label': '$'}]
        self.log_tabela = log_tabela
        self.derivation_stack = [TreeNode(t['label']) for t in self.input_stack if t['label'] != '$']
        while True:
            estado_atual = self.state_stack[-1]
            token_data = self.input_stack[0]
            token = token_data['label']
            if token == 'INVALID':
                self.error(f"Syntax error at line {token_data['line']}: {token}")
                return
            action = self.parsing_table.get(estado_atual, {}).get(token, None)
            
            log_tabela.append([
                self.pilha_formatada(),
                ' '.join([t['label'] for t in self.input_stack]), action
            ])

            if token == 'INVALID':
                self.error(f"Token inválido '{token}'", token_data.get('line'), tipo="Erro léxico")
                return
            if action is None:
                print(tabulate(log_tabela, headers=["Pilha", "Fita", "Ação"], tablefmt="grid"))
                self.error(f"Token inesperado '{token}' no estado {estado_atual}", token_data.get('line'))
                return
            # FAZ SHIFT
            if action.startswith('s'):
                next_state = int(action[1:])
                consumed_token = self.input_stack.pop(0)
                self.symbol_stack.append(consumed_token)
                self.state_stack.append(next_state)
                print(f"Shifted to state {next_state}")
            # FAZ REDUCE
            elif action.startswith('r'):
                print(tabulate(log_tabela, headers=["Pilha", "Fita", "Ação"], tablefmt="grid"))
                production_number = int(action[1:])
                if not self.reduce(production_number):
                    return
            elif action == 'acc' or action == '$' and action == 'acc':
                print(tabulate(log_tabela, headers=["Pilha", "Fita", "Ação"], tablefmt="grid"))
                print("Input aceito.\n")
                print("Árvore de derivação:")
                if self.derivation_stack:
                    self.derivation_stack[-1].print_tree()
                return
            else:
                print(tabulate(log_tabela, headers=["Pilha", "Fita", "Ação"], tablefmt="grid"))
                self.error(f"Ação inválida '{action}' no estado {estado_atual}", token_data.get('line'))
                return

    def error(self, message, line=None, tipo="Erro sintático"):
        if line is not None:
            print(f"{tipo} na linha {line}: {message}")
        else:
            print(f"{tipo}: {message}")

    def reduce(self, production):
        producao = self.reducoes[production]
        producao_goto = self.producoes_goto[production]
        if producao is None or producao_goto is None:
            self.error(f"Sem informação semantica para produção {production}", self.input_stack.get('line'))
            return False

        children = []
        for _ in range(producao):
            self.state_stack.pop()
            self.symbol_stack.pop()
            children.insert(0, self.derivation_stack.pop())

        prod_map = {
            0: "PROGRAM'",
            1: "SEQUENCE",
            2: "SEQUENCE",
            3: "STATEMENT",
            4: "STATEMENT",
            5: "STATEMENT",
            6: "STATEMENT",
            7: "STATEMENT",
        }
        node_label = prod_map[production]
        node = TreeNode(node_label, children)
        self.derivation_stack.append(node)

        goto_state = self.goto(self.state_stack[-1], producao_goto)
        self.state_stack.append(goto_state)
        self.symbol_stack.append(producao_goto)
        

        if goto_state is None:
            self.error(f"Error: Sem estado goto para {producao_goto} do estado {self.state_stack[-1]}", self.input_stack.get('line'))
            return False

        # print(f"Pós redução - Estado da pilha: {self.state_stack}")
        # print(f"Symbol stack: {self.symbol_stack}")
        return True

    def goto(self, current_state, non_terminal):
        action = self.parsing_table.get(current_state, 
                                        {}).get(non_terminal, None)
        print(f"GOTO: estado {current_state}, não-terminal '{non_terminal}' -> ação: {action}")
        if action and action.isdigit():
            return int(action)
        else:
            self.error(f"GOTO não encontrado para estado {current_state} e não-terminal '{non_terminal}'", self.input_stack.get('line'))
            return None

    def pilha_formatada(self):
        pares = []
        for estado, simbolo in zip(self.state_stack[:-1], self.symbol_stack):
            if isinstance(simbolo, dict):
                label = simbolo.get('label', str(simbolo))
            else:
                label = str(simbolo)
            pares.append(f"{estado} {label}")
        if len(self.state_stack) > len(self.symbol_stack):
            pares.append(str(self.state_stack[-1]))
        return ' '.join(pares)
    
   # def update_symbol_table(self, production, reduced_tokens):
   #     # Produção 4: E -> let var = E ;
   #    print(production)
   #     if production == 4:
   #         # Espera-se: [{'label': 'let'}, {'label': 'IDENT'}, {'label': '='}, {'label': valor}, {'label': ';'}]
   #         current_variable = self.current_variable_stack.pop()
            # Busca o valor atribuído (o último token relevante)
   ##         print(current_variable)
     #       var_value = None
   #         for t in reduced_tokens:
    #            if t['label'] not in ['let', '=', ';']:
    #               var_value = t['label']
    #                print(var_value, 'kkkkkkkkkkkkkkkk')
     #       if current_variable in self.symbol_table.keys():
    #            self.error(f"Tried to Reassign variable '{current_variable}'")
    #            return False
     #       else:
   #             self.symbol_table[current_variable] = {
    #                "value": var_value,
    #                "type": "bool" if var_value in ['true', 'false'] else "unknown"
   #             }
#
 #       # Produção 7: E -> var (uso de variável)
  #      elif production == 7:
   #         current_variable = self.current_variable_stack.pop()
    #        print(current_variable, 'AAAAAAAAAAAAAA')
     #       if current_variable in self.symbol_table.keys():
     #           self.current_expression_value = self.symbol_table[current_variable]
      #      else:
       #         self.error(f"Tried to Invoke No Declared Variable '{current_variable}'")
        #        return False
#
 #       else:
  #          print('PASSED')
   #         pass

if __name__ == '__main__':
    parsing_table_file = 'parsing_table.csv'
    # Provide actual productions dict matching parsing_table
    from lexical_analyzer import LexicalAnalyzer
    lexer = LexicalAnalyzer(afd)
    # Get tokens from lexical analyzer;
    tokens = lexer.transitions('inputs/input.in')[3]
    parser = SintaticalAnalyzer(parsing_table_file)
    result = parser.parse(tokens)
    # print(parser.symbol_table)