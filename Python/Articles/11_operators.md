# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Type Casting in Python](/Python/Articles/10_type_casting.md) 🔄

## Operators in Python 🔧

Operators in Python are special symbols used to perform operations on variables and values. They are essential in forming expressions and performing various computations. Let's explore the different types of operators in Python.

### 1. Arithmetic Operators 🔢

Arithmetic operators are used to perform common mathematical operations.

| Operator | Description        | Example         | Result       |
|:----------:|:--------------------:|:-----------------:|:--------------:|
| `+`      | Addition           | `a + b`         | Sum of `a` and `b` |
| `-`      | Subtraction        | `a - b`         | Difference of `a` and `b` |
| `*`      | Multiplication     | `a * b`         | Product of `a` and `b` |
| `/`      | Division           | `a / b`         | Quotient of `a` and `b` |
| `%`      | Modulus            | `a % b`         | Remainder of `a` divided by `b` |
| `**`     | Exponentiation     | `a ** b`        | `a` raised to the power of `b` |
| `//`     | Floor Division     | `a // b`        | Quotient of `a` divided by `b`, rounded down to the nearest whole number |

**Examples**:
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3
```

### 2. Relational (Comparison) Operators

Relational operators compare the values of two operands and return a Boolean value.

| Operator | Description      | Example         | Result |
|:----------:|:------------------:|:-----------------:|:--------:|
| `==`     | Equal            | `a == b`        | `True` if `a` is equal to `b`, else `False` |
| `!=`     | Not Equal        | `a != b`        | `True` if `a` is not equal to `b`, else `False` |
| `>`      | Greater than     | `a > b`         | `True` if `a` is greater than `b`, else `False` |
| `<`      | Less than        | `a < b`         | `True` if `a` is less than `b`, else `False` |
| `>=`     | Greater than or equal to | `a >= b` | `True` if `a` is greater than or equal to `b`, else `False` |
| `<=`     | Less than or equal to | `a <= b` | `True` if `a` is less than or equal to `b`, else `False` |

**Examples**:
```python
a = 10
b = 3

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
```

### 3. Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description      | Example         | Result |
|:----------:|:------------------:|:-----------------:|:--------:|
| `and`    | Logical AND      | `a and b`       | `True` if both `a` and `b` are `True`, else `False` |
| `or`     | Logical OR       | `a or b`        | `True` if either `a` or `b` is `True`, else `False` |
| `not`    | Logical NOT      | `not a`         | `True` if `a` is `False`, else `False` |

**Examples**:
```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

### 4. Bitwise Operators

Bitwise operators are used to perform bit-level operations on integer values.

| Operator | Description      | Example         | Result |
|:----------:|:------------------:|:-----------------:|:--------:|
| `&`      | Bitwise AND      | `a & b`         | Bitwise AND of `a` and `b` |
| `\|`      | Bitwise OR       | `a \| b`         | Bitwise OR of `a` and `b` |
| `^`      | Bitwise XOR      | `a ^ b`         | Bitwise XOR of `a` and `b` |
| `~`      | Bitwise NOT      | `~a`            | Bitwise NOT of `a` |
| `<<`     | Bitwise Left Shift | `a << b`     | `a` shifted left by `b` bits |
| `>>`     | Bitwise Right Shift | `a >> b`    | `a` shifted right by `b` bits |

**Examples**:
```python
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)   # 0  (0000 in binary)
print(a | b)   # 14 (1110 in binary)
print(a ^ b)   # 14 (1110 in binary)
print(~a)      # -11 (Two's complement: -(a+1))
print(a << 1)  # 20 (10100 in binary)
print(a >> 1)  # 5  (0101 in binary)
```

### 5. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Description                  | Example         | Result |
|:----------:|:------------------------------:|:-----------------:|:--------:|
| `=`      | Assign                       | `a = 5`         | Assigns value `5` to `a` |
| `+=`     | Add and assign               | `a += 5`        | `a = a + 5` |
| `-=`     | Subtract and assign          | `a -= 5`        | `a = a - 5` |
| `*=`     | Multiply and assign          | `a *= 5`        | `a = a * 5` |
| `/=`     | Divide and assign            | `a /= 5`        | `a = a / 5` |
| `%=`     | Modulus and assign           | `a %= 5`        | `a = a % 5` |
| `**=`    | Exponentiation and assign    | `a **= 5`       | `a = a ** 5` |
| `//=`    | Floor division and assign    | `a //= 5`       | `a = a // 5` |
| `&=`     | Bitwise AND and assign       | `a &= b`        | `a = a & b` |
| `\|=`     | Bitwise OR and assign        | `a \|= b`        | `a = a \| b` |
| `^=`     | Bitwise XOR and assign       | `a ^= b`        | `a = a ^ b` |
| `<<=`    | Bitwise left shift and assign| `a <<= b`       | `a = a << b` |
| `>>=`    | Bitwise right shift and assign| `a >>= b`      | `a = a >> b` |

**Examples**:
```python
a = 10

a += 5
print(a)  # 15

a -= 2
print(a)  # 13

a *= 2
print(a)  # 26

a /= 2
print(a)  # 13.0

a %= 3
print(a)  # 1.0

a **= 3
print(a)  # 1.0

a //= 2
print(a)  # 0.0
```

### 6. Membership Operators

Membership operators test for membership in a sequence, such as strings, lists, or tuples.

| Operator | Description                  | Example         | Result |
|:----------:|:------------------------------:|:-----------------:|:--------:|
| `in`     | Returns `True` if a sequence contains the specified value | `a in list`  | `True` if `a` is in `list`, else `False` |
| `not in` | Returns `True` if a sequence does not contain the specified value | `a not in list` | `True` if `a` is not in `list`, else `False` |

**Examples**:
```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)     # True
print("grape" not in fruits) # True
```

### Important Points for Learners 📘

1. **Division Behavior**:
   - In Python 3, the `/` operator performs true division (floating-point division), while `//` performs floor division.
   ```python
   print(7 / 2)   # 3.5
   print(7 // 2)  # 3
   ```

2. **Type Promotion**:
   - If you mix integers and floats in an arithmetic

 operation, the result will be promoted to a float.
   ```python
   result = 5 + 3.0
   print(result)  # Output: 8.0
   print(type(result))  # Output: <class 'float'>
   ```

3. **Zero Division Error**:
   - Dividing by zero using `/` or `//` will raise a `ZeroDivisionError`.
   ```python
   try:
       result = 5 / 0
   except ZeroDivisionError:
       print("Division by zero is not allowed.")  # Output: Division by zero is not allowed.
   ```

4. **Negative Modulus**:
   - The result of the modulus operation with negative numbers can be surprising.
   ```python
   print(10 % 3)  # Output: 1
   print(-10 % 3) # Output: 2
   ```

5. **Short-Circuit Evaluation**:
   - Logical operators `and` and `or` use short-circuit evaluation.
   ```python
   a = True
   b = False
   print(a or b)   # True (doesn't evaluate b)
   print(a and b)  # False (evaluates b)
   ```

Understanding these operators and their nuances is crucial for effective programming in Python. 😊

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->