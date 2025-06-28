afd = {
    'transitions': {
            'q0': {'i': 'q1', 'l': 'q2', 't': 'q3', 'f': 'q4', '{': 'q5', '}': 'q6', '=': 'q7'},
            'q1': {'f': 'q8'},           # Caminho para "if": i → f
            'q2': {'e': 'q9'},           # Caminho para  "let": l → e
            'q3': {'r': 'q10'},          # Caminho para "true": t → r
            'q4': {'a': 'q11'},          # Caminho para  "false": f → a
            'q9': {'t': 'q12'},          # ... → t (completa "let")
            'q10': {'u': 'q13'},         # ... → u (para "true")
            'q11': {'l': 'q14'},         # ... → l (para "false")
            'q13': {'e': 'q15'},         # ... → e (Completa "true")
            'q14': {'s': 'q16'},         # ... → s (para "false")
            'q16': {'e': 'q17'}          # ... → e (Completa "false")
    },
     'initial_state': 'q0',
     'final_states' :  ['q5', 'q6', 'q7', 'q8', 'q12', 'q15', 'q17']
}