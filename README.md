# SQL Transpiler PoC

Este projeto é uma PoC para transpilar queries SQL entre Oracle SQL e T-SQL usando ANTLR4 e o padrão de visitante (Visitor).

## Como Executar

1. **Instalar Dependências**:
   ```
   pip install -r requirements.txt
   ```

2. **Gerar Lexer e Parser**:
   Execute o comando ANTLR para gerar os arquivos de Lexer e Parser:
   ```
   antlr4 -Dlanguage=Python3 antlr/SqlLexer.g4 antlr/SqlParser.g4
   ```

3. **Rodar a Tradução**:
   ```
   python main.py
   ```

4. **Rodar os Testes**:
   ```
   python -m unittest discover
   ```
