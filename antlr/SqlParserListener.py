# Generated from SqlParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#query.
    def enterQuery(self, ctx:SqlParser.QueryContext):
        pass

    # Exit a parse tree produced by SqlParser#query.
    def exitQuery(self, ctx:SqlParser.QueryContext):
        pass


    # Enter a parse tree produced by SqlParser#selectStmt.
    def enterSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by SqlParser#selectStmt.
    def exitSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by SqlParser#column.
    def enterColumn(self, ctx:SqlParser.ColumnContext):
        pass

    # Exit a parse tree produced by SqlParser#column.
    def exitColumn(self, ctx:SqlParser.ColumnContext):
        pass


    # Enter a parse tree produced by SqlParser#table.
    def enterTable(self, ctx:SqlParser.TableContext):
        pass

    # Exit a parse tree produced by SqlParser#table.
    def exitTable(self, ctx:SqlParser.TableContext):
        pass



del SqlParser