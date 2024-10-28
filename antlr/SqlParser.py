# Generated from SqlParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,21,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,2,2,0,3,3,5,5,1,0,4,
        5,16,0,8,1,0,0,0,2,11,1,0,0,0,4,16,1,0,0,0,6,18,1,0,0,0,8,9,3,2,
        1,0,9,10,5,6,0,0,10,1,1,0,0,0,11,12,5,1,0,0,12,13,3,4,2,0,13,14,
        5,2,0,0,14,15,3,6,3,0,15,3,1,0,0,0,16,17,7,0,0,0,17,5,1,0,0,0,18,
        19,7,1,0,0,19,7,1,0,0,0,0
    ]

class SqlParser ( Parser ):

    grammarFileName = "SqlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'SYSDATE'", "'DUAL'", 
                     "<INVALID>", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "SYSDATE", "DUAL", 
                      "IDENTIFIER", "SEMICOLON", "COMMA", "WS" ]

    RULE_query = 0
    RULE_selectStmt = 1
    RULE_column = 2
    RULE_table = 3

    ruleNames =  [ "query", "selectStmt", "column", "table" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    SYSDATE=3
    DUAL=4
    IDENTIFIER=5
    SEMICOLON=6
    COMMA=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStmt(self):
            return self.getTypedRuleContext(SqlParser.SelectStmtContext,0)


        def SEMICOLON(self):
            return self.getToken(SqlParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = SqlParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.selectStmt()
            self.state = 9
            self.match(SqlParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SqlParser.SELECT, 0)

        def column(self):
            return self.getTypedRuleContext(SqlParser.ColumnContext,0)


        def FROM(self):
            return self.getToken(SqlParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(SqlParser.TableContext,0)


        def getRuleIndex(self):
            return SqlParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = SqlParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_selectStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(SqlParser.SELECT)
            self.state = 12
            self.column()
            self.state = 13
            self.match(SqlParser.FROM)
            self.state = 14
            self.table()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSDATE(self):
            return self.getToken(SqlParser.SYSDATE, 0)

        def IDENTIFIER(self):
            return self.getToken(SqlParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = SqlParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==3 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DUAL(self):
            return self.getToken(SqlParser.DUAL, 0)

        def IDENTIFIER(self):
            return self.getToken(SqlParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SqlParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable" ):
                return visitor.visitTable(self)
            else:
                return visitor.visitChildren(self)




    def table(self):

        localctx = SqlParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





