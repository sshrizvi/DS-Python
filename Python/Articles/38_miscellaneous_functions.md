# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Nested Functions](/Python/Articles/37_nested_functions.md)

# Some Useful Functions for Data Scientists

## Introduction

In Python, there are several built-in functions that are particularly useful for data scientists. These functions help to write clean, concise, and efficient code. Four such functions are `lambda`, `map`, `filter`, and `reduce`. In this article, we'll explore these functions in detail and provide examples of their usage.

## Lambda Functions

A `lambda` function is a small anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression. The expression is evaluated and returned.

### Syntax

```python
lambda arguments: expression
```

### Examples

1. **Basic Usage**

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

2. **Using with `map`**

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
```

3. **Sorting a List of Tuples**

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## Normal Function V/S Lambda Function

Here's a table that highlights the key differences between normal functions and lambda functions in Python:

| **Aspect**                 | **Normal Function**                          | **Lambda Function**                        |
|----------------------------|----------------------------------------------|--------------------------------------------|
| **Definition**             | Defined using the `def` keyword.             | Defined using the `lambda` keyword.        |
| **Syntax**                 | `def function_name(parameters):`             | `lambda parameters: expression`            |
| **Name**                   | Has a name (e.g., `function_name`).          | Anonymous (no name unless assigned).       |
| **Number of Expressions**  | Can contain multiple expressions.            | Contains a single expression.              |
| **Return Statement**       | Explicit `return` statement required.        | Implicitly returns the result of the expression. |
| **Readability**            | Generally more readable for complex logic.   | Concise but can be less readable for complex logic. |
| **Use Case**               | Suitable for defining reusable, named, and complex functions. | Suitable for small, simple operations, often used as arguments to higher-order functions like `map()`, `filter()`, and `reduce()`. |
| **Docstrings**             | Can include docstrings for documentation.    | Cannot include docstrings.                 |
| **Support for Statements** | Can include multiple statements, including loops and conditionals. | Cannot include statements; limited to a single expression. |
| **Example**                | ```python                                      def add(x, y):                              return x + y```                        | ```python lambda x, y: x + y```            |
| **Decorators**             | Can be decorated with function decorators.   | Cannot be decorated.                       |

This table captures the main differences between normal functions and lambda functions, helping you understand when and how to use each type of function effectively in Python.

## Map Function

The `map` function applies a given function to all items in an iterable (like a list) and returns a map object (which can be converted to a list, set, etc.).

### Syntax

```python
map(function, iterable)
```

### Examples

1. **Squaring Numbers**

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
```

2. **Converting Strings to Uppercase**

```python
words = ['apple', 'banana', 'cherry']
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY']
```

3. **Adding Two Lists Element-Wise**

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
summed_lists = list(map(lambda x, y: x + y, list1, list2))
print(summed_lists)  # Output: [5, 7, 9]
```

## Filter Function

The `filter` function constructs an iterator from elements of an iterable for which a function returns true.

### Syntax

```python
filter(function, iterable)
```

### Examples

1. **Filtering Even Numbers**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

2. **Filtering Words Longer than 3 Characters**

```python
words = ['cat', 'elephant', 'dog', 'fish']
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)  # Output: ['elephant', 'fish']
```

3. **Filtering Non-Empty Strings**

```python
strings = ['hello', '', 'world', '']
non_empty_strings = list(filter(lambda s: s != '', strings))
print(non_empty_strings)  # Output: ['hello', 'world']
```

## Reduce Function

The `reduce` function applies a rolling computation to sequential pairs of values in a list. It is part of the `functools` module.

### Syntax

```python
from functools import reduce
reduce(function, iterable)
```

### Examples

1. **Summing a List of Numbers**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 10
```

2. **Finding the Maximum Number**

```python
numbers = [3, 1, 4, 1, 5, 9]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # Output: 9
```

3. **Product of a List of Numbers**

```python
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

## Conclusion

Understanding and utilizing `lambda`, `map`, `filter`, and `reduce` functions can significantly enhance your efficiency as a data scientist. These functions support a more functional programming approach, allowing for concise and readable code. By mastering these tools, you can perform complex data manipulations with ease.

> [!IMPORTANT]  
> If you have studied Article 34-38, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 6](/Python/Tasks/task_6.ipynb)

> [!TIP]  
> Link to Next Article  
> 🡺 [Object-Oriented Programming (OOP)](../../OOPs%20with%20Python/Articles/39_intro_to_oops.md)