import re
from token_types import TOKENS

tokens_re = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS))

class Tokenizer:
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        tokens = []
        for match in tokens_re.finditer(self.code):
            kind = match.lastgroup
            value = match.group()
            if kind in ('SKIP', 'NEWLINE'):
                continue
            tokens.append((kind, value))
        return tokens
