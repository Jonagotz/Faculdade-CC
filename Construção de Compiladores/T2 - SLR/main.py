
from afd import afd
from lexical_analyzer import LexicalAnalyzer
from sintatical_analyzer import SintaticalAnalyzer


lexical_analyzer = LexicalAnalyzer(afd)
symbol_table = lexical_analyzer.transitions("inputs/input.in")
#lexical_analyzer.print_symbol_table()   
# lexical_analyzer.print_afd()
sintatical_analyzer = SintaticalAnalyzer('parsing_table.csv')
