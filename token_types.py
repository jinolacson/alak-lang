# Add new token types for the parser
# These token types will be used in the parser to identify different constructs in the Alak language
# File: token_types.py
TOKENS = [
    ('NUMBER', r'\d+'),
    ('LAPAG', r'\blapag\b'),
    ('PRINT', r'\bshot\b'),
    ('IF', r'\bif\b'),
    ('ELSE', r'\belse\b'),
    ('JUMBO', r'\bjumbo\b'),
     ('FUN', r'\bfun\b'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('IDENT', r'[a-zA-Z_]\w*'),
    ('EQUAL', r'='),
    ('PLUS', r'\+'),
    ('GT', r'>'),
    ('GTE', r'>='),
    ('LT', r'<'),
    ('LTE', r'<='),
    ('EQ', r'=='),
    ('NEQ', r'!='),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('STRING', r'"[^"]*"'),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]
