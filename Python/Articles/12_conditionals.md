# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Operators in Python](/Python/Articles/11_operators.md) 🔧

## Conditional Statements in Python 🛤️

Conditional statements are used to execute a block of code based on certain conditions. They allow your program to make decisions and perform different actions depending on the outcome of those decisions.

### Types of Conditional Statements

1. **`if` statement**
2. **`if-else` statement**
3. **`if-elif-else` ladder**
4. **Nested `if` statements**

#### 1. `if` Statement

The `if` statement evaluates a condition and executes the block of code inside it if the condition is `True`.

**Syntax**:
```python
if condition:
    # block of code to execute if condition is True
```

**Example**:
```python
num = 10

if num > 0:
    print("The number is positive")
# Output: The number is positive
```

#### 2. `if-else` Statement

The `if-else` statement evaluates a condition and executes one block of code if the condition is `True`, and another block of code if the condition is `False`.

**Syntax**:
```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

**Example**:
```python
num = -5

if num > 0:
    print("The number is positive")
else:
    print("The number is non-positive")
# Output: The number is non-positive
```

#### 3. `if-elif-else` Ladder

The `if-elif-else` ladder evaluates multiple conditions. It executes the block of code corresponding to the first `True` condition. If none of the conditions are `True`, it executes the code in the `else` block.

**Syntax**:
```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition2 is True
elif condition3:
    # block of code to execute if condition3 is True
else:
    # block of code to execute if none of the conditions are True
```

**Example**:
```python
num = 0

if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
# Output: The number is zero
```

#### 4. Nested `if` Statements

Nested `if` statements are `if` statements within other `if` statements. They are used to check multiple conditions within a condition.

**Syntax**:
```python
if condition1:
    # block of code to execute if condition1 is True
    if condition2:
        # block of code to execute if condition2 is True
```

**Example**:
```python
num = 10

if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
# Output:
# The number is positive
# The number is even
```

### Important Information for Learners 📘

1. **Indentation**:
   - Python uses indentation (whitespace at the beginning of lines) to define the scope of loops, functions, and conditional blocks. Ensure consistent indentation to avoid errors.
   ```python
   if True:
       print("Hello")
   ```

2. **Boolean Expressions**:
   - Conditions in `if` statements are evaluated as Boolean expressions, which can be either `True` or `False`.
   ```python
   a = 5
   b = 10
   print(a < b)  # True
   ```

3. **Logical Operators**:
   - You can combine multiple conditions using logical operators (`and`, `or`, `not`).
   ```python
   a = 5
   b = 10
   if a < b and b < 20:
       print("Both conditions are True")
   ```

4. **Chained Comparisons**:
   - Python supports chained comparisons, which are a shorthand way of writing multiple comparisons in a single statement.
   ```python
   x = 5
   if 0 < x < 10:
       print("x is between 0 and 10")
   ```

5. **`pass` Statement**:
   - Use the `pass` statement as a placeholder in an empty `if` statement to avoid errors.
   ```python
   if condition:
       pass  # TODO: Implement this later
   ```

6. **`elif` versus `else if`**:
   - Unlike some other programming languages, Python uses `elif` instead of `else if`.
   ```python
   if condition1:
       pass
   elif condition2:
       pass
   ```

Understanding these conditional statements and their nuances is crucial for controlling the flow of your programs in Python. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Modules in Python](/Python/Articles/13_modules.md) 📦