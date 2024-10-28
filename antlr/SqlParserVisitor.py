# Generated from SqlParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete generic visitor for a parse tree produced by SqlParser.

class SqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlParser#query.
    def visitQuery(self, ctx:SqlParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#selectStmt.
    def visitSelectStmt(self, ctx:SqlParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#column.
    def visitColumn(self, ctx:SqlParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlParser#table.
    def visitTable(self, ctx:SqlParser.TableContext):
        return self.visitChildren(ctx)



del SqlParser