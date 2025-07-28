class Interpreter:
    def __init__(self):
        self.env = {}

    def interpret(self, ast):
        for stmt in ast:
            self.execute(stmt)

    def execute(self, stmt):
        if stmt[0] == 'lapag':  # let statement
            _, name, expr = stmt
            self.env[name] = self.evaluate(expr)

        elif stmt[0] == 'assign':
            _, name, expr = stmt
            if name not in self.env:
                raise RuntimeError(f"Undefined variable '{name}'")
            self.env[name] = self.evaluate(expr)


        elif stmt[0] == 'print':
            _, expr = stmt
            value = self.evaluate(expr)

            # If value is a string, interpolate variables inside `{}` 
            #  Example  shot "Shot na {tropa}";
            if isinstance(value, str):
                import re
                def replacer(match):
                    var_name = match.group(1)
                    return str(self.env.get(var_name, f'{{{var_name}}}'))
                value = re.sub(r'\{(\w+)\}', replacer, value)
            print(value)


        elif stmt[0] == 'if':
            _, cond, then_branch, else_branch = stmt
            if self.evaluate(cond):
                for s in then_branch:
                    self.execute(s)
            elif else_branch:
                for s in else_branch:
                    self.execute(s)
        
        elif stmt[0] == 'jumbo': # while loop
            _, cond, body = stmt
            while self.evaluate(cond):
                for s in body:
                    self.execute(s)

        elif stmt[0] == 'fun': # function declaration
            _, name, body = stmt
            self.env[name] = ('function', body)

        elif stmt[0] == 'call':
            _, name = stmt
            if name not in self.env or self.env[name][0] != 'function':
                raise RuntimeError(f"Function '{name}' not defined")
            _, body = self.env[name]
            for inner_stmt in body:
                self.execute(inner_stmt)

    def evaluate(self, expr):
        kind = expr[0]
        if kind == 'number':
            return expr[1]
        elif kind == 'string':
            return expr[1]
        elif kind == 'var':
            return self.env.get(expr[1], None)
        elif kind == 'add':
            return self.evaluate(expr[1]) + self.evaluate(expr[2])
        elif kind == 'gt':
            return self.evaluate(expr[1]) > self.evaluate(expr[2])
        elif kind == 'lt':
            return self.evaluate(expr[1]) < self.evaluate(expr[2])
        elif kind == 'gte':
            return self.evaluate(expr[1]) >= self.evaluate(expr[2])
        elif kind == 'lte':
            return self.evaluate(expr[1]) <= self.evaluate(expr[2])
        elif kind == 'eq':
            return self.evaluate(expr[1]) == self.evaluate(expr[2])
        elif kind == 'neq':
            return self.evaluate(expr[1]) != self.evaluate(expr[2])
        elif kind == 'gt':
            return self.evaluate(expr[1]) > self.evaluate(expr[2])
        elif kind == 'lt':
            return self.evaluate(expr[1]) < self.evaluate(expr[2])
        elif kind == 'gte':
            return self.evaluate(expr[1]) >= self.evaluate(expr[2])
        elif kind == 'lte':
            return self.evaluate(expr[1]) <= self.evaluate(expr[2])
        elif kind == 'eq':
            return self.evaluate(expr[1]) == self.evaluate(expr[2])
        elif kind == 'neq':
            return self.evaluate(expr[1]) != self.evaluate(expr[2])


