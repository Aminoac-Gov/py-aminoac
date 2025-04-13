# PyAminoac

A Python tool for translating Chinese to Aminoac.

## Features

- Supports both simplified and traditional Chinese characters
- Removes book title marks (《》) during translation
- Converts Chinese punctuation to English equivalents
- Intelligently handles non-paragraph-splitting punctuation (keeps commas, parentheses, etc. within sentences)
- Only splits sentences on major punctuation (.!?;:)
- Reverses Chinese words in pinyin format

## Installation

```bash
pip install pyaminoac
```

Or install from source:

```bash
git clone https://github.com/Aminoac-Gov/pyaminoac.git
cd pyaminoac
pip install -e .
```

## Usage

### Command Line Interface

Start the REST API server:
```bash
pyaminoac serve
```

Translate text:
```bash
pyaminoac translate "Input text here"
```

### As a Python Module

```python
from pyaminoac.translator import translate_text

result = translate_text("Input text here")
print(result)
```

## API Endpoints

- `GET /translate?text=<text>` - Translate the given text

## License

MIT