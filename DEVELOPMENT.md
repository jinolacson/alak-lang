## Getting Started

### Creating a Build and Uploading to PyPI

1. Install required tools and build the package:

```
# From root of alak-lang
pip install --upgrade build
python -m build

# Install locally
pip install dist/alak-0.1.0-py3-none-any.whl
```

2. Install the package locally (for testing):

```
pip install dist/alak-0.1.0-py3-none-any.whl
```
3. Upload to PyPI:

```
pip install twine
twine upload dist/*
```
4. Test the CLI command:

```
alak --version // alak version 0.1.0
```

### Developer Installation (Editable Mode)

Make sure you have Python 3.x installed.

```bash
git clone https://github.com/jinolacson/alak-lang.git
cd alak-lang
python3 -m venv env
source env/bin/activate
pip install -e .

```

Now you can run:

```
alak yourfile.alak
```
