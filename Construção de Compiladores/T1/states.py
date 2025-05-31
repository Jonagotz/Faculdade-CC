# CLASSE DE ESTADOS -- states.py

import itertools

class STATE:
    id_iter = itertools.count()
    def __init__(self, index):
        self.index = index
        self.id = next(self.id_iter)
        self.next_states: list[list[str, str]] = []
        self.final = False

    def addNextState(self, symbol, nextState):
        for transition in self.next_states:
            if transition[0] == symbol:
                transition.append(nextState)
                return
        self.next_states.append([symbol, nextState])

    def setFinal(self, bool):
        self.final = bool

    def printStates(self):
        for transition in self.next_states:
            print(transition)