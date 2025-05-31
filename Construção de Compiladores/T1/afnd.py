# --------- AFND -- afnd.py
import re
import tabulate # type: ignore
from states import STATE

class AFND:
    def __init__(self, path) -> None:
        self.tokens = []
        self.symbols = []
        self.states = []
        self.table = []
        self.new_state_counter = 0
        self.__get_data_from_file(path)

    def __get_data_from_file(self, path):
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("<"):
                    self._handle_grammar_rule(line)
                else:
                    self._handle_token(line)

    def _handle_grammar_rule(self, line):
        parts = line.split("::=")
        left = parts[0].strip()
        right = parts[1].strip()
        state_name = re.search(r"<(\w+)>", left).group(1)
        state = STATE(state_name)
        self.table.append(state)

        productions = [p.strip() for p in right.split("|")]
        for prod in productions:
            if prod == "ε":
                state.setFinal(True)
            elif "<" in prod:
                match = re.match(r"(\w+)<(\w+)>", prod)
                if match:
                    symbol, next_state = match.groups()
                    state.addNextState(symbol, next_state)
                    if next_state not in self.states:
                        self.states.append(next_state)
                    if symbol not in self.symbols:
                        self.symbols.append(symbol)
            else:
                symbol = prod
                new_index = f"q{self.new_state_counter}"
                self.new_state_counter += 1
                new_state = STATE(new_index)
                new_state.setFinal(True)
                self.table.append(new_state)
                state.addNextState(symbol, new_index)
                if symbol not in self.symbols:
                    self.symbols.append(symbol)

    def _handle_token(self, line):
        token = line.strip()
        if not token:
            return

        if self.table:
            initial_state = next(s for s in self.table if s.id == 0)
        else:
            initial_state = STATE(f"q{self.new_state_counter}")
            self.new_state_counter += 1
            self.table.append(initial_state)

        current_state = initial_state
        for char in token:
            if char not in self.symbols:
                self.symbols.append(char)
            new_index = f"q{self.new_state_counter}"
            self.new_state_counter += 1
            new_state = STATE(new_index)
            self.table.append(new_state)
            current_state.addNextState(char, new_index)
            current_state = new_state
        current_state.setFinal(True)


    def printAttributes(self):
        table = [["State"] + self.symbols]
        for state in self.table:
            row = [f"*{state.index}" if state.final else state.index]
            for symbol in self.symbols:
                found = False
                for transition in state.next_states:
                    if transition[0] == symbol:
                        row.append(transition[1:])
                        found = True
                        break
                if not found:
                    row.append("")
            table.append(row)
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="heavy_grid"))

    def printWithErrorState(self):
        table = [["State"] + self.symbols]
        table.append(["-1"] + ["-1"] * len(self.symbols))
        for state in self.table:
            row = [f"*{state.index}" if state.final else state.index]
            for symbol in self.symbols:
                found = False
                for transition in state.next_states:
                    if transition[0] == symbol:
                        row.append(transition[1:])
                        found = True
                        break
                if not found:
                    row.append("-1")
            table.append(row)
        print(tabulate.tabulate(table, headers="firstrow", tablefmt="heavy_grid"))

    def findState(self, index):
        for state in self.table:
            if state.index == index:
                return state
        return False