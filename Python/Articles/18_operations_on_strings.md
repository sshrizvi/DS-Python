# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Substrings in Python](/Python/Articles/17_substrings.md) 🧩

## Operations on Strings in Python 🔧

Strings in Python support a variety of operations, including arithmetic, relational, logical, looping, and membership operations. Understanding these operations can help in effectively manipulating and analyzing text data.

### 1. **Arithmetic Operations**

Arithmetic operations on strings include concatenation and repetition.

#### Concatenation (`+`)

Combines two strings into one.

**Syntax**:
```python
result = string1 + string2
```

**Example**:
```python
s1 = "Hello, "
s2 = "World!"
result = s1 + s2
print(result)  # Output: Hello, World!
```

#### Repetition (`*`)

Repeats the string a specified number of times.

**Syntax**:
```python
result = string * n
```

**Example**:
```python
s = "Hello! "
result = s * 3
print(result)  # Output: Hello! Hello! Hello! 
```

### 2. **Relational Operations**

Relational operations compare strings based on lexicographical order.

#### Equality (`==`)

Checks if two strings are equal.

**Syntax**:
```python
result = string1 == string2
```

**Example**:
```python
s1 = "Hello"
s2 = "Hello"
print(s1 == s2)  # Output: True
```

#### Inequality (`!=`)

Checks if two strings are not equal.

**Syntax**:
```python
result = string1 != string2
```

**Example**:
```python
s1 = "Hello"
s2 = "World"
print(s1 != s2)  # Output: True
```

#### Greater Than (`>`)

Checks if one string is lexicographically greater than another.

**Syntax**:
```python
result = string1 > string2
```

**Example**:
```python
s1 = "Hello"
s2 = "Goodbye"
print(s1 > s2)  # Output: False
```

#### Less Than (`<`)

Checks if one string is lexicographically less than another.

**Syntax**:
```python
result = string1 < string2
```

**Example**:
```python
s1 = "Hello"
s2 = "World"
print(s1 < s2)  # Output: True
```

#### Greater Than or Equal To (`>=`)

Checks if one string is greater than or equal to another.

**Syntax**:
```python
result = string1 >= string2
```

**Example**:
```python
s1 = "Hello"
s2 = "Hello"
print(s1 >= s2)  # Output: True
```

#### Less Than or Equal To (`<=`)

Checks if one string is less than or equal to another.

**Syntax**:
```python
result = string1 <= string2
```

**Example**:
```python
s1 = "Goodbye"
s2 = "World"
print(s1 <= s2)  # Output: True
```

### 3. **Logical Operations**

Logical operations on strings are not directly applicable as they are for booleans, but you can use boolean contexts.

#### Logical `and`

Both strings must be truthy (non-empty) for the result to be truthy.

**Syntax**:
```python
result = string1 and string2
```

**Example**:
```python
s1 = "Hello"
s2 = "World"
print(s1 and s2)  # Output: World (both are truthy)
```

#### Logical `or`

Returns the first truthy string or the last string if none are truthy.

**Syntax**:
```python
result = string1 or string2
```

**Example**:
```python
s1 = ""
s2 = "World"
print(s1 or s2)  # Output: World (s1 is falsy, so s2 is returned)
```

#### Logical `not`

Returns the negation of the string's truthiness (empty strings are falsy).

**Syntax**:
```python
result = not string
```

**Example**:
```python
s = ""
print(not s)  # Output: True (empty string is falsy)
```

### 4. **Loops with Strings**

Loops can iterate over characters in a string.

#### `for` Loop

Iterates over each character in the string.

**Syntax**:
```python
for char in string:
    # process char
```

**Example**:
```python
s = "Hello"
for char in s:
    print(char)
# Output: H e l l o
```

#### `while` Loop

Can be used with indexing to iterate over a string.

**Syntax**:
```python
index = 0
while index < len(string):
    # process string[index]
    index += 1
```

**Example**:
```python
s = "Hello"
index = 0
while index < len(s):
    print(s[index])
    index += 1
# Output: H e l l o
```

### 5. **Membership Operators**

Membership operators check if a substring exists within a string.

#### `in`

Checks if a substring is present in the string.

**Syntax**:
```python
result = substring in string
```

**Example**:
```python
s = "Hello, World!"
print("World" in s)  # Output: True
print("world" in s)  # Output: False (case-sensitive)
```

#### `not in`

Checks if a substring is not present in the string.

**Syntax**:
```python
result = substring not in string
```

**Example**:
```python
s = "Hello, World!"
print("Python" not in s)  # Output: True
print("World" not in s)  # Output: False
```

### Flashing Tricks for Learners 🚀

1. **String Multiplication**:
   - Use string multiplication to quickly generate repeated patterns, such as `'-' * 20` to create a line of dashes.

2. **String Methods**:
   - Combine string methods for complex transformations, e.g., `s.strip().upper().replace("OLD", "NEW")`.

3. **F-Strings**:
   - Use f-strings for more readable and efficient string formatting: `f"Value: {value}"`.

4. **String Interpolation**:
   - Practice using different string formatting methods (f-strings, `str.format()`, `%` formatting) to choose the best for your needs.

5. **Handling Empty Strings**:
   - Remember that empty strings are falsy, so they can be used effectively in conditional statements.

6. **Slice Tricks**:
   - Use slicing to reverse a string: `s[::-1]`.

7. **Checking Substrings**:
   - Combine `in` with string methods for more advanced checks, like case-insensitive searches using `s.lower()`.

Understanding these operations and how they interact with strings will significantly enhance your ability to work with text data in Python. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [String Methods in Python](/Python/Articles/19_string_methods.md) 🧰