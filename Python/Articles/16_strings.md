# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Loop Control Statements in Python](/Python/Articles/15_loop_control_statements.md) 🛑

## Strings in Python 📜

In Python, strings are sequences of characters enclosed in quotes. Strings are immutable, meaning they cannot be changed after creation. Python provides various ways to represent and manipulate strings.

### Types of String Representation

1. **Single Quotes**:
   - Strings can be enclosed in single quotes (`'`).
   ```python
   single_quote_string = 'Hello, World!'
   ```

2. **Double Quotes**:
   - Strings can also be enclosed in double quotes (`"`).
   ```python
   double_quote_string = "Hello, World!"
   ```

3. **Triple Quotes**:
   - For multi-line strings or strings with both single and double quotes, use triple quotes (`'''` or `"""`).
   ```python
   triple_quote_string = '''This is a 
   multi-line string. It can span 
   multiple lines.'''
   
   triple_quote_string = """This is another example
   of a multi-line string using double triple quotes."""
   ```

4. **Raw Strings**:
   - Raw strings ignore escape characters and are prefixed with an `r`.
   ```python
   raw_string = r'C:\Users\Name\Documents'
   ```

5. **Unicode Strings**:
   - In Python 3, all strings are Unicode by default, meaning they can represent characters from various languages and symbols.
   ```python
   unicode_string = "こんにちは世界"  # Japanese for "Hello, World"
   ```

### Indexing in Strings

Python strings support indexing to access individual characters. Indexing can be both positive and negative.

#### Positive Indexing

Positive indexing starts from `0` and increases as you move to the right.

**Syntax**:
```python
string[index]
```

**Example**:
```python
s = "Hello, World!"
print(s[0])  # Output: H
print(s[7])  # Output: W
```

#### Negative Indexing

Negative indexing starts from `-1` and decreases as you move to the left.

**Syntax**:
```python
string[-index]
```

**Example**:
```python
s = "Hello, World!"
print(s[-1])  # Output: !
print(s[-7])  # Output: W
```

> [!TIP]  
> Link to Next Article  
> 🡺 [Substrings in Python](/Python/Articles/17_substrings.md) 🧩