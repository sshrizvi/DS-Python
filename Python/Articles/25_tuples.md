# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [List Comprehensions in Python](/Python/Articles/24_list_comprehensions.md) 📋

# Tuples in Python 📚

Tuples are an essential and versatile data structure in Python. They are similar to lists but with key differences that make them useful in various scenarios. This article delves into tuples, covering their definition, characteristics, creation, accessing items, modification, adding items, deletion, and operations.

## 1. Definition of Tuple 📝

A tuple is an ordered collection of items, which can be of different data types. Tuples are immutable, meaning that once they are created, their elements cannot be changed.

## 2. Characteristics of Tuples 🔍

- **Ordered**: The elements in a tuple have a defined order, and this order will not change.
- **Immutable**: Once a tuple is created, its elements cannot be modified. This immutability makes tuples hashable and allows them to be used as keys in dictionaries.
- **Heterogeneous**: A tuple can contain elements of different data types.
- **Allows Duplicates**: Tuples can contain duplicate elements.

## 3. Creation of Tuples 🛠️

### 1D Tuple

```python
# Creating a 1D tuple
tuple_1d = (1, 2, 3, 4)
print(tuple_1d)  # Output: (1, 2, 3, 4)
```

### 2D Tuple

```python
# Creating a 2D tuple
tuple_2d = ((1, 2), (3, 4))
print(tuple_2d)  # Output: ((1, 2), (3, 4))
```

### Single Item Tuple

```python
# Creating a single item tuple
single_item_tuple = (5,)
print(single_item_tuple)  # Output: (5,)
```

### Homogeneous Tuple

```python
# Creating a homogeneous tuple
homogeneous_tuple = (1, 2, 3, 4, 5)
print(homogeneous_tuple)  # Output: (1, 2, 3, 4, 5)
```

### Heterogeneous Tuple

```python
# Creating a heterogeneous tuple
heterogeneous_tuple = (1, "apple", 3.5, True)
print(heterogeneous_tuple)  # Output: (1, 'apple', 3.5, True)
```

### Type Conversion

```python
# Converting a list to a tuple
list_items = [1, 2, 3, 4]
tuple_from_list = tuple(list_items)
print(tuple_from_list)  # Output: (1, 2, 3, 4)
```

## 4. Accessing Items 🎯

Items in a tuple can be accessed using indexing and slicing.

### Indexing

```python
# Accessing items using indexing
tuple_1d = (1, 2, 3, 4)
print(tuple_1d[0])  # Output: 1
print(tuple_1d[-1])  # Output: 4
```

### Slicing

```python
# Accessing items using slicing
print(tuple_1d[1:3])  # Output: (2, 3)
print(tuple_1d[:2])  # Output: (1, 2)
print(tuple_1d[2:])  # Output: (3, 4)
```

## 5. Modification ❌

Tuples are immutable, so elements cannot be modified directly. However, you can create a new tuple by combining slices of the existing tuple with the new elements.

```python
# Trying to modify a tuple (this will raise an error)
tuple_1d[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Creating a new tuple with modified values
tuple_modified = (10,) + tuple_1d[1:]
print(tuple_modified)  # Output: (10, 2, 3, 4)
```

## 6. Adding Items ➕

Tuples cannot be modified directly to add items, but you can concatenate tuples to create a new tuple.

```python
# Adding an item by concatenation
new_tuple = tuple_1d + (5,)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
```

## 7. Deletion of Tuple and Its Items 🗑️

While individual items cannot be removed from a tuple due to its immutability, the entire tuple can be deleted.

```python
# Deleting a tuple
del tuple_1d
# print(tuple_1d)  # NameError: name 'tuple_1d' is not defined
```

## 8. Operations on Tuples 🔄

### Arithmetic Operations

Tuples do not support direct arithmetic operations like lists, but you can concatenate and repeat them.

```python
# Concatenation
tuple_1 = (1, 2)
tuple_2 = (3, 4)
tuple_concatenated = tuple_1 + tuple_2
print(tuple_concatenated)  # Output: (1, 2, 3, 4)

# Repetition
tuple_repeated = tuple_1 * 3
print(tuple_repeated)  # Output: (1, 2, 1, 2, 1, 2)
```

### Membership Operations

You can check if an item exists in a tuple using the `in` keyword.

```python
# Checking membership
print(3 in tuple_1)  # Output: False
print(2 in tuple_1)  # Output: True
```

### Looping Through a Tuple

You can use loops to iterate through the elements of a tuple.

```python
# Looping through a tuple
for item in tuple_1:
    print(item)
# Output:
# 1
# 2
```

### Tuple Unpacking

Tuples can be unpacked into individual variables.

```python
# Unpacking a tuple
a, b = tuple_1
print(a)  # Output: 1
print(b)  # Output: 2
```

### Advantages of Tuples

- **Immutability**: Tuples provide a guarantee that data cannot be modified, which can be useful for data integrity.
- **Performance**: Tuples are generally faster than lists due to their immutability.
- **Hashable**: Tuples can be used as keys in dictionaries and as elements of sets.

### Disadvantages of Tuples

- **Immutability**: While immutability can be an advantage, it also means that you cannot modify the contents of a tuple, which can be a limitation in some scenarios.
- **Lack of Methods**: Tuples do not have as many built-in methods as lists.

Understanding tuples and their operations is crucial for effectively using Python. Their immutability and efficiency make them a valuable tool for various programming tasks.

> [!TIP]  
> Link to Next Article  
> 🡺 [Methods of Tuples in Python](/Python/Articles/26_methods_of_tuples.md) 📜