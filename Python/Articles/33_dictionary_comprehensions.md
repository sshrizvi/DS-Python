# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Dictionary Functions and Methods](/Python/Articles/32_dictionary_functions.md)

# Dictionary Comprehensions

## Introduction

Dictionary comprehensions provide a concise way to create dictionaries in Python. Similar to list comprehensions, they enable the creation and manipulation of dictionaries in a more readable and efficient manner. This article covers the syntax of dictionary comprehensions, presents five tricky examples, and discusses how they are similar to list comprehensions.

## Syntax of Dictionary Comprehensions

The basic syntax of a dictionary comprehension is:

```python
{key_expression: value_expression for item in iterable if condition}
```

- **key_expression**: Expression that generates the key for the new dictionary.
- **value_expression**: Expression that generates the value for the new dictionary.
- **item**: Variable representing the current item from the iterable.
- **iterable**: A sequence or collection that is being iterated over.
- **condition**: (Optional) A condition that filters which items are included in the new dictionary.

### Basic Example

```python
squares = {x: x*x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Tricky Examples

### 1. Dictionary of Even Numbers Squared

Create a dictionary of numbers and their squares, but only include even numbers.

```python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### 2. Inverting a Dictionary

Given a dictionary, create a new dictionary that inverts keys and values.

```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # Output: {1: 'a', 2: 'b', 3: 'c'}
```

### 3. Nested Dictionary Comprehension

Create a dictionary where keys are numbers and values are dictionaries of their multiplication table up to 5.

```python
multiplication_table = {x: {y: x*y for y in range(1, 6)} for x in range(1, 4)}
print(multiplication_table)
# Output:
# {
#   1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
#   2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
#   3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
# }
```

### 4. Filtering with Dictionary Comprehension

Create a dictionary from a list of words, but only include words with more than 3 characters.

```python
words = ["apple", "bat", "car", "dog", "elephant"]
filtered_words = {word: len(word) for word in words if len(word) > 3}
print(filtered_words)  # Output: {'apple': 5, 'elephant': 8}
```

### 5. Combining Two Lists into a Dictionary

Given two lists, create a dictionary by zipping them together.

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
combined = {k: v for k, v in zip(keys, values)}
print(combined)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

## Similarities to List Comprehensions

Dictionary comprehensions are similar to list comprehensions in the following ways:

1. **Syntax**: Both comprehensions use a similar syntax. For lists, the syntax is `[expression for item in iterable if condition]`. For dictionaries, it is `{key_expression: value_expression for item in iterable if condition}`.
  
2. **Readability and Conciseness**: Both comprehensions provide a way to create collections in a readable and concise manner, making the code easier to understand and maintain.
  
3. **Conditional Logic**: Both comprehensions can include optional conditions to filter elements based on specific criteria.

### Example Comparison

**List Comprehension:**

```python
squares = [x*x for x in range(6)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25]
```

**Dictionary Comprehension:**

```python
squares_dict = {x: x*x for x in range(6)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Conclusion

Dictionary comprehensions are a powerful feature in Python, enabling developers to create and manipulate dictionaries with a clean and concise syntax. Understanding how to use dictionary comprehensions effectively can lead to more readable and efficient code. By practicing with tricky examples, you can master this feature and apply it to a wide range of programming scenarios.


> [!IMPORTANT]  
> If you have studied Article 25-33, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 5](/Python/Tasks/task_5.ipynb)


> [!TIP]  
> Link to Next Article  
> 🡺 [Functions in Python](/Python/Articles/34_functions.md)