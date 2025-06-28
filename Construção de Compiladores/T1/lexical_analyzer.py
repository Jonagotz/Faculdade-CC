from afd import *
from tabulate import tabulate
class LexicalAnalyzer:
    def __init__(self, afd):    
        self.afd = afd
        self.symbol_table = []
        self.errors = []

    def tokenize(self, line):
        delimiters = [':', '+', '=', '<']
        result = []
        current_token = ''
        for char in line:
            if char.isspace():
                if current_token:
                    result.append(current_token)
                    current_token = ""
            elif char in delimiters:
                if current_token:
                    result.append(current_token)
                    current_token = ""
                result.append(char)
            else:
                current_token += char
        if current_token:
            result.append(current_token)
        return result
                        
                        
    def classify_token(self, token):
        if token in ['count']:
            return 'VARIABLE'
        elif token in ['while', '=', ':']:
            return 'KEYWORD'
        elif token in ['<', '+']:
            return 'OPERATOR'
        elif token in ['0', '1', '5']:
            return 'NUMBER'
        else:
            return 'INVALID'

    def transitions(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        path = []
        current_state = self.afd['initial_state']
        
        
        for line_number, line in enumerate(lines, 1):
            if not line.strip():  # Pula linhas vazias
                continue
            tokens = self.tokenize(line)
            for token in tokens:
                for char in token:
                    if (current_state in self.afd['transitions'] 
                        and char in self.afd['transitions'][current_state]):
                        
                        next_state = self.afd['transitions'][current_state][char]
                        path.append(next_state)
                        current_state = next_state
                    else:
                    # Transição inválida
                        self.errors.append({
                            'line': line_number,
                            'token': token,
                            'message': f'Não há transição para o token "{token}" no estado {current_state}'
                        })
                        break
                label = self.classify_token(token)
                self.symbol_table.append({
                    'line': line_number,
                    'identifier': token,
                    'label': label
                })      
        if current_state not in self.afd['final_states']:
            self.errors.append({
                'line': line_number,
                'token': '',
                'message': f'Processo terminal sem um estado final {current_state}'
            })
                
        return True, path, self.errors    
    
    def print_afd(self):
        # Print the alphabet
        print(' ')
        
        states = sorted(self.afd['transitions'].keys(), key=lambda x: int(x[1:]))
        
        alphabet = sorted(self.afd['alphabet'])
        
        table_data = []
        for state in states:
            row = [state]  
            for symbol in alphabet:
                next_state = ""
                for char in symbol: 
                    if state in self.afd['transitions'] and char in self.afd['transitions'][state]:
                        next_state = self.afd['transitions'][state][char]
                        break  
                row.append(next_state)
            table_data.append(row)
        
        headers = ["Estado"] + alphabet
        
        print("\nAFD:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        print("\nEstado Inicial:", self.afd['initial_state'])
        
        print("\nEstado final:", ', '.join(self.afd['final_states']))
        
        
          
    def print_symbol_table(self):
        if not self.errors:
            print("Nenhum erro encontrado.")
        for error in self.errors:
            print(f"Linha {error['line']}: Erro com o token'{error['token']}' - {error['message']}")
        print("\nTabela:")
        print("Linha\tIdentificador\tRótulo")
        print("-" * 40)
        for symbol in self.symbol_table:
            print("{}\t{}\t\t{}".format(
                symbol['line'],
                symbol['identifier'],
                symbol['label']
            ))