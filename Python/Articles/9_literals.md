# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Variables in Python](/Python/Articles/8_variables.md) 📝

## Literals in Python 📜

Literals in Python are raw data that represent fixed values. They are the most fundamental part of the Python programming language and can be assigned to variables or used in expressions. There are several types of literals in Python, each representing different kinds of data.

### Types of Literals in Python:

1. **Numeric Literals**:
   - Represent numbers and are divided into three types: integers, floats, and complex numbers.
   
   **Integers**:
   ```python
   x = 10      # Decimal
   y = 0b1010  # Binary
   z = 0o12    # Octal
   w = 0xA     # Hexadecimal
   ```

   **Floats**:
   ```python
   pi = 3.14
   scientific = 1.5e2  # 1.5 * 10^2
   ```

   **Complex Numbers**:
   ```python
   complex_num = 3 + 4j
   ```

2. **String Literals**:
   - Represent sequences of characters and are enclosed in single quotes (`'`), double quotes (`"`), triple single quotes (`'''`), or triple double quotes (`"""`).
   ```python
   single_quote_str = 'Hello'
   double_quote_str = "World"
   triple_single_quote_str = '''This is a
   multi-line string.'''
   triple_double_quote_str = """This is also
   a multi-line string."""
   ```

3. **Boolean Literals**:
   - Represent truth values and can be either `True` or `False`.
   ```python
   is_valid = True
   is_empty = False
   ```

4. **Special Literal `None`**:
   - Represents the absence of a value or a null value.
   ```python
   result = None
   ```

5. **Collection Literals**:
   - Represent collections of values and include lists, tuples, sets, and dictionaries.

   **List Literals**:
   ```python
   fruits = ["apple", "banana", "cherry"]
   ```

   **Tuple Literals**:
   ```python
   coordinates = (10, 20)
   ```

   **Set Literals**:
   ```python
   unique_numbers = {1, 2, 3, 4, 5}
   ```

   **Dictionary Literals**:
   ```python
   person = {"name": "John", "age": 30}
   ```

### Important Points for Learners:

1. **Immutable Nature of Some Literals**:
   - String and tuple literals are immutable, meaning their values cannot be changed after they are created.
   ```python
   name = "John"
   name[0] = "j"  # TypeError: 'str' object does not support item assignment
   ```

2. **Use of Quotes in Strings**:
   - Single and double quotes can be used interchangeably for string literals. Triple quotes are used for multi-line strings.
   ```python
   quote = 'She said, "Hello!"'
   multi_line = """This is
   a multi-line
   string."""
   ```

3. **Escape Sequences in Strings**:
   - Special characters in strings can be represented using escape sequences.
   ```python
   newline = "Hello\nWorld"
   tab = "Hello\tWorld"
   backslash = "This is a backslash: \\"
   ```

4. **Boolean Context**:
   - Boolean literals can be used in conditions and control flow statements.
   ```python
   if is_valid:
       print("The value is valid.")
   ```

5. **Precision of Floats**:
   - Floating-point literals are approximations of real numbers and can have precision issues.
   ```python
   a = 0.1 + 0.2
   print(a)  # Output might be 0.30000000000000004
   ```

6. **None as a Default Value**:
   - The `None` literal is often used as a default value for optional parameters in functions.
   ```python
   def greet(name=None):
       if name is None:
           name = "Stranger"
       print(f"Hello, {name}")
   ```

7. **Mutable Collection Literals**:
   - List and dictionary literals are mutable, meaning their contents can be changed after they are created.
   ```python
   numbers = [1, 2, 3]
   numbers.append(4)

   person = {"name": "Alice"}
   person["age"] = 25
   ```

Understanding literals and how to use them effectively is crucial for writing clear and efficient Python code. 😊

> [!TIP]  
> Link to Next Article  
> 🡺 [Type Casting in Python](/Python/Articles/10_type_casting.md) 🔄