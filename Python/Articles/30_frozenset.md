# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Set Functions and Methods](/Python/Articles/29_set_functions.md)

# Frozen Sets

Frozen sets are a type of set in Python that are immutable. They provide a powerful tool for handling collections of unique elements in a way that ensures the elements cannot be changed. In this article, we will explore the definition, characteristics, comparison with regular sets, functions, and methods associated with frozen sets.

## Definition of Frozen Sets

A frozen set is an immutable version of a set in Python. Once a frozen set is created, its elements cannot be modified, added, or removed.

```python
frozenset([1, 2, 3])
```

## Characteristics of Frozen Sets

1. **Immutable**: Once created, the elements of a frozen set cannot be changed.
2. **Unordered**: Frozen sets do not maintain any specific order of elements.
3. **Unique Elements**: Just like regular sets, frozen sets do not allow duplicate elements.
4. **Hashable**: Since frozen sets are immutable, they can be used as keys in dictionaries or elements in other sets.

## Comparison with Sets

### Similarities

1. **Unique Elements**: Both sets and frozen sets ensure that all elements are unique.
2. **Unordered**: Both data structures do not maintain the order of elements.
3. **Set Operations**: Both can perform union, intersection, difference, and symmetric difference operations.

### Differences

1. **Mutability**: Regular sets are mutable, meaning their elements can be modified, added, or removed. Frozen sets are immutable and cannot be altered once created.
2. **Hashability**: Frozen sets can be used as dictionary keys or elements of another set because they are hashable. Regular sets cannot be used as dictionary keys or elements of other sets.

## Functions for Frozen Sets

Python provides a set of built-in functions that can be used with frozen sets. Here's a table listing these functions:

| Function            | Description                                                                | Example                                                     |
|---------------------|----------------------------------------------------------------------------|-------------------------------------------------------------|
| `len(frozenset)`    | Returns the number of elements in a frozen set.                            | `len(frozenset([1, 2, 3]))` → 3                             |
| `max(frozenset)`    | Returns the maximum value in a frozen set.                                 | `max(frozenset([1, 2, 3]))` → 3                             |
| `min(frozenset)`    | Returns the minimum value in a frozen set.                                 | `min(frozenset([1, 2, 3]))` → 1                             |
| `sum(frozenset)`    | Returns the sum of all elements in a frozen set.                           | `sum(frozenset([1, 2, 3]))` → 6                             |
| `sorted(frozenset)` | Returns a sorted list of the frozen set's elements.                        | `sorted(frozenset([3, 1, 2]))` → [1, 2, 3]                  |
| `all(frozenset)`    | Returns `True` if all elements in the frozen set are true (or if empty).   | `all(frozenset([1, 2, 3]))` → True                          |
| `any(frozenset)`    | Returns `True` if any element in the frozen set is true.                   | `any(frozenset([0, 0, 1]))` → True                          |
| `enumerate(frozenset)` | Returns an enumerate object containing pairs of index and element.     | `list(enumerate(frozenset([1, 2, 3])))` → [(0, 1), (1, 2), (2, 3)] |

## Methods for Frozen Sets

Frozen sets support a subset of the methods available for regular sets. Below is a table listing these methods:

| Method                    | Description                                                                      | Syntax                                 | Example                                                          |
|---------------------------|----------------------------------------------------------------------------------|----------------------------------------|------------------------------------------------------------------|
| `copy()`                  | Returns a shallow copy of the frozen set.                                        | `frozenset.copy()`                     | `fs = frozenset([1, 2, 3]); fs_copy = fs.copy(); print(fs_copy)` |
| `difference(*sets)`       | Returns a new set with elements in the frozen set that are not in the others.    | `frozenset.difference(*sets)`          | `fs = frozenset([1, 2, 3]); print(fs.difference([2, 3, 4]))`     |
| `intersection(*sets)`     | Returns a new set with elements common to the frozen set and all others.         | `frozenset.intersection(*sets)`        | `fs = frozenset([1, 2, 3]); print(fs.intersection([2, 3, 4]))`   |
| `union(*sets)`            | Returns a new set with elements from the frozen set and all others.              | `frozenset.union(*sets)`               | `fs = frozenset([1, 2, 3]); print(fs.union([3, 4, 5]))`          |
| `symmetric_difference(set)` | Returns a new set with elements in either the frozen set or other but not both.| `frozenset.symmetric_difference(set)`  | `fs = frozenset([1, 2, 3]); print(fs.symmetric_difference([2, 3, 4]))` |
| `issubset(set)`           | Returns `True` if the frozen set is a subset of another set.                     | `frozenset.issubset(set)`              | `fs = frozenset([1, 2]); print(fs.issubset([1, 2, 3]))`          |
| `issuperset(set)`         | Returns `True` if the frozen set is a superset of another set.                   | `frozenset.issuperset(set)`            | `fs = frozenset([1, 2, 3]); print(fs.issuperset([1, 2]))`        |
| `isdisjoint(set)`         | Returns `True` if the frozen set has no elements in common with another set.     | `frozenset.isdisjoint(set)`            | `fs = frozenset([1, 2, 3]); print(fs.isdisjoint([4, 5]))`        |

### Examples

#### Using `difference()`, `intersection()`, and `union()`

```python
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

difference_fs = fs1.difference(fs2)
print(difference_fs)  # Output: frozenset({1, 2})

intersection_fs = fs1.intersection(fs2)
print(intersection_fs)  # Output: frozenset({3})

union_fs = fs1.union(fs2)
print(union_fs)  # Output: frozenset({1, 2, 3, 4, 5})
```

#### Using `issubset()`, `issuperset()`, and `isdisjoint()`

```python
fs1 = frozenset([1, 2])
fs2 = frozenset([1, 2, 3])

print(fs1.issubset(fs2))  # Output: True
print(fs2.issuperset(fs1))  # Output: True
print(fs1.isdisjoint(frozenset([4, 5])))  # Output: True
```

## Conclusion

Frozen sets are an essential feature in Python for handling immutable collections of unique elements. They provide many of the benefits of regular sets, including the ability to perform various set operations, while ensuring that the elements cannot be modified. Understanding the functions and methods available for frozen sets allows developers to leverage their full potential in creating efficient and effective programs.

> [!TIP]  
> Link to Next Article  
> 🡺 [Dictionaries in Python](/Python/Articles/31_dictionary.md)