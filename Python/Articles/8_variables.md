# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Keywords in Python](/Python/Articles/7_keywords.md) 🔑

## Variables in Python 📝

In Python, a variable is a name that refers to a value. Variables are essential for storing data and performing operations on that data. Python variables are dynamic, meaning they can change type and value during execution.

### Variable Declaration and Assignment:

- **Declaration and Initialization**: Variables are created when you assign a value to them.
  ```python
  x = 10      # x is an integer
  y = "hello" # y is a string
  z = 3.14    # z is a float
  ```

- **Dynamic Typing**: Variables can change type dynamically.
  ```python
  a = 5
  a = "now a string"
  ```

### Naming Variables:

1. **Rules**:
   - Must start with a letter (a-z, A-Z) or an underscore (_).
   - Followed by letters, numbers (0-9), or underscores.
   - Case-sensitive: `variable` and `Variable` are different.
   - Cannot use Python keywords or reserved words (like `if`, `else`, `for`).

2. **Conventions**:
   - Use meaningful names to make your code readable and maintainable.
   - Use lowercase words separated by underscores (snake_case) for variable names.
   ```python
   first_name = "John"
   last_name = "Doe"
   age = 30
   ```

3. **Special Variables**:
   - Variables starting and ending with double underscores (`__`) are typically reserved for special use in Python (magic methods).
   ```python
   __init__, __str__, __name__
   ```

### Special Variable Declaration Techniques:

1. **Multiple Assignment**:
   - You can assign multiple variables in a single line.
   ```python
   x, y, z = 1, 2, 3
   ```

2. **Swapping Variables**:
   - Python allows easy swapping of variable values.
   ```python
   a, b = 5, 10
   a, b = b, a
   ```

3. **Unpacking**:
   - Assign values from a list or tuple to multiple variables.
   ```python
   my_list = [1, 2, 3]
   a, b, c = my_list
   ```

4. **Global Variables**:
   - Declared outside of functions and accessible inside any function in the code.
   ```python
   global_var = "I am global"

   def my_function():
       global global_var
       global_var = "Modified global"
   ```

5. **Nonlocal Variables**:
   - Used in nested functions to refer to variables in the nearest enclosing scope that is not global.
   ```python
   def outer_function():
       outer_var = "outer"

       def inner_function():
           nonlocal outer_var
           outer_var = "modified outer"
       
       inner_function()
       print(outer_var)  # Output: modified outer
   ```

### Key Points for Learners:

1. **Use Meaningful Names**:
   - Variables should have names that convey their purpose.
   ```python
   count = 10  # Good
   c = 10      # Not descriptive
   ```

2. **Consistency**:
   - Stick to a consistent naming convention (e.g., snake_case) throughout your code.
   ```python
   total_cost = 100  # Consistent
   totalCost = 100   # Inconsistent with snake_case
   ```

3. **Avoid Using Reserved Words**:
   - Do not use Python keywords as variable names.
   ```python
   # Incorrect
   if = 5

   # Correct
   condition = 5
   ```

4. **Keep Scope in Mind**:
   - Be aware of the scope of your variables to avoid unexpected behavior.
   ```python
   def func():
       local_var = "I am local"

   print(local_var)  # NameError: name 'local_var' is not defined
   ```

5. **Commenting and Documentation**:
   - Use comments and docstrings to explain the purpose of variables, especially if their role is not immediately obvious.
   ```python
   total_items = 50  # Total number of items in stock
   ```

6. **Avoid Magic Numbers**:
   - Use named constants instead of hardcoding values.
   ```python
   TAX_RATE = 0.08
   total = subtotal * TAX_RATE
   ```

By following these practices, you can write clean, readable, and maintainable Python code. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Literals in Python](/Python/Articles/9_literals.md) 📜