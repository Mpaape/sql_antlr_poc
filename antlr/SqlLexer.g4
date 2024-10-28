lexer grammar SqlLexer;

SELECT: 'SELECT';
FROM: 'FROM';
SYSDATE: 'SYSDATE';
DUAL: 'DUAL';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
SEMICOLON: ';';
COMMA: ',';
WS: [ \t\r\n]+ -> skip;
