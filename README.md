# 🧪 Alak

**Alak** is a fun, Tagalog-inspired esolang designed for learning and laughs. It uses Filipino "inuman" terms as syntax.

---

## Project Structure
```bash
alak-lang/
├── alak/
│   ├── __init__.py
│   ├── cli.py           # Entry CLI file
│   └── interpreter.py   # Transformer logic
├── example.alak         # Example program
├── setup.py             # Setup config
└── requirements.txt     # Dependencies
```

---

## Getting Started

### 1. How to install

```bash
git clone https://github.com/your-username/alak.git
python3 -m venv env
source env/bin/activate
pip install -e .
```

### Run an Alak Program
```bash
alak run example.alak
```
Make sure you have Python 3.10 installed.

### Example
Here's what an example ```.alak``` file might look like:
```bash
alak x = 5;
alak y = 10;
tungga x;
kung (x < y) tagay
    tungga "x is less than y";
bitaw

ikot (x < 10) tagay
    tungga x;
    alak x = x + 1;
bitaw

inom greet tagay
    tungga "Hello from inom!";
bitaw

greet();

```

Output:
```bash
5.0
x is less than y
5.0
6.0
7.0
8.0
9.0
Hello from inom!
```

### License
MIT License. Feel free to use and modify.
