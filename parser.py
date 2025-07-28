class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        # print(f"Peeking at token: {self.tokens[self.pos] if self.pos < len(self.tokens) else 'EOF'}")
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
        # print(f"Parsing statement: {kind}")
        if kind == 'LAPAG': # 'lapag' for let statement
            return self.let_statement()
        elif kind == 'PRINT':
            return self.print_statement()
        elif kind == 'IF':
            return self.if_statement()
        elif kind == 'JUMBO':  # 'jumbo' for while loop
            return self.while_statement()
        elif kind == 'IDENT':
            return self.assignment_or_call()
        elif kind == 'FUN':
            return self.function_declaration()
        else:
            raise SyntaxError(f"Unknown statement: {kind}")
    
    def let_statement(self):
        self.match('LAPAG')
        name = self.match('IDENT')
        self.match('EQUAL')
        value = self.expression()
        self.match('SEMICOLON')
        return ('lapag', name, value)

    # Handles assignment or function call
    def assignment_or_call(self):
        name = self.match('IDENT')
        next_kind, _ = self.peek()

        if next_kind == 'EQUAL':
            self.match('EQUAL')
            expr = self.expression()
            self.match('SEMICOLON')
            return ('assign', name, expr)

        elif next_kind == 'LPAREN':
            self.match('LPAREN')
            self.match('RPAREN')
            self.match('SEMICOLON')
            return ('call', name)

        else:
            raise SyntaxError(f"Unexpected token after IDENT: {next_kind}")


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
        self.match('JUMBO')
        condition = self.expression()
        self.match('LBRACE')
        body = []
        while self.peek()[0] != 'RBRACE':
            body.append(self.statement())
        self.match('RBRACE')
        return ('jumbo', condition, body)

    def function_declaration(self):
        self.match('FUN')               # Consume 'fun'
        name = self.match('IDENT')      # Function name
        self.match('LBRACE')            # Start of block

        body = []
        while self.peek()[0] != 'RBRACE':
            body.append(self.statement())

        self.match('RBRACE')            # End of block
        return ('fun', name, body)

    # Parses an expression, which can be a number, string, variable, or a more complex expression
    # This is a simplified version and can be extended to handle more complex expressions
    def expression(self):
        left = self.additive()
        while self.peek()[0] in ('GT', 'LT', 'GTE', 'LTE', 'EQ', 'NEQ'):
            op = self.match(self.peek()[0])
            right = self.additive()
            if op == '>':
                left = ('gt', left, right)
            elif op == '<':
                left = ('lt', left, right)
            elif op == '>=':
                left = ('gte', left, right)
            elif op == '<=':
                left = ('lte', left, right)
            elif op == '==':
                left = ('eq', left, right)
            elif op == '!=':
                left = ('neq', left, right)
        return left
    
    # Handles addition
    def additive(self):
        left = self.term()
        while self.peek()[0] == 'PLUS':
            self.match('PLUS')
            right = self.term()
            left = ('add', left, right)
        return left

    # Parses a term or type of expression
    def term(self):
        kind, value = self.peek()
        if kind == 'NUMBER':
            self.match('NUMBER')
            return ('number', int(value))
        elif kind == 'STRING':
            self.match('STRING')
            return ('string', value.strip('"'))
        elif kind == 'IDENT':
            return ('var', self.match('IDENT'))
        elif kind == 'LPAREN':
            self.match('LPAREN')
            expr = self.expression()
            self.match('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token: {kind}")
