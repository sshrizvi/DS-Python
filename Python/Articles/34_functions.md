# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Dictionary Comprehensions](/Python/Articles/33_dictionary_comprehensions.md)

# Functions in Python

## 1. Definition of Function

A function in Python is a block of reusable code designed to perform a specific task. Functions help break down complex problems into smaller, manageable pieces, promoting code reusability and organization.

## 2. Syntax of Function in Python

The basic syntax of a function in Python is:

```python
def function_name(parameters):
    """docstring"""
    # function body
    return value
```

- `def`: The keyword used to define a function.
- `function_name`: A unique name to identify the function.
- `parameters`: Optional. A list of parameters the function can accept.
- `"""docstring"""`: Optional. A string that describes the function.
- `# function body`: The block of code that performs the function’s task.
- `return value`: Optional. The value that the function returns.

## 3. The `def` Keyword

The `def` keyword is used to define a new user-defined function. This keyword tells Python that a new function block is starting.

## 4. Structure of Function

### Function Signature

The function signature consists of the function name and the parameter list.

```python
def greet(name):
    """Greets a person with their name"""
    print(f"Hello, {name}!")
```

### Parameters

Parameters are variables listed inside the parentheses in the function definition.

```python
def add(a, b):
    return a + b
```

### Function Name

The function name should be descriptive of the task the function performs.

### Definition

The function definition is the block of code that performs the specific task.

### Docstrings

Docstrings are optional but recommended. They describe what the function does and how to use it.

```python
def multiply(a, b):
    """Returns the product of two numbers a and b"""
    return a * b
```

## 5. How to Access Documentation of Any Function?

You can access the documentation of any function using the `help()` function or the `__doc__` attribute.

```python
help(multiply)
# Or
print(multiply.__doc__)
```

## 6. Difference Between Parameters and Arguments

- **Parameters** are variables in the function definition.
- **Arguments** are the actual values passed to the function when it is called.

```python
def subtract(a, b):  # a and b are parameters
    return a - b

result = subtract(10, 5)  # 10 and 5 are arguments
```

## 7. Types of Arguments

### Positional Arguments

Arguments passed in the same order as the parameters.

```python
def power(base, exponent):
    return base ** exponent

result = power(2, 3)  # Positional arguments: 2 and 3
```

### Keyword Arguments

Arguments passed using the parameter names as keywords.

```python
result = power(base=2, exponent=3)  # Keyword arguments: base=2, exponent=3
```

### Default Arguments

Parameters that assume a default value if a value is not provided.

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Uses default message
greet("Bob", "Hi")  # Overrides default message
```

## 8. *args and **kwargs

### *args

`*args` allows a function to accept any number of positional arguments.

```python
def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4)  # Accepts any number of arguments
```

### **kwargs

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")  # Accepts any number of keyword arguments
```

## Examples

### Example 1: Function with Positional Arguments

```python
def divide(a, b):
    return a / b

result = divide(10, 2)
print(result)  # Output: 5.0
```

### Example 2: Function with Default Arguments

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!
```

### Example 3: Function with *args

```python
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4))  # Output: 24
```

### Example 4: Function with **kwargs

```python
def print_user_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

## Conclusion

Functions are fundamental building blocks in Python, allowing for code reusability and modularity. Understanding the syntax, structure, and types of arguments in functions, as well as how to use *args and **kwargs, can greatly enhance your ability to write efficient and readable code.

> [!TIP]  
> Link to Next Article  
> 🡺 [Functions at Memory Level](/Python/Articles/35_function_at_memory_level.md)