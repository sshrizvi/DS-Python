# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Python is a Dynamically Typed Language](/Python/Articles/4_dynamic_typing.md) ⚡

## Comments in Python 💬

Comments are an essential part of programming, allowing you to include explanations or notes within your code. They are *ignored by the Python interpreter* and do not affect the execution of the program.

### Types of Comments in Python:

1. **Single-Line Comments**:
   - Single-line comments start with a hash symbol (`#`) and extend to the end of the line.
   - **Usage**: To add short notes or explanations about the code.
   ```python
   # This is a single-line comment
   x = 10  # This comment is next to a statement
   ```

2. **Multi-Line Comments**:
   - Python does not have a specific syntax for multi-line comments like some other languages. However, you can use consecutive single-line comments or a multi-line string (triple quotes) to achieve the same effect.
   - **Usage**: To comment out multiple lines of code or to provide more detailed explanations.
   
   **Using Consecutive Single-Line Comments**:
   ```python
   # This is a multi-line comment
   # using consecutive single-line comments
   # to describe what the following code does.
   x = 10
   y = 20
   result = x + y
   ```

   **Using Multi-Line String**:
   ```python
   """
   This is a multi-line comment using a multi-line string.
   It's not technically a comment, but it works the same way
   if not assigned to any variable or used in a function.
   """
   x = 10
   y = 20
   result = x + y
   ```

### Special Uses of Comments:

1. **Disabling Code**:
   - Comments can be used to temporarily disable parts of your code without deleting them.
   ```python
   x = 10
   # y = 20
   result = x  # + y
   print(result)  # Output will be 10
   ```

2. **Documentation Strings (Docstrings)**:
   - Docstrings are special multi-line strings used to document modules, classes, functions, and methods. They are written inside triple quotes (`""" ... """`) and can span multiple lines.
   - **Usage**: To provide detailed descriptions and documentation for your code elements.
   ```python
   def add_numbers(a, b):
       """
       Add two numbers and return the result.

       Parameters:
       a (int): The first number
       b (int): The second number

       Returns:
       int: The sum of the two numbers
       """
       return a + b
   ```

3. **Inline Comments**:
   - Inline comments are placed on the same line as a statement, after the code.
   - **Usage**: To provide brief explanations of specific parts of a line of code.
   ```python
   x = 10  # Assign 10 to x
   y = x * 2  # Multiply x by 2 and assign the result to y
   ```

### Tips for Effective Commenting:

1. **Be Clear and Concise**: Write comments that are easy to understand. Avoid unnecessary comments that state the obvious.
   ```python
   x = 10  # Set x to 10  (Good)
   x = 10  # Assign the value of 10 to the variable x (Too verbose)
   ```

2. **Update Comments**: Ensure comments are kept up to date with the code. Outdated comments can be misleading.
   ```python
   # Calculate the sum of two numbers (Ensure this matches the code logic)
   result = x + y
   ```

3. **Use Comments to Explain Why, Not What**: The code should be self-explanatory about what it does. Use comments to explain why you are doing something a particular way.
   ```python
   # Use a binary search for faster lookup in a sorted list
   ```

4. **Avoid Redundancy**: Don't over-comment trivial code. Focus on explaining complex logic and decisions.
   ```python
   x = 10  # Initialize x with 10 (Unnecessary comment)
   ```

5. **Consistent Style**: Follow a consistent commenting style throughout your codebase for better readability.

Comments are a powerful tool for making your code more understandable and maintainable. Use them wisely to communicate the intent and logic behind your code. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Taking Inputs in Python](/Python/Articles/6_taking_inputs_in_python.md) 🖥️