from translators.ast_translator import ASTTranslator

# Inicializando o tradutor AST
translator = ASTTranslator()

# Query Oracle SQL
query = "SELECT SYSDATE FROM DUAL;"

# Tradução para T-SQL
translated_query = translator.translate(query)
print(f"Oracle Query: {query}")
print(f"T-SQL Query: {translated_query}")
