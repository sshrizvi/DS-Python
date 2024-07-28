# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Operations on Strings in Python](/Python/Articles/18_operations_on_strings.md) 🔧

## String Methods in Python 🧰

Python provides a rich set of string methods for various operations. Here's a comprehensive table of string methods with their function signatures, descriptions, and examples.

| Method                     | Function Signature                      | Description                                                                                       | Example                                                |
|:----------------------------:|:-----------------------------------------:|:---------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|
| `capitalize()`             | `str.capitalize()`                      | Converts the first character to uppercase.                                                        | `"hello".capitalize()` → `'Hello'`                      |
| `casefold()`               | `str.casefold()`                        | Converts the string to lowercase, more aggressive than `lower()`.                                  | `"HELLO".casefold()` → `'hello'`                        |
| `center(width[, fillchar])`| `str.center(width, fillchar=' ')`       | Centers the string, padding with `fillchar`.                                                      | `"hello".center(10, '*')` → `'**hello***'`              |
| `count(sub[, start[, end]])` | `str.count(sub, start=0, end=len(str))` | Counts occurrences of `sub` in the string.                                                        | `"hello".count('l')` → `2`                              |
| `encode(encoding='utf-8', errors='strict')` | `str.encode(encoding, errors)` | Encodes the string using the specified `encoding`.                                                | `"hello".encode('utf-8')` → `b'hello'`                  |
| `endswith(suffix[, start[, end]])` | `str.endswith(suffix, start=0, end=len(str))` | Checks if the string ends with `suffix`.                                                          | `"hello".endswith('lo')` → `True`                       |
| `expandtabs(tabsize=8)`     | `str.expandtabs(tabsize=8)`            | Replaces tabs with spaces.                                                                        | `"Hello\tWorld".expandtabs(4)` → `'Hello   World'`      |
| `find(sub[, start[, end]])` | `str.find(sub, start=0, end=len(str))` | Finds the first occurrence of `sub`. Returns `-1` if not found.                                   | `"hello".find('l')` → `2`                               |
| `format(*args, **kwargs)`   | `str.format(*args, **kwargs)`          | Formats the string using placeholders.                                                            | `"Hello, {}".format("World")` → `'Hello, World'`        |
| `format_map(mapping)`       | `str.format_map(mapping)`              | Formats the string using a dictionary mapping.                                                    | `"{name}".format_map({'name': 'Alice'})` → `'Alice'`    |
| `index(sub[, start[, end]])` | `str.index(sub, start=0, end=len(str))` | Finds the first occurrence of `sub`. Raises `ValueError` if not found.                            | `"hello".index('l')` → `2`                              |
| `isalnum()`                 | `str.isalnum()`                        | Checks if all characters are alphanumeric.                                                        | `"hello123".isalnum()` → `True`                         |
| `isalpha()`                 | `str.isalpha()`                        | Checks if all characters are alphabetic.                                                          | `"hello".isalpha()` → `True`                            |
| `isascii()`                 | `str.isascii()`                        | Checks if all characters are ASCII.                                                               | `"hello".isascii()` → `True`                            |
| `isdecimal()`               | `str.isdecimal()`                      | Checks if all characters are decimal characters.                                                  | `"123".isdecimal()` → `True`                            |
| `isdigit()`                 | `str.isdigit()`                        | Checks if all characters are digits.                                                              | `"123".isdigit()` → `True`                              |
| `isidentifier()`            | `str.isidentifier()`                   | Checks if the string is a valid identifier.                                                       | `"hello".isidentifier()` → `True`                       |
| `islower()`                 | `str.islower()`                        | Checks if all characters are lowercase.                                                           | `"hello".islower()` → `True`                            |
| `isnumeric()`               | `str.isnumeric()`                      | Checks if all characters are numeric.                                                             | `"123".isnumeric()` → `True`                            |
| `isprintable()`             | `str.isprintable()`                    | Checks if all characters are printable.                                                           | `"hello".isprintable()` → `True`                        |
| `isspace()`                 | `str.isspace()`                        | Checks if all characters are whitespace.                                                          | `" \t\n".isspace()` → `True`                            |
| `istitle()`                 | `str.istitle()`                        | Checks if the string is titlecased.                                                               | `"Hello World".istitle()` → `True`                      |
| `isupper()`                 | `str.isupper()`                        | Checks if all characters are uppercase.                                                           | `"HELLO".isupper()` → `True`                            |
| `join(iterable)`            | `str.join(iterable)`                   | Joins elements of an iterable with the string as a separator.                                     | `", ".join(["a", "b", "c"])` → `'a, b, c'`              |
| `ljust(width[, fillchar])`  | `str.ljust(width, fillchar=' ')`       | Left-justifies the string, padding with `fillchar`.                                               | `"hello".ljust(10, '*')` → `'hello*****'`               |
| `lower()`                   | `str.lower()`                          | Converts the string to lowercase.                                                                 | `"HELLO".lower()` → `'hello'`                           |
| `lstrip([chars])`           | `str.lstrip(chars)`                    | Removes leading characters specified in `chars`.                                                  | `"  hello".lstrip()` → `'hello'`                        |
| `maketrans(x[, y[, z]])`    | `str.maketrans(x, y, z)`               | Returns a translation table to be used in `translate()`.                                          | `"hello".maketrans("h", "H")` → `{104: 72}`             |
| `partition(sep)`            | `str.partition(sep)`                   | Splits the string at the first occurrence of `sep`.                                               | `"hello world".partition(" ")` → `('hello', ' ', 'world')` |
| `replace(old, new[, count])`| `str.replace(old, new, count=-1)`      | Replaces occurrences of `old` with `new`.                                                         | `"hello world".replace("world", "Python")` → `'hello Python'` |
| `rfind(sub[, start[, end]])`| `str.rfind(sub, start=0, end=len(str))`| Finds the last occurrence of `sub`. Returns `-1` if not found.                                    | `"hello".rfind('l')` → `3`                              |
| `rindex(sub[, start[, end]])`| `str.rindex(sub, start=0, end=len(str))` | Finds the last occurrence of `sub`. Raises `ValueError` if not found.                             | `"hello".rindex('l')` → `3`                             |
| `rjust(width[, fillchar])`  | `str.rjust(width, fillchar=' ')`       | Right-justifies the string, padding with `fillchar`.                                              | `"hello".rjust(10, '*')` → `'*****hello'`               |
| `rpartition(sep)`           | `str.rpartition(sep)`                  | Splits the string at the last occurrence of `sep`.                                                | `"hello world".rpartition(" ")` → `('hello', ' ', 'world')` |
| `rsplit(sep=None, maxsplit=-1)`| `str.rsplit(sep, maxsplit)`         | Splits the string from the right at each occurrence of `sep`.                                     | `"a,b,c".rsplit(",", 1)` → `['a,b', 'c']`               |
| `rstrip([chars])`           | `str.rstrip(chars)`                    | Removes trailing characters specified in `chars`.                                                 | `"hello  ".rstrip()` → `'hello'`                        |
| `split(sep=None, maxsplit=-1)`| `str.split(sep, maxsplit)`          | Splits the string at each occurrence of `sep`.                                                    | `"a,b,c".split(",")` → `['a', 'b', 'c']`                |
| `splitlines([keepends])`    | `str.splitlines(keepends=False)`       | Splits the string at line breaks.                                                                 | `"a\nb\nc".splitlines()` → `['a', 'b', 'c']`            |
| `startswith(prefix[, start[, end]])`| `str.startswith(prefix, start=0, end=len(str))` | Checks if the string starts with `prefix`.                                                       | `"hello".startswith('he')` → `True`                     |
| `strip([chars])`            | `str.strip(chars)`                     | Removes leading and trailing characters specified in `chars`.                                     | `"  hello  ".strip()` → `'hello'`                       |
| `swapcase()`                | `str.swapcase()`                       | Swaps the case of all characters in the string.                                                   | `"Hello".swapcase()` → `'hELLO'`                        |
| `title()`                   | `str.title()`                          | Converts the string to title case.                                                                | `"hello world".title()` → `'Hello World'`               |
| `translate(table)`         

 | `str.translate(table)`                 | Translates the string using the translation table returned by `maketrans()`.                      | `"hello".translate({"h": "H"})` → `'Hello'`             |
| `upper()`                   | `str.upper()`                          | Converts the string to uppercase.                                                                 | `"hello".upper()` → `'HELLO'`                           |
| `zfill(width)`              | `str.zfill(width)`                     | Pads the string with zeros on the left until it reaches the specified width.                      | `"42".zfill(5)` → `'00042'`                             |

### Examples 📝

#### 1. `capitalize()`
```python
s = "hello"
print(s.capitalize())  # Output: 'Hello'
```

#### 2. `count()`
```python
s = "hello"
print(s.count('l'))  # Output: 2
```

#### 3. `find()`
```python
s = "hello"
print(s.find('l'))  # Output: 2
```

#### 4. `join()`
```python
items = ["apple", "banana", "cherry"]
print(", ".join(items))  # Output: 'apple, banana, cherry'
```

#### 5. `replace()`
```python
s = "hello world"
print(s.replace("world", "Python"))  # Output: 'hello Python'
```

#### 6. `split()`
```python
s = "a,b,c"
print(s.split(","))  # Output: ['a', 'b', 'c']
```

### Additional Information 💡

1. **Immutability**: Strings in Python are immutable, meaning that any operation on a string will return a new string rather than modifying the original one.
2. **Unicode Support**: Python strings support Unicode, which means they can handle a wide range of characters from different languages.
3. **Efficiency**: String methods are optimized for performance, making them efficient for text processing tasks.

These methods provide a powerful toolkit for manipulating and analyzing strings in Python. 😊

> [!WARNING]
> If you have learned about Strings, try to solve the some problems.  
> Here is the link to the problems [Problems on Strings](/Notebooks/1_problems_on_strings.ipynb)

> [!IMPORTANT]  
> If you have studied Article 16-19, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 3](/Python/Tasks/task_3.ipynb)

> [!TIP]  
> Link to Next Article  
> 🡺 [Complexity Analysis in Programming](/Python/Articles/20_complexity_analysis.md) 📊