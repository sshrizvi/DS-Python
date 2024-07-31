# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Functions at Memory Level](/Python/Articles/35_function_at_memory_level.md)

# Functions - A First Class Object

## Definition of First Class Objects

In programming, a first-class object (or first-class citizen) is an entity that can be:
- Passed as an argument to a function
- Returned from a function
- Assigned to a variable
- Stored in data structures

First-class objects support all the operations generally available to other entities in the language.

## Functions as First Class Objects

In Python, functions are first-class objects. This means that functions can be used in the same way as any other data type, like integers, strings, or lists. This property provides Python with great flexibility and power in its functional programming capabilities.

### 1. Reassigning Functions

Functions can be reassigned to variables, allowing the same function to be called using different names.

```python
def greet(name):
    return f"Hello, {name}!"

# Reassigning the function to a variable
say_hello = greet

print(say_hello("Alice"))  # Output: Hello, Alice!
```

### 2. Deleting Functions

Functions can be deleted using the `del` keyword.

```python
def farewell(name):
    return f"Goodbye, {name}!"

# Deleting the function
del farewell

# print(farewell("Bob"))  # This will raise a NameError as the function is deleted
```

### 3. Storing Functions in Iterables

Functions can be stored in iterables such as lists, dictionaries, and sets.

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Storing functions in a list
operations = [add, multiply]

# Using functions from the list
print(operations[0](2, 3))  # Output: 5 (add function)
print(operations[1](2, 3))  # Output: 6 (multiply function)
```

### 4. Passing Functions as Arguments

Functions can be passed as arguments to other functions.

```python
def execute_operation(operation, a, b):
    return operation(a, b)

result = execute_operation(add, 5, 3)
print(result)  # Output: 8
```

### 5. Returning Functions from Other Functions

Functions can return other functions.

```python
def outer_function(msg):
    def inner_function():
        return f"Message: {msg}"
    return inner_function

func = outer_function("Hello, World!")
print(func())  # Output: Message: Hello, World!
```

## Properties of Functions as First-Class Objects

### Immutability

Functions themselves are immutable. Once a function is defined, its behavior cannot be changed without redefining it.

```python
def original_function():
    return "I am the original function."

# Attempting to change the function's behavior directly is not possible.
# We can only redefine or reassign a new function.
```

### Benefits of Functions as First-Class Objects

1. **Higher-Order Functions**: Functions that take other functions as arguments or return functions.
    - Example: `map()`, `filter()`, and `reduce()` functions.

    ```python
    def square(x):
        return x * x

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
    ```

2. **Functional Programming**: Allows for functional programming paradigms, promoting concise and expressive code.
    - Example: Lambda functions and function chaining.

    ```python
    numbers = [1, 2, 3, 4, 5]
    even_squares = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
    print(even_squares)  # Output: [4, 16]
    ```

3. **Callbacks and Event Handling**: Useful in event-driven programming where functions can be passed as callbacks.
    - Example: GUI applications and asynchronous programming.

    ```python
    def on_event(callback):
        # Simulate an event
        callback("Event triggered")

    def handle_event(message):
        print(message)

    on_event(handle_event)  # Output: Event triggered
    ```

4. **Decorators**: Functions that modify the behavior of other functions.
    - Example: Logging, access control, and memoization.

    ```python
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f"Function {original_function.__name__} is being called")
            return original_function(*args, **kwargs)
        return wrapper_function

    @decorator_function
    def display():
        print("Display function ran")

    display()
    # Output:
    # Function display is being called
    # Display function ran
    ```

## Conclusion

Understanding that functions in Python are first-class objects unlocks a plethora of programming techniques and paradigms. This knowledge enables developers to write more modular, flexible, and reusable code. By leveraging the power of first-class functions, one can implement advanced programming concepts such as higher-order functions, decorators, and functional programming patterns, making Python a versatile and powerful language.

> [!TIP]  
> Link to Next Article  
> 🡺 [Nested Functions](/Python/Articles/37_nested_functions.md)