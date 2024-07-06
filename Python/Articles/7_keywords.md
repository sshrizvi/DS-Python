# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Taking Inputs in Python](/Python/Articles/6_taking_inputs_in_python.md) 🖥️

## Keywords in Python 🔑

Keywords in Python are reserved words that have a special meaning and purpose. They are part of the syntax and cannot be used as identifiers (names for variables, functions, classes, etc.). 

Here's a comprehensive list of all the keywords used in Python, along with a brief description of each:

| Keyword   | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| `False`   | Represents the boolean value `False`.                                       |
| `None`    | Represents the absence of a value or a null value.                          |
| `True`    | Represents the boolean value `True`.                                        |
| `and`     | Logical AND operator.                                                       |
| `as`      | Used to create an alias while importing a module.                           |
| `assert`  | Used for debugging purposes to test if a condition is true.                 |
| `async`   | Declares an asynchronous function (used with `await`).                      |
| `await`   | Used to wait for the result of an async function.                           |
| `break`   | Exits a loop prematurely.                                                   |
| `class`   | Used to define a new user-defined class.                                    |
| `continue`| Skips the rest of the code inside a loop for the current iteration.         |
| `def`     | Used to define a new user-defined function.                                 |
| `del`     | Used to delete objects.                                                     |
| `elif`    | Used in conditional statements, same as else if.                            |
| `else`    | Used in conditional statements.                                             |
| `except`  | Used with exceptions, what to do when an exception occurs.                  |
| `finally` | Used with exceptions, a block of code that will be executed no matter what. |
| `for`     | Used to create a for loop.                                                  |
| `from`    | Used to import specific parts of a module.                                  |
| `global`  | Declares a variable as global.                                              |
| `if`      | Used to make a conditional statement.                                       |
| `import`  | Used to import a module.                                                    |
| `in`      | Used to check if a value is present in a list, tuple, etc.                  |
| `is`      | Tests for object identity.                                                  |
| `lambda`  | Used to create an anonymous function.                                       |
| `nonlocal`| Declares a variable as non-local.                                           |
| `not`     | Logical NOT operator.                                                       |
| `or`      | Logical OR operator.                                                        |
| `pass`    | A null statement, a statement that will do nothing.                         |
| `raise`   | Used to raise an exception.                                                 |
| `return`  | Exits a function and returns a value.                                       |
| `try`     | Used to make a try...except statement.                                      |
| `while`   | Used to create a while loop.                                                |
| `with`    | Used to simplify exception handling.                                        |
| `yield`   | Used inside a function to return a generator.                               |

### Additional Information

1. **Reserved Words**:
   - Keywords are reserved and cannot be used as variable names, function names, or any other identifier.
   ```python
   # Incorrect usage
   def return(x):
       return x  # SyntaxError

   # Correct usage
   def my_function(x):
       return x
   ```

2. **Case Sensitivity**:
   - Keywords are case-sensitive. For example, `True` is a keyword, but `true` is not.
   ```python
   print(True)  # Correct, prints: True
   print(true)  # NameError: name 'true' is not defined
   ```

3. **Contextual Keywords**:
   - Some keywords like `async` and `await` are used in specific contexts (e.g., asynchronous programming).
   ```python
   async def main():
       await some_async_function()
   ```

4. **`None` as a Placeholder**:
   - `None` is often used as a default value for function arguments or to represent the absence of a value.
   ```python
   def greet(name=None):
       if name is None:
           name = "Stranger"
       print("Hello, " + name)
   ```

5. **Boolean Values**:
   - `True` and `False` are used to represent boolean values, which are essential for control flow and logical operations.
   ```python
   is_valid = True
   if is_valid:
       print("The input is valid.")
   ```

6. **Importing Modules**:
   - `import`, `from`, and `as` are used for importing modules and creating aliases.
   ```python
   import math
   from math import sqrt
   import math as m

   print(math.sqrt(16))
   print(sqrt(16))
   print(m.sqrt(16))
   ```

Understanding these keywords and their usage is crucial for mastering Python programming. If you have any questions or need more examples, feel free to ask! 😊

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->