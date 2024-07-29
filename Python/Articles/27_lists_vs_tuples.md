# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Methods of Tuples in Python](/Python/Articles/26_methods_of_tuples.md) 📜

# List V/S Tuple

Python offers several ways to store data, among which lists and tuples are two of the most common. Both lists and tuples are ordered collections, but they have some distinct differences. This article will delve into the contrasts between lists and tuples, highlighting their unique characteristics, use cases, and providing example code for clarity.

## Definition

- **List**: A list is a mutable, ordered collection of items. Lists are defined by square brackets `[]`.
- **Tuple**: A tuple is an immutable, ordered collection of items. Tuples are defined by parentheses `()`.

## Key Differences

### 1. Mutability

- **Lists** are mutable, meaning their elements can be changed, added, or removed.
- **Tuples** are immutable, meaning once created, their elements cannot be changed.

**Example:**

```python
# List
list_example = [1, 2, 3]
list_example[0] = 4  # Allowed
print(list_example)  # Output: [4, 2, 3]

# Tuple
tuple_example = (1, 2, 3)
# tuple_example[0] = 4  # Raises TypeError
```

### 2. Syntax

- **Lists** use square brackets `[]`.
- **Tuples** use parentheses `()`.

**Example:**

```python
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
```

### 3. Performance

- **Lists** are slower than tuples when it comes to operations like iteration and access, because of their mutability.
- **Tuples** are faster than lists due to their immutability.

**Example:**

```python
import timeit

# List
list_time = timeit.timeit(stmt="[1, 2, 3]", number=1000000)
print(f"List creation time: {list_time}")

# Tuple
tuple_time = timeit.timeit(stmt="(1, 2, 3)", number=1000000)
print(f"Tuple creation time: {tuple_time}")
```

### 4. Use Cases

- **Lists** are used when the data is expected to change.
- **Tuples** are used when the data is constant and cannot change.

**Example:**

```python
# List for a dynamic collection
dynamic_collection = [1, 2, 3]
dynamic_collection.append(4)

# Tuple for a fixed collection
fixed_collection = (1, 2, 3)
```

### 5. Memory Usage

- **Lists** consume more memory due to their dynamic nature.
- **Tuples** consume less memory, being static.

**Example:**

```python
import sys

list_example = [1, 2, 3]
tuple_example = (1, 2, 3)

print(f"List size: {sys.getsizeof(list_example)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_example)} bytes")
```

### 6. Built-in Methods

- **Lists** have more built-in methods than tuples due to their mutability (e.g., `append()`, `remove()`, `pop()`).
- **Tuples** have fewer built-in methods (e.g., `count()`, `index()`).

**Example:**

```python
# List methods
list_example = [1, 2, 3]
list_example.append(4)  # [1, 2, 3, 4]
list_example.remove(2)  # [1, 3, 4]
print(list_example)

# Tuple methods
tuple_example = (1, 2, 3)
count = tuple_example.count(1)  # 1
index = tuple_example.index(2)  # 1
print(f"Count of 1 in tuple: {count}")
print(f"Index of 2 in tuple: {index}")
```

### 7. Slicing and Indexing

Both lists and tuples support slicing and indexing.

**Example:**

```python
# List
list_example = [1, 2, 3, 4, 5]
print(list_example[1:3])  # Output: [2, 3]
print(list_example[-1])   # Output: 5

# Tuple
tuple_example = (1, 2, 3, 4, 5)
print(tuple_example[1:3])  # Output: (2, 3)
print(tuple_example[-1])   # Output: 5
```

### 8. Immutability Implications

- **Lists** can be nested within other lists or tuples, and their contents can be changed.
- **Tuples** can be nested, but if a tuple contains a list, the list can be changed, even if the tuple itself cannot.

**Example:**

```python
# List in a list
nested_list = [[1, 2], [3, 4]]
nested_list[0][1] = 5  # Allowed
print(nested_list)  # Output: [[1, 5], [3, 4]]

# List in a tuple
nested_tuple = ([1, 2], [3, 4])
nested_tuple[0][1] = 5  # Allowed
print(nested_tuple)  # Output: ([1, 5], [3, 4])
```

### 9. Hashability

- **Lists** are not hashable and cannot be used as dictionary keys.
- **Tuples** are hashable (as long as they contain only hashable types) and can be used as dictionary keys.

**Example:**

```python
# Using a tuple as a dictionary key
dictionary = { (1, 2): "tuple key" }
print(dictionary[(1, 2)])  # Output: tuple key

# Using a list as a dictionary key (raises TypeError)
# dictionary = { [1, 2]: "list key" }  # Raises TypeError
```

## Summary

### Lists

- Mutable
- Slower performance
- More memory usage
- Dynamic data storage
- More built-in methods

### Tuples

- Immutable
- Faster performance
- Less memory usage
- Static data storage
- Fewer built-in methods

Understanding the differences between lists and tuples is crucial for selecting the appropriate data structure for your needs. While lists offer flexibility and a wide range of methods for dynamic operations, tuples provide efficiency and immutability for fixed collections of data.

> [!TIP]  
> Link to Next Article  
> 🡺 [Sets in Python](/Python/Articles/28_sets.md)