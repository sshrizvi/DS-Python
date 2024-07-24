# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Loops in Python](/Python/Articles/14_loops.md) 🔄

## Loop Control Statements in Python 🛑

Loop control statements change the execution flow of loops. Python provides three main loop control statements:

1. **`break`**: Exits the loop immediately.
2. **`continue`**: Skips the current iteration and proceeds to the next iteration.
3. **`pass`**: Does nothing and serves as a placeholder.

### 1. `break` Statement

The `break` statement is used to exit a loop prematurely, regardless of the original loop condition.

**Syntax**:
```python
break
```

**Example**:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4
```

**Use Case**: 
- Exiting a loop when a certain condition is met, such as finding an item in a list or meeting a specific criterion.

### 2. `continue` Statement

The `continue` statement skips the rest of the code inside the current iteration of the loop and moves to the next iteration.

**Syntax**:
```python
continue
```

**Example**:
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
```

**Use Case**:
- Skipping specific iterations, such as ignoring even numbers in a loop that processes numbers.

### 3. `pass` Statement

The `pass` statement does nothing and is used as a placeholder for future code.

**Syntax**:
```python
pass
```

**Example**:
```python
for i in range(10):
    if i % 2 == 0:
        pass  # To be implemented later
    else:
        print(i)
# Output: 1 3 5 7 9
```

**Use Case**:
- Defining empty loops, functions, classes, or conditionals that will be implemented later.

### Use Cases and Important Points 📘

#### Use Cases

1. **Searching in a Collection**:
   - Use `break` to exit the loop when an item is found.
   ```python
   items = [1, 2, 3, 4, 5]
   for item in items:
       if item == 3:
           print("Item found")
           break
   ```

2. **Skipping Certain Conditions**:
   - Use `continue` to skip over items that do not meet a condition.
   ```python
   items = [1, 2, 3, 4, 5]
   for item in items:
       if item % 2 == 0:
           continue
       print(f"Odd item: {item}")
   ```

3. **Placeholder for Future Code**:
   - Use `pass` when writing code that you plan to implement later.
   ```python
   def my_function():
       pass  # TODO: Implement this function
   ```

#### Important Points

1. **Readability**:
   - Use loop control statements judiciously to maintain readability and prevent confusion.

2. **Efficient Loop Termination**:
   - `break` can make loops more efficient by terminating unnecessary iterations once the desired condition is met.

3. **Conditional Checks**:
   - `continue` helps in conditional checks, especially when dealing with large datasets or complex conditions.

4. **Development Placeholders**:
   - `pass` is useful during development for defining functions, loops, and conditionals without immediately implementing their functionality.

### Examples

#### Example 1: Using `break`
```python
# Finding a number in a list
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    if number == 30:
        print("Number found!")
        break
# Output: Number found!
```

#### Example 2: Using `continue`
```python
# Skipping even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
```

#### Example 3: Using `pass`
```python
# Placeholder for future code
for i in range(1, 6):
    if i % 2 == 0:
        pass  # Placeholder for code to handle even numbers
    else:
        print(f"Odd number: {i}")
# Output: Odd number: 1 Odd number: 3 Odd number: 5
```

Understanding and using loop control statements effectively can greatly enhance the control and efficiency of your programs. If you have any questions or need further clarification, feel free to ask! 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Strings in Python](/Python/Articles/16_strings.md)📜