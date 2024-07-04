# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP] Link to Previous Article
> 🡸 [ Printing in Python](/Python/Articles/2_how_to_print_in_python.md) 🖨️


## Data Types in Python 💊

Data types are classifications that specify which kind of value a variable can hold. Python has several built-in data types, each suited for different purposes. Understanding these data types is fundamental to working effectively with Python.

### Basic Data Types:

1. **`int` (Integer)**:
   - **Description**: Represents whole numbers, positive or negative, without decimals.
   - **Example**: `a = 10`, `b = -5`
   - **Edge Case**: Very large integers are supported without overflow, limited by memory (e.g., `a = 10**100`).

2. **`float` (Floating Point)**:
   - **Description**: Represents numbers with decimals.
   - **Example**: `a = 10.5`, `b = -2.3`
   - **Edge Case**: Precision issues can arise with very large or very small floating-point numbers (e.g., `0.1 + 0.2` results in `0.30000000000000004`).

3. **`str` (String)**:
   - **Description**: Represents a sequence of characters.
   - **Example**: `a = "hello"`, `b = 'world'`
   - **Edge Case**: Strings can include escape sequences like `\n` (newline) and `\t` (tab). Multiline strings are created with triple quotes (`""" ... """`).

4. **`bool` (Boolean)**:
   - **Description**: Represents two values: `True` or `False`.
   - **Example**: `a = True`, `b = False`
   - **Edge Case**: Any non-zero number or non-empty object is considered `True` when used in a boolean context.

### Compound Data Types:

1. **`list`**:
   - **Description**: Ordered, mutable collection of items.
   - **Example**: `a = [1, 2, 3]`, `b = ["apple", "banana", "cherry"]`
   - **Edge Case**: Lists can contain mixed data types and nested lists (e.g., `a = [1, "two", [3, 4]]`).

2. **`tuple`**:
   - **Description**: Ordered, immutable collection of items.
   - **Example**: `a = (1, 2, 3)`, `b = ("apple", "banana", "cherry")`
   - **Edge Case**: Tuples with one item require a comma (e.g., `a = (1,)`).

3. **`set`**:
   - **Description**: Unordered collection of unique items.
   - **Example**: `a = {1, 2, 3}`, `b = {"apple", "banana", "cherry"}`
   - **Edge Case**: Sets cannot contain mutable items like lists or other sets.

4. **`dict` (Dictionary)**:
   - **Description**: Unordered collection of key-value pairs.
   - **Example**: `a = {"name": "Alice", "age": 25}`, `b = {"fruit": "apple", "color": "red"}`
   - **Edge Case**: Keys must be immutable (e.g., strings, numbers), and each key must be unique.

### Specialized Data Types:

1. **`NoneType`**:
   - **Description**: Represents the absence of a value.
   - **Example**: `a = None`
   - **Edge Case**: Used to signify 'no value' or 'null', often as a default return value for functions.

2. **`complex`**:
   - **Description**: Represents complex numbers (a + bj).
   - **Example**: `a = 1 + 2j`, `b = 3 - 4j`
   - **Edge Case**: Useful in specific domains like electrical engineering and scientific computing.

### Summary

Understanding Python's data types and their characteristics is essential for effective programming. Here are the main types:

- **Basic Types** : `int`, `float`, `str`, `bool`
- **Compound Types** : `list`, `tuple`, `set`, `dict`
- **Specialized Types** : `NoneType`, `complex`

Each type has unique behaviors and edge cases, so experimenting with them will help solidify your understanding. 😊

> [!TIP] Link to Next Article
>  🡺 [Python is a Dynamically Typed Language](/Python/Articles/4_dynamic_typing.md) ⚡