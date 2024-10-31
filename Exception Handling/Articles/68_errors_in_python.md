# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Serialization in Python: Custom Data Types, Pickling, and JSON](/File%20Handling/Articles/67_pickling.md)

# Understanding Errors in Python: Types, Causes, and Examples

In programming, errors are inevitable. They help identify logical, syntactical, or runtime issues in code. Python, being an interpreted language, is designed with robust error-handling mechanisms that make it easier to identify and resolve errors during development. In this article, we’ll explore the types of errors in Python, the general classification, and common errors such as `IndexError`, `ModuleNotFoundError`, `KeyError`, `TypeError`, `ValueError`, `NameError`, and `AttributeError`.

## 1. Types of Errors in Python

Errors in Python can be broadly classified into three main categories:

### a. Syntax Errors
Syntax errors occur when code is not written according to Python’s syntax rules. These errors prevent the interpreter from parsing the code, resulting in immediate failure. Syntax errors are usually caused by typos, incorrect indentation, or missing punctuation.

**Example:**
```python
if x = 5    # SyntaxError due to using '=' instead of '=='
    print(x)
```

### b. Runtime Errors
Runtime errors occur during the execution of code after it has successfully passed the syntax check. These errors are usually due to logic issues, incorrect operations, or invalid references. The code fails at runtime, and Python generates exceptions, which are error messages that help diagnose the issue.

### c. Logical Errors
Logical errors do not raise any exceptions but lead to incorrect results. They occur when code executes without errors, but the output is not what was intended due to logical mistakes.

**Example:**
```python
def add(x, y):
    return x - y  # Logical Error: should be x + y
```

## 2. Common Runtime Errors and Their Causes

Python has built-in error types that indicate specific issues in the code. Here’s an overview of some common errors and their causes:

### a. `IndexError`

An `IndexError` occurs when attempting to access an index that is out of the range of a list, tuple, or other indexable objects. This error is common in loops or when accessing data structures based on index positions.

**Example:**
```python
my_list = [1, 2, 3]
print(my_list[5])  # IndexError: list index out of range
```

**Cause:** Accessing a position that doesn’t exist in the list (in this case, index `5`).

**Tip for Avoidance:** Always check the length of lists or arrays before accessing elements by index.

### b. `ModuleNotFoundError`

`ModuleNotFoundError` occurs when Python cannot locate a module that you’re trying to import. This typically results from misspelled module names, incorrect paths, or missing installations.

**Example:**
```python
import non_existent_module  # ModuleNotFoundError: No module named 'non_existent_module'
```

**Cause:** Trying to import a module that isn’t available or is misspelled.

**Tip for Avoidance:** Verify that the module name is correct and installed in the Python environment.

### c. `KeyError`

A `KeyError` is raised when attempting to access a key that doesn’t exist in a dictionary. This is common when working with dynamic data or trying to retrieve values from dictionaries without verifying the existence of keys.

**Example:**
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # KeyError: 'c'
```

**Cause:** The key `c` is not in `my_dict`.

**Tip for Avoidance:** Use `dict.get(key, default)` to safely retrieve values from dictionaries without causing `KeyError`.

### d. `TypeError`

A `TypeError` occurs when an operation or function is applied to an object of an inappropriate type. This error is commonly seen in arithmetic operations, concatenations, or when calling functions with incorrect argument types.

**Example:**
```python
print("Age: " + 25)  # TypeError: can only concatenate str (not "int") to str
```

**Cause:** Attempting to concatenate a string with an integer without conversion.

**Tip for Avoidance:** Ensure type compatibility before performing operations. Convert values where necessary (e.g., `str(25)`).

### e. `ValueError`

A `ValueError` occurs when a function receives an argument of the correct type but with an inappropriate value. This error frequently arises during data processing or type conversions.

**Example:**
```python
int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'
```

**Cause:** Trying to convert a non-numeric string to an integer.

**Tip for Avoidance:** Check values before conversion, especially when dealing with user input or unstructured data.

### f. `NameError`

A `NameError` occurs when a local or global name is not found. This typically happens when trying to use a variable or function that hasn’t been defined.

**Example:**
```python
print(x)  # NameError: name 'x' is not defined
```

**Cause:** Attempting to access a variable that hasn’t been initialized or imported.

**Tip for Avoidance:** Double-check variable definitions and scope. Ensure variables are defined before use.

### g. `AttributeError`

An `AttributeError` occurs when trying to access an attribute or method that doesn’t exist on an object. This is common when working with class instances or library functions.

**Example:**
```python
my_list = [1, 2, 3]
my_list.push(4)  # AttributeError: 'list' object has no attribute 'push'
```

**Cause:** The `list` type in Python doesn’t have a `push` method; `append` should be used instead.

**Tip for Avoidance:** Refer to documentation to confirm available methods and attributes. Avoid typos in attribute names.

## Dead-Ends and Difficult Situations

Errors can be more challenging when working with:
- **Dynamic Data**: Accessing keys or indexes in data that change structure frequently, such as data from APIs or user inputs.
- **Nested Data Structures**: Lists or dictionaries within other data structures require careful error handling, particularly `KeyError` and `IndexError`.
- **Data Processing Pipelines**: When processing data through multiple stages, errors can propagate, making debugging difficult.

Handling errors with proper logging and exception handling helps in understanding where issues originate, especially in complex pipelines.

## Error Handling Best Practices for Data Scientists

For data scientists, error handling is critical because data processing often involves unstructured data, APIs, and machine learning models with unpredictable behaviors. Here are a few strategies for better error handling:

1. **Use Try-Except Blocks**: Wrap code in `try-except` blocks to handle errors gracefully.
2. **Check for Key and Index Existence**: Validate keys in dictionaries and indexes in lists before accessing them.
3. **Type Checking**: Use `isinstance()` to verify data types before performing operations.
4. **Logging**: Log errors for tracking issues, especially in data processing pipelines.
5. **Data Validation**: Clean and validate data inputs to minimize `ValueError` and `TypeError` occurrences.

Errors are a natural part of coding, and understanding how to identify and handle them is crucial to writing robust, efficient Python code. By mastering error handling techniques, you can enhance your data processing skills, leading to more stable, reliable programs and data workflows.

> [!TIP]  
> Link to Next Article  
> 🡺 [Understanding Exceptions in Python: Concepts, Differences, and Importance of Handling Them](/Exception%20Handling/Articles/69_exceptions.md)