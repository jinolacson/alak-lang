import sys
from tokenizer import Tokenizer
from parser import Parser
from interpreter import Interpreter
# Simple command-line compiler for Alak language

if len(sys.argv) < 2:
    print("Usage: python compiler.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Read code from the file
with open(filename, 'r') as f:
    code = f.read()

# Tokenize
tk = Tokenizer(code)
tokens = tk.tokenize()

# Output tokens
# for token in tokens:
#     print(token)

# Parse
parser = Parser(tokens)
try:
    ast = parser.parse()
    # print("Parsed AST:", ast)
    interpreter = Interpreter()
    interpreter.interpret(ast)
except SyntaxError as e:
    print(f"Syntax Error: {e}")
    sys.exit(1)