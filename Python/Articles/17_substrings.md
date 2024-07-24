# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Strings in Python](/Python/Articles/16_strings.md)📜

## Substrings in Python 🧩

A **substring** is a contiguous sequence of characters within a string. Extracting substrings is a common operation in text processing. In Python, substrings can be extracted using **slicing**.

### Extracting Substrings

#### 1. **Basic Slicing**

Slicing allows you to extract a substring from a string using the following syntax:

**Syntax**:
```python
substring = string[start:end]
```

- `start`: The starting index of the substring (inclusive).
- `end`: The ending index of the substring (exclusive).

**Example**:
```python
s = "Hello, World!"
substring = s[0:5]  # Extracts from index 0 to 4
print(substring)    # Output: Hello
```

#### 2. **Omitting Indices**

If `start` or `end` is omitted, Python uses default values.

- Omitting `start` uses the beginning of the string.
- Omitting `end` uses the end of the string.

**Examples**:
```python
s = "Hello, World!"
print(s[:5])    # Output: Hello (from start to index 4)
print(s[7:])    # Output: World! (from index 7 to end)
```

#### 3. **Negative Indexing**

Negative indices count from the end of the string.

**Examples**:
```python
s = "Hello, World!"
print(s[-6:-1])  # Output: World (from index -6 to -2)
print(s[-6:])    # Output: World! (from index -6 to end)
```

#### 4. **Step Parameter**

The slice notation can include a `step` parameter to skip characters.

**Syntax**:
```python
substring = string[start:end:step]
```

**Example**:
```python
s = "Hello, World!"
print(s[::2])    # Output: Hlo ol! (every 2nd character)
print(s[1:10:3]) # Output: e, W (characters from index 1 to 9, every 3rd character)
```

### Important Points About Substrings 📘

1. **Immutable Strings**:
   - Strings in Python are immutable, so slicing a string does not modify the original string but returns a new substring.

2. **Index Out of Range**:
   - If `start` or `end` are out of the string’s range, Python handles it gracefully. For instance, `s[10:20]` on a string of length 15 will return an empty string.

3. **Efficiency**:
   - String slicing is efficient and typically implemented in C, making it faster than manual iteration for substring extraction.

4. **Negative Steps**:
   - A negative `step` parameter reverses the order of characters in the substring.
   ```python
   s = "Hello, World!"
   print(s[12:6:-1])  # Output:  W ,o (reverses from index 12 to 7)
   ```

5. **Use Cases**:
   - Extracting parts of text for processing (e.g., date extraction, text analysis).
   - Manipulating or formatting strings (e.g., extracting file extensions).

6. **Edge Cases**:
   - Slicing with `start > end` results in an empty string.
   - Slicing with `step` of `0` is invalid and will raise an error.

### Examples

#### Example 1: Basic Slicing
```python
s = "Python Programming"
substring = s[7:18]  # Extracts "Programming"
print(substring)
```

#### Example 2: Negative Indexing
```python
s = "Data Science"
substring = s[-7:-1]  # Extracts "Science"
print(substring)
```

#### Example 3: Slicing with Step
```python
s = "abcdefghijkl"
substring = s[1:10:2]  # Extracts "bdfhj"
print(substring)
```

Understanding how to extract and manipulate substrings is crucial for tasks such as text parsing, data cleaning, and user input validation. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Operations on Strings in Python](/Python/Articles/18_operations_on_strings.md) 🔧