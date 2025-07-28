# 🧪 Alak: A Toy Programming Language built with Python

**Alak** is a simple interpreted programming language built in Python for educational and experimental purposes. It features a basic compiler, tokenizer, parser, and interpreter pipeline. Alak was designed to help you understand how programming languages work under the hood.

---

## Project Structure
```bash
alak/
├── compiler.py # Entry point for compiling & running Alak files
├── interpreter.py # Evaluates parsed syntax tree
├── parser.py # Converts tokens into an AST
├── token_types.py # Definitions of token types
├── tokenizer.py # Lexical analyzer (lexer)
└── example.alak # Sample Alak program
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alak.git
cd alak
```

### Run an Alak Program
```bash
python3.10 compiler.py example.alak
```
Make sure you have Python 3.10 installed.

### Example
Here's what an example ```.alak``` file might look like:
```bash
lapag tropa = "Leetz";
lapag ambag_one = 5;
lapag ambag_two = 150;
lapag total_ambag = 0;

total_ambag = ambag_one + ambag_two;

if total_ambag > 100 {
  shot "letsgo";
} else {
  shot "Ambag muna";
}


lapag bote = 0;
jumbo bote < 5 {
  shot "Bili na ng {bote} gin";
  bote = bote + 1;
}

fun oras_na {
  shot "Shot na {tropa} may ambag {total_ambag} pesos na!";
}

oras_na();

```

Output:
```bash
letsgo
Bili na ng 0 gin
Bili na ng 1 gin
Bili na ng 2 gin
Bili na ng 3 gin
Bili na ng 4 gin
Shot na Leetz may ambag 155 pesos na!
```

### How It Works
* Tokenizer (tokenizer.py): Breaks source code into tokens.
* Parser (parser.py): Converts tokens into an abstract syntax tree (AST).
* Interpreter (interpreter.py): Walks through the AST and executes commands.
* Compiler (compiler.py): Orchestrates the entire compilation and execution process.

### Current Features
* Variable declaration using lapag
* Expression assignment and math operations
* shot for printing with string interpolation
* Conditional logic: if / else
* Loops: while
* Functions: fun with zero-arg support and calling
* String interpolation with {var} in shot


### Future Improvements
* Function Parameters – Allow passing arguments into functions
  ```Example: fun greet(name) { shot "Hi {name}"; }```
*  Return Statement (balik) – Enable returning values from functions
```Example: balik a + b;```
* Function Scope – Support local variables inside functions using scoped env
* Operator Precedence & Grouping – Handle parentheses in math
```Example: lapag result = (5 + 3) * 2;```
* Arrays (Lists) – Allow defining and accessing list items
```Example: lapag items = ["a", "b"]; shot items[0];```
* Built-in Functions – Add helpers like length(), type(), input()
* For Loop Syntax – Add a for-style loop (sugar for while)
* Logical Operators – Support &&, ||, !, and ==, != in conditions
* Error Reporting with Line Numbers – Improve debugging and tracing
* REPL (Interactive Mode) – Let users test code line-by-line
* Standard Library – Include reusable helpers and utilities

### License
MIT License. Feel free to use and modify.
