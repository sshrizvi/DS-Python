# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [List V/S Tuple](/Python/Articles/27_lists_vs_tuples.md)

# Sets in Python

Sets are a fundamental data structure in Python that provide a unique way to handle collections of data. In this article, we will explore the characteristics, creation, access, modification, and operations of sets in Python.

## Characteristics of Sets 📜

1. **Unordered**: Sets do not maintain any order of elements.
2. **Mutable**: Elements can be added or removed.
3. **No Duplicate Elements**: Sets automatically eliminate duplicate entries.
4. **Iterable**: You can iterate over the elements in a set.
5. **Heterogeneous**: Sets can contain elements of different data types.
6. **Hashable Elements**: Elements in a set must be immutable (e.g., numbers, strings, tuples).

## Creation of Sets 🔨

Sets can be created in multiple ways:

### 1. Using Curly Braces `{}`

```python
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}
```

### 2. Using the `set()` Constructor

#### From an Iterable

```python
my_set = set([1, 2, 3])
print(my_set)  # Output: {1, 2, 3}
```

#### Creating an Empty Set

```python
empty_set = set()
print(empty_set)  # Output: set()
```

## Accessing Items 🔍

Since sets are unordered, you cannot access items using an index. Instead, you can check for the presence of an item using the `in` keyword.

```python
my_set = {1, 2, 3}
print(1 in my_set)  # Output: True
print(4 in my_set)  # Output: False
```

## Modifying Items ✏️

You cannot directly modify an item in a set, but you can add or remove items.

## Adding Items to a Set ➕

### Using `add()`

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

### Using `update()` to Add Multiple Items

```python
my_set = {1, 2, 3}
my_set.update([4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

## Deleting Items ❌

### Using `remove()`

Raises a `KeyError` if the item is not found.

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
# my_set.remove(4)  # Raises KeyError
```

### Using `discard()`

Does not raise an error if the item is not found.

```python
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # No error raised
```

### Using `pop()`

Removes and returns an arbitrary element. Raises `KeyError` if the set is empty.

```python
my_set = {1, 2, 3}
item = my_set.pop()
print(item)  # Output: 1 (or any other item)
print(my_set)  # Output: {2, 3}
```

### Using `clear()`

Removes all elements from the set.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
```

## Set Operations 🔄

### Union `|`

Combines elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### Intersection `&`

Returns elements common to both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
```

### Difference `-`

Returns elements in the first set but not in the second.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
```

### Symmetric Difference `^`

Returns elements in either set, but not in both.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

### Membership

Check if an item is in a set.

```python
my_set = {1, 2, 3}
print(1 in my_set)  # Output: True
print(4 in my_set)  # Output: False
```

### Loop

Iterate over elements in a set.

```python
my_set = {1, 2, 3}
for item in my_set:
    print(item)
# Output:
# 1
# 2
# 3
```

## Conclusion 📚

Sets in Python are a powerful and versatile data structure, useful for storing unique elements and performing various mathematical set operations. Their key characteristics, such as being unordered, mutable, and having no duplicate elements, make them ideal for specific use cases. Understanding how to create, access, modify, and perform operations on sets is essential for effective programming in Python.

> [!TIP]  
> Link to Next Article  
> 🡺 [Set Functions and Methods](/Python/Articles/29_set_functions.md)