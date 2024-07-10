# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Modules in Python](/Python/Articles/13_modules.md) 📦

## Loops in Python 🔄

Loops are used in programming to repeat a block of code as long as a specified condition is met. Python provides two main types of loops: `while` loops and `for` loops. Additionally, Python has unique constructs like `else` clauses in loops and supports nested loops.

### 1. `while` Loop

The `while` loop repeats a block of code as long as a specified condition is `True`.

**Syntax**:
```python
while condition:
    # block of code
```

**Example**:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 2. `for` Loop

The `for` loop iterates over a sequence (like a list, tuple, dictionary, set, or string) and executes a block of code for each element in the sequence.

**Syntax**:
```python
for variable in sequence:
    # block of code
```

**Example**:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 3. `while-else` Loop

The `else` block in a `while` loop is executed when the loop condition becomes `False`. If the loop is terminated by a `break` statement, the `else` block is not executed.

**Syntax**:
```python
while condition:
    # block of code
else:
    # block of code to execute when the condition becomes False
```

**Example**:
```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count reached 5")
```

### 4. `for-else` Loop

The `else` block in a `for` loop is executed when the loop has iterated over all elements in the sequence. If the loop is terminated by a `break` statement, the `else` block is not executed.

**Syntax**:
```python
for variable in sequence:
    # block of code
else:
    # block of code to execute when the loop completes normally
```

**Example**:
```python
for num in range(5):
    print(num)
else:
    print("Loop completed")
```

### 5. Nested Loops

Nested loops are loops inside another loop. Both `for` and `while` loops can be nested.

**Syntax**:
```python
for variable1 in sequence1:
    for variable2 in sequence2:
        # block of code
```

**Example**:
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

### Differences from Other Programming Languages

1. **`else` Clause in Loops**:
   - Python's `else` clause in loops is not common in many other programming languages. It provides a way to execute code after the loop completes normally.

2. **Indentation**:
   - Python uses indentation to define the scope of loops, which makes the code visually clean and structured. Other languages often use curly braces `{}` or keywords like `begin` and `end`.

3. **Dynamic Typing**:
   - Python's dynamic typing allows you to use loops with sequences of various data types without explicit type declarations.

### Important Points for Learners 📘

1. **Avoid Infinite Loops**:
   - Ensure that the loop condition will eventually become `False` to prevent infinite loops.
   ```python
   count = 0
   while count < 5:
       print(count)
       # Make sure to update 'count' to avoid an infinite loop
       count += 1
   ```

2. **Break and Continue Statements**:
   - Use `break` to exit the loop prematurely and `continue` to skip the current iteration and proceed to the next iteration.
   ```python
   for i in range(10):
       if i == 5:
           break
       if i % 2 == 0:
           continue
       print(i)
   ```

3. **Enumerate and Zip Functions**:
   - Use `enumerate()` to get both the index and the value in a loop, and `zip()` to iterate over multiple sequences in parallel.
   ```python
   fruits = ["apple", "banana", "cherry"]
   for index, fruit in enumerate(fruits):
       print(index, fruit)

   names = ["Alice", "Bob", "Charlie"]
   ages = [25, 30, 35]
   for name, age in zip(names, ages):
       print(name, age)
   ```

4. **Iterating over Dictionaries**:
   - Use methods like `items()`, `keys()`, and `values()` to iterate over dictionaries.
   ```python
   my_dict = {"a": 1, "b": 2, "c": 3}
   for key, value in my_dict.items():
       print(key, value)
   ```

5. **List Comprehensions**:
   - Use list comprehensions for concise and readable loop-based list operations.
   ```python
   squares = [x**2 for x in range(10)]
   print(squares)
   ```

Understanding loops and their various constructs in Python is fundamental to mastering control flow and efficient programming. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Loop Control Statements in Python](/Python/Articles/15_loop_control_statements.md) 🛑