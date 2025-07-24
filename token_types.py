# Add new token types for the parser
# These token types will be used in the parser to identify different constructs in the Alak language
# File: token_types.py
TOKENS = [
    ('NUMBER', r'\d+'),
    ('LET', r'let'),
    ('PRINT', r'print'),
    ('IF', r'\bif\b'),
    ('ELSE', r'\belse\b'),
    ('WHILE', r'\bwhile\b'),
    ('IDENT', r'[a-zA-Z_]\w*'),
    ('EQUAL', r'='),
    ('PLUS', r'\+'),
    ('GT', r'>'),
    ('LT', r'<'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('STRING', r"'[^']*'"),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]