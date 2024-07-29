# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Tuples in Python](/Python/Articles/25_tuples.md) 📚

# Methods of Tuples in Python 📜

Tuples in Python are immutable sequences, which limits the number of methods available compared to lists. However, they do come with some useful methods that can help in various operations. This article provides a comprehensive guide to all the methods available for tuples, organized into a table with method signatures, syntax, descriptions, return types, and examples.

## Tuple Methods

The table below lists all the methods available for tuples in Python:

| Method Signature    | Syntax                          | Description                                                               | Return Type | Example |
|:---------------------:|:---------------------------------:|:---------------------------------------------------------------------------:|:-------------:|:---------:|
| `tuple.count(value)`| `t.count(value)`                | Counts the number of times a specified value appears in the tuple.         | `int`       | `t = (1, 2, 3, 1, 1); count = t.count(1)  # Output: 3` |
| `tuple.index(value, [start], [end])` | `t.index(value, [start], [end])` | Returns the index of the first occurrence of the specified value. Raises `ValueError` if the value is not found. Optional `start` and `end` arguments can specify a subrange to search within. | `int`       | `t = (1, 2, 3, 1, 1); index = t.index(3)  # Output: 2` |

### Descriptions and Examples of Tuple Methods 📘

### 1. `tuple.count(value)`

**Description**: This method counts the number of times a specified value appears in the tuple.

**Syntax**: 
```python
t.count(value)
```

**Return Type**: `int`

**Example**:
```python
t = (1, 2, 3, 1, 1)
count = t.count(1)
print(count)  # Output: 3
```

### 2. `tuple.index(value, [start], [end])`

**Description**: This method returns the index of the first occurrence of the specified value. If the value is not found, it raises a `ValueError`. The optional `start` and `end` arguments specify a subrange to search within.

**Syntax**: 
```python
t.index(value, [start], [end])
```

**Return Type**: `int`

**Example**:
```python
t = (1, 2, 3, 1, 1)
index = t.index(3)
print(index)  # Output: 2

# Using start and end arguments
index = t.index(1, 2)
print(index)  # Output: 3
```

## Important Points to Remember 🚀

1. **Immutability**: Tuples are immutable, meaning once created, their elements cannot be changed. This immutability results in fewer methods compared to lists.
2. **Efficiency**: Tuples can be more memory-efficient and faster than lists, especially when dealing with fixed-size data.
3. **Hashable**: Because tuples are immutable, they can be used as keys in dictionaries, whereas lists cannot.
4. **Usage**: Tuples are often used to store heterogeneous data, while lists are typically used for homogeneous data.

Understanding these methods and characteristics can significantly enhance your ability to work effectively with tuples in Python. Although tuples have fewer methods than lists, they are powerful in their specific use cases due to their immutability and efficiency.

> [!TIP]  
> Link to Next Article  
> 🡺 [List V/S Tuple](/Python/Articles/27_lists_vs_tuples.md)