parser grammar SqlParser;

options { tokenVocab=SqlLexer; } // Use esta linha para especificar que o vocabulário de tokens vem de SqlLexer

query: selectStmt SEMICOLON;

selectStmt: SELECT column FROM table;

column: SYSDATE | IDENTIFIER;

table: DUAL | IDENTIFIER;
