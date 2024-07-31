# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Functions - A First Class Object](/Python/Articles/36_functions_are_first_class_objects.md)

# Nested Functions

## Definition

A nested function is a function defined inside another function. In Python, functions can be nested to any depth, meaning one function can contain another function, which can contain another, and so on. Nested functions are primarily used to encapsulate functionality and create closures.

## Syntax

The syntax for nested functions in Python involves defining one function inside another. The inner function can access the variables of the outer function, creating a closure.

```python
def outer_function():
    def inner_function():
        print("This is the inner function")
    inner_function()
```

## Uses of Nested Functions

1. **Encapsulation**: Nested functions help in encapsulating the logic of the inner function, making the outer function self-contained.
2. **Closures**: Nested functions can capture and carry some of the outer function’s state with them, allowing the inner function to remember the state even after the outer function has finished execution.
3. **Helper Functions**: They are useful for defining small helper functions that are only relevant within the context of the outer function.
4. **Decorators**: Nested functions are commonly used in implementing decorators, which modify the behavior of other functions.

## Examples

### 1. Basic Nested Function

```python
def greet(name):
    def display_message():
        print(f"Hello, {name}!")
    display_message()

greet("Alice")
```

### 2. Closures

Closures are a powerful feature of nested functions, allowing the inner function to remember the state of the outer function even after the outer function has finished execution.

```python
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

my_function = outer_function("Hello, World!")
my_function()  # Output: Hello, World!
```

### 3. Nested Functions as Helper Functions

```python
def calculate_area(radius):
    def area():
        return 3.14 * radius ** 2
    return area()

print(calculate_area(5))  # Output: 78.5
```

### 4. Implementing Decorators

```python
def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()
# Output:
# Wrapper executed before display
# Display function executed
```

### 5. Nested Function with Multiple Inner Functions

```python
def outer_function(x):
    def inner_function1():
        return x + 1

    def inner_function2():
        return x + 2

    return inner_function1() + inner_function2()

print(outer_function(10))  # Output: 23
```

## Advantages of Nested Functions

1. **Encapsulation**: Keeps the code organized and readable by encapsulating functionality within the outer function.
2. **State Preservation**: Useful in scenarios where state needs to be preserved across function calls, as with closures.
3. **Scoped Helper Functions**: Allows defining helper functions that are not exposed outside their containing function, reducing the global namespace pollution.
4. **Decorator Implementation**: Simplifies the creation of decorators that can modify or extend the behavior of other functions.

## Important Points

- **Scope**: The inner function has access to the variables and parameters of the outer function but not vice versa.
- **Lifespan**: Inner functions can outlive the outer function when returned as closures, preserving the state of the outer function’s environment.
- **Access to Variables**: Variables of the outer function can be accessed in the inner function but must be declared as `nonlocal` if they need to be modified.

### Example: Using `nonlocal`

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print(x)
    inner()
    print(x)

outer()
# Output:
# 15
# 15
```

## Conclusion

Nested functions in Python provide a powerful mechanism for creating closures, encapsulating functionality, and implementing decorators. They enhance the modularity and readability of code by keeping related functionalities together and allowing functions to capture the state of their enclosing environment. Understanding and utilizing nested functions effectively can lead to more organized, maintainable, and efficient code.

> [!TIP]  
> Link to Next Article  
> 🡺 [Some Useful Functions for Data Scientists](/Python/Articles/38_miscellaneous_functions.md)