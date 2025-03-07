# Generated from SqlLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,45,
        8,4,10,4,12,4,48,9,4,1,5,1,5,1,6,1,6,1,7,4,7,55,8,7,11,7,12,7,56,
        1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,3,3,0,65,90,
        95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,61,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,24,1,0,0,0,5,29,
        1,0,0,0,7,37,1,0,0,0,9,42,1,0,0,0,11,49,1,0,0,0,13,51,1,0,0,0,15,
        54,1,0,0,0,17,18,5,83,0,0,18,19,5,69,0,0,19,20,5,76,0,0,20,21,5,
        69,0,0,21,22,5,67,0,0,22,23,5,84,0,0,23,2,1,0,0,0,24,25,5,70,0,0,
        25,26,5,82,0,0,26,27,5,79,0,0,27,28,5,77,0,0,28,4,1,0,0,0,29,30,
        5,83,0,0,30,31,5,89,0,0,31,32,5,83,0,0,32,33,5,68,0,0,33,34,5,65,
        0,0,34,35,5,84,0,0,35,36,5,69,0,0,36,6,1,0,0,0,37,38,5,68,0,0,38,
        39,5,85,0,0,39,40,5,65,0,0,40,41,5,76,0,0,41,8,1,0,0,0,42,46,7,0,
        0,0,43,45,7,1,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,
        1,0,0,0,47,10,1,0,0,0,48,46,1,0,0,0,49,50,5,59,0,0,50,12,1,0,0,0,
        51,52,5,44,0,0,52,14,1,0,0,0,53,55,7,2,0,0,54,53,1,0,0,0,55,56,1,
        0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,6,7,0,0,59,
        16,1,0,0,0,3,0,46,56,1,6,0,0
    ]

class SqlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SELECT = 1
    FROM = 2
    SYSDATE = 3
    DUAL = 4
    IDENTIFIER = 5
    SEMICOLON = 6
    COMMA = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'SELECT'", "'FROM'", "'SYSDATE'", "'DUAL'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "SELECT", "FROM", "SYSDATE", "DUAL", "IDENTIFIER", "SEMICOLON", 
            "COMMA", "WS" ]

    ruleNames = [ "SELECT", "FROM", "SYSDATE", "DUAL", "IDENTIFIER", "SEMICOLON", 
                  "COMMA", "WS" ]

    grammarFileName = "SqlLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


