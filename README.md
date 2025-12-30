# sql-lisfy

A SQL parser that transforms SQL queries into structured S-expression representations.

## Overview

sql-lisfy parses SQL statements and converts them into Lisp-like S-expressions, providing a structured and programmatically accessible format. The parser includes a lexer for tokenization and a statement parser that supports SELECT and CREATE statements.

## Requirements

- Python 3.11 or higher

## Installation

```bash
pip install sql-lisfy
```

Or with Poetry:

```bash
poetry add sql-lisfy
```

## Usage

### Interactive REPL

Start the interactive SQL parser:

```bash
sql-lisfy
```

Then enter SQL statements at the prompt:

```
sql_lisfy> SELECT id, name FROM users
```

### Programmatic Usage

```python
from sql_lisfy import rep

# Parse a SQL statement
result = rep.rep("SELECT id, name FROM users")
print(result)
```

## Features

- Lexical analysis of SQL tokens including operators, strings, and identifiers
- Statement parsing for SELECT and CREATE TABLE queries
- Structured output using Pydantic models
- Interactive REPL for testing and experimentation

## License

Apache-2.0
