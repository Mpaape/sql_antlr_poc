from antlr4 import *
from antlr.SqlLexer import SqlLexer
from antlr.SqlParser import SqlParser
from antlr.SqlParserVisitor import SqlParserVisitor
from antlr4.tree.Trees import Trees   

class SQLTranslateVisitor(SqlParserVisitor):
    def __init__(self):
        self.query = ""

    def visitQuery(self, ctx):
        translated_select = self.visit(ctx.selectStmt())
        return f"{translated_select};"  

    def visitSelectStmt(self, ctx):
        self.query = "SELECT "
        self.visit(ctx.column())
        self.query += " FROM "
        self.visit(ctx.table())
        print(f"Finalizando SELECT statement: {self.query}")
        return self.query

    def visitColumn(self, ctx):
        if ctx.getText().upper() == "SYSDATE":
            self.query += "GETDATE()"
        else:
            self.query += ctx.getText()
        print(f"Após visitar coluna: {self.query}")

    def visitTable(self, ctx):
        self.query += ctx.getText()
        print(f"Após visitar tabela: {self.query}")

     

    def defaultResult(self):
        return self.query

class ASTTranslator:
    def translate(self, query):
        input_stream = InputStream(query)
        lexer = SqlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SqlParser(stream)
        tree = parser.query()  
        
        
        print("Árvore Sintática: ", Trees.toStringTree(tree, None, parser))
        
        visitor = SQLTranslateVisitor()
        translated_query = visitor.visit(tree)
        
        
        print(f"Query traduzida final no ASTTranslator: {translated_query}")
        
        return translated_query