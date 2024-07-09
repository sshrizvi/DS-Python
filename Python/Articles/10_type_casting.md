# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Literals in Python](/Python/Articles/9_literals.md) 📜

## Type Casting in Python 🔄

Type casting, or type conversion, is the process of converting a value from one data type to another. Python supports both implicit and explicit type conversion.

### Implicit Type Conversion (Coercion)

Implicit type conversion is performed automatically by Python when it encounters two different data types in an operation. Python promotes one data type to another to avoid data loss.

**Example:**

```python
# Implicit type conversion from int to float
x = 10      # int
y = 3.14    # float

result = x + y  # x is converted to float implicitly
print(result)   # Output: 13.14
print(type(result))  # Output: <class 'float'>
```

In the above example, the integer `x` is automatically converted to a float before the addition operation, ensuring the result is a float.

### Explicit Type Conversion (Type Casting)

Explicit type conversion is when the programmer manually converts one data type to another using built-in functions like `int()`, `float()`, `str()`, etc.

**Example:**

```python
# Explicit type conversion from float to int
x = 3.14  # float
y = int(x)  # manually converting float to int

print(y)  # Output: 3
print(type(y))  # Output: <class 'int'>
```

In this example, the float `x` is manually converted to an integer using the `int()` function.

### Differences Between Implicit and Explicit Type Conversion

| Feature                     | Implicit Type Conversion                             | Explicit Type Conversion              |
|:-----------------------------:|:------------------------------------------------------:|:---------------------------------------:|
| **Automatic Conversion**    | Performed automatically by Python                    | Manually performed by the programmer  |
| **Data Loss**               | Generally avoids data loss by promoting to a higher type | May cause data loss (e.g., float to int) |
| **Readability**             | Increases readability since it's implicit            | Clear and explicit, but can be verbose|
| **Control**                 | Less control over the conversion process             | Complete control over the conversion  |
| **Common Use Cases**        | Mixed-type arithmetic operations                     | Parsing user input, converting data types for specific operations |

### Important Points for Learners:

1. **Avoid Unintended Conversions**:
   - Be cautious of implicit conversions that may lead to unexpected results.
   ```python
   x = 1
   y = "2"
   result = x + y  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
   ```

2. **Precision and Rounding**:
   - Converting from float to int will truncate the decimal part, potentially leading to precision loss.
   ```python
   x = 5.99
   y = int(x)
   print(y)  # Output: 5
   ```

3. **String Conversion**:
   - Strings can be converted to numbers if they contain numeric values, and vice versa.
   ```python
   num_str = "123"
   num = int(num_str)
   print(num)  # Output: 123
   print(type(num))  # Output: <class 'int'>

   num = 456
   num_str = str(num)
   print(num_str)  # Output: '456'
   print(type(num_str))  # Output: <class 'str'>
   ```

4. **Complex Conversions**:
   - Converting complex numbers to floats or ints will raise an error.
   ```python
   z = 1 + 2j
   # float(z)  # TypeError: can't convert complex to float
   # int(z)    # TypeError: can't convert complex to int
   ```

5. **Boolean Conversions**:
   - Booleans can be converted to integers (`True` becomes `1`, `False` becomes `0`), and vice versa.
   ```python
   truth = True
   num = int(truth)
   print(num)  # Output: 1

   num = 0
   truth = bool(num)
   print(truth)  # Output: False
   ```

Understanding type casting is crucial for writing robust and error-free Python code. It helps you control how data is handled and ensures that operations are performed as expected. 😊

> [!IMPORTANT]  
> If you have studied all the nine articles, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 1](/Python/Tasks/task_1.ipynb)

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->