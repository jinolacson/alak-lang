class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def match(self, expected_type):
        kind, value = self.peek()
        if kind == expected_type:
            self.pos += 1
            return value
        raise SyntaxError(f"Expected {expected_type}, got {kind}")

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            stmt = self.statement()
            statements.append(stmt)
        return statements

    def statement(self):
        kind, _ = self.peek()
        if kind == 'LET':
            return self.let_statement()
        elif kind == 'PRINT':
            return self.print_statement()
        elif kind == 'IF':
            return self.if_statement()
        elif kind == 'WHILE':
            return self.while_statement()
        else:
            raise SyntaxError(f"Unknown statement: {kind}")

    def let_statement(self):
        self.match('LET')
        name = self.match('IDENT')
        self.match('EQUAL')
        value = self.expression()
        self.match('SEMICOLON')
        return ('let', name, value)

    def print_statement(self):
        self.match('PRINT')
        value = self.expression()
        self.match('SEMICOLON')
        return ('print', value)

    def block(self):
        self.match('LBRACE')
        statements = []
        while self.peek()[0] != 'RBRACE':
            statements.append(self.statement())
        self.match('RBRACE')
        return statements

    def if_statement(self):
        self.match('IF')
        condition = self.expression()
        then_branch = self.block()
        else_branch = None
        if self.peek()[0] == 'ELSE':
            self.match('ELSE')
            else_branch = self.block()
        return ('if', condition, then_branch, else_branch)

    def while_statement(self):
        self.match('WHILE')
        condition = self.expression()
        body = self.block()
        return ('while', condition, body)

    def expression(self):
        left = self.additive()
        kind, _ = self.peek()
        if kind in ('GT', 'LT', 'EQ', 'NEQ'):
            op = self.match(kind)
            right = self.additive()
            return (op.lower(), left, right)  # e.g., ('gt', left, right)
        return left

    def additive(self):
        left = self.term()
        while self.peek()[0] == 'PLUS':
            self.match('PLUS')
            right = self.term()
            left = ('add', left, right)
        return left

    def term(self):
        kind, value = self.peek()
        if kind == 'NUMBER':
            self.match('NUMBER')
            return ('number', int(value))
        elif kind == 'IDENT':
            return ('var', self.match('IDENT'))
        elif kind == 'LPAREN':
            self.match('LPAREN')
            expr = self.expression()
            self.match('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token: {kind}")
