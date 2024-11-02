# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Namespaces in Python: A Comprehensive Guide for Intermediate Learners](/NameSpaces%20&%20Decorators/Articles/73_namespaces.md)

# Understanding Scopes in Python: A Guide to Mastering Variable Access and the LEGB Rule

In Python, **scope** determines where a variable is accessible in your code. Understanding scope is essential because it helps you manage variables and avoid accidental modifications or conflicts, making your code cleaner and less error-prone. In this article, we’ll delve into the concept of scopes, explain how Python searches for variables using the **LEGB rule**, and provide illustrative examples to help clarify these ideas.

## What is Scope in Python?

In programming, **scope** refers to the region of a program where a variable or function is accessible. Python, like many other languages, has specific rules for determining where variables are visible and where they aren’t. In Python, these rules are defined by **scopes**.

### Types of Scopes in Python

Python has four main types of scopes, each of which dictates where variables are accessible:

1. **Local Scope**: Variables created inside a function belong to the local scope of that function. They can only be accessed within that function.
2. **Enclosing Scope**: When functions are nested, the enclosing scope refers to the outer function’s local scope.
3. **Global Scope**: Variables declared outside any function or class belong to the global scope and can be accessed from anywhere in the module.
4. **Built-in Scope**: Python has a built-in scope that includes all built-in functions and exceptions, such as `print()`, `len()`, and `ValueError`.

Let’s go through these types one by one with examples to understand them better.

## Understanding Scopes with Examples

### 1. Local Scope

A **local scope** is created whenever a function is called. Variables declared inside the function are local to that function and cannot be accessed from outside.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Outputs: 10
print(x)       # Raises an error because 'x' is not defined outside the function
```

In this example:
- `x` is defined within the function `my_function` and is local to it.
- Trying to access `x` outside the function raises an error because `x` only exists within the function.

### 2. Global Scope

Variables defined outside of any function are considered to be in the **global scope** and can be accessed from anywhere within the same module.

```python
y = 20  # Global variable

def show_y():
    print(y)  # Accessing global variable

show_y()      # Outputs: 20
print(y)      # Outputs: 20
```

Here:
- The variable `y` is defined outside any function, making it global.
- Both `show_y()` and the print statement outside the function can access `y` without any issues.

## Introducing the LEGB Rule

Python resolves names using the **LEGB rule**. LEGB stands for **Local, Enclosing, Global, and Built-in** and defines the order in which Python searches for variable names.

1. **Local (L)**: The local scope, which is the innermost scope, typically refers to variables inside the current function.
2. **Enclosing (E)**: The enclosing scope is the next level up and refers to non-global, non-local scopes in nested functions.
3. **Global (G)**: The global scope contains variables defined at the module level.
4. **Built-in (B)**: The built-in scope contains Python’s built-in functions and exceptions.

Python follows this order, so if it doesn’t find the variable in the local scope, it moves to the enclosing scope, then to the global scope, and finally to the built-in scope.

### LEGB Rule in Action

Let’s look at examples that illustrate how Python applies the LEGB rule.

## Example 1: Local Scope with Nested Functions

```python
def outer_function():
    x = "outer"  # Enclosing scope

    def inner_function():
        x = "inner"  # Local scope
        print(x)

    inner_function()

outer_function()  # Outputs: inner
```

Explanation:
- The variable `x` in `inner_function` is local to it, so Python prints `"inner"`.
- Even though there is an `x` variable in `outer_function`, it’s not used because Python finds `x` in the local scope of `inner_function` first.

## Example 2: Enclosing Scope

```python
def outer_function():
    x = "outer"  # Enclosing scope

    def inner_function():
        print(x)  # Accessing the enclosing variable

    inner_function()

outer_function()  # Outputs: outer
```

Explanation:
- `x` is defined in the `outer_function`, and there’s no `x` in `inner_function`.
- Python applies the LEGB rule, finds `x` in the enclosing scope (outer function), and prints `"outer"`.

## Example 3: Using Global Scope

```python
x = "global"  # Global scope

def show_x():
    print(x)

show_x()      # Outputs: global
print(x)      # Outputs: global
```

Explanation:
- Since `x` is defined outside any function, it’s in the global scope.
- Both `show_x()` and the print statement outside the function access the global `x`, resulting in `"global"`.

## Example 4: Modifying Global Variables within a Function

To modify a global variable inside a function, you need to use the `global` keyword. 

```python
x = 5  # Global variable

def modify_x():
    global x
    x = 10  # Modify global x
    print(x)

modify_x()  # Outputs: 10
print(x)    # Outputs: 10
```

Explanation:
- By declaring `x` as `global` inside `modify_x`, you modify the global `x`.
- This changes the value of `x` globally, not just within the function.

> **Caution**: Using `global` can lead to hard-to-debug code and should be used sparingly. It’s often better to pass variables as function arguments.

## Example 5: Built-in Scope

```python
def length(item):
    return len(item)  # 'len' is a built-in function in Python

print(length("Python"))  # Outputs: 6
```

Explanation:
- The function `len` is part of Python’s built-in scope.
- Even though we haven’t defined `len` ourselves, it’s available because Python includes it in the built-in scope.

### LEGB Rule in a Complex Example

Let’s see how the LEGB rule applies when we have variables with the same name in different scopes.

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)
    
    inner()

outer()  # Outputs: local
```

Explanation:
- `inner()` has its own local `x`, so it prints `"local"`.
- If the `x` inside `inner()` was missing, Python would look at the `enclosing` scope and use that `x`.
- If both local and enclosing scopes lacked `x`, Python would check the global scope and use `"global"`.

## Common Errors and Gotchas with Scope

1. **UnboundLocalError**: This occurs when you try to reference a variable before it’s assigned in the local scope.

   ```python
   def show_x():
       print(x)  # Error: x is referenced before assignment
       x = 10

   show_x()
   ```

   **Fix**: Initialize `x` before referencing it or declare it as `global`.

2. **Accidental Global Modifications**: Modifying a global variable from within a function without `global` keyword may raise errors or cause unexpected behavior.

3. **Shadowing Built-in Names**: Avoid using names that match built-in functions (like `len` or `list`). Doing so can override the built-in functions and lead to unexpected behavior.

## Conclusion

Understanding scopes and the LEGB rule is a powerful way to manage variables effectively in Python. By recognizing where variables exist and how they interact in different scopes, you can write code that’s clear, efficient, and free from common pitfalls.

In summary:
- **Local Scope**: Variables defined inside a function.
- **Enclosing Scope**: Variables in outer functions for nested functions.
- **Global Scope**: Variables defined outside any function.
- **Built-in Scope**: Python’s built-in functions and constants.

Mastering scope and the LEGB rule helps you create clean, bug-free code by understanding variable access and lifecycle. Test these concepts in your own projects, and you’ll see how much control and clarity they bring to your Python code!

> [!TIP]  
> Link to Next Article  
> 🡺 [Exploring the Built-in Namespace in Python](/NameSpaces%20&%20Decorators/Articles/75_builtins.md)