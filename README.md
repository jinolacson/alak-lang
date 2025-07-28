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
Here's what an example .alak file might look like:
```bash
lapag tropa = "Leetz";
lapag ambag_one = 5;
lapag ambag_two = 10;
lapag total_ambag = 0;

total_ambag = ambag_one + ambag_two;
shot tropa;
shot total_ambag;

if total_ambag > 15 {
  shot "letsgo";
} else {
  shot "Ambag muna";
}


lapag i = 0;
jumbo i < 5 {
  shot i;
  i = i + 1;
}
```

Output:
```bash
Leetz
15
Ambag muna
0
1
2
3
4
```

### How It Works
* Tokenizer (tokenizer.py): Breaks source code into tokens.
* Parser (parser.py): Converts tokens into an abstract syntax tree (AST).
* Interpreter (interpreter.py): Walks through the AST and executes commands.
* Compiler (compiler.py): Orchestrates the entire compilation and execution process.

### Future Improvements
Add support for more complex expressions
Add function definitions
Improve error handling

📜 License
MIT License. Feel free to use and modify.
