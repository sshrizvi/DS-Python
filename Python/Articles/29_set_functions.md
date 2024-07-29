# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Sets in Python](/Python/Articles/28_sets.md)

# Set Functions and Methods

Sets in Python are powerful data structures that come with a wide range of built-in functions and methods to facilitate various operations. In this article, we will explore these functions and methods, providing detailed descriptions and examples for each.

## Set Functions

Python provides a set of built-in functions that work with sets. Here’s a table listing these functions:

| Function            | Description                                                                | Example                                                     |
|:---------------------:|:----------------------------------------------------------------------------:|:-------------------------------------------------------------:|
| `len(set)`          | Returns the number of elements in a set.                                   | `len({1, 2, 3})` → 3                                        |
| `max(set)`          | Returns the maximum value in a set.                                        | `max({1, 2, 3})` → 3                                        |
| `min(set)`          | Returns the minimum value in a set.                                        | `min({1, 2, 3})` → 1                                        |
| `sum(set)`          | Returns the sum of all elements in a set.                                  | `sum({1, 2, 3})` → 6                                        |
| `sorted(set)`       | Returns a sorted list of the set's elements.                               | `sorted({3, 1, 2})` → [1, 2, 3]                             |
| `all(set)`          | Returns `True` if all elements in the set are true (or if the set is empty)| `all({1, 2, 3})` → True                                     |
| `any(set)`          | Returns `True` if any element in the set is true                           | `any({0, 0, 1})` → True                                     |
| `enumerate(set)`    | Returns an enumerate object containing pairs of index and element          | `list(enumerate({1, 2, 3}))` → [(0, 1), (1, 2), (2, 3)]     |
| `frozenset(iterable)`| Returns an immutable frozenset containing elements from the given iterable| `frozenset([1, 2, 3])` → frozenset({1, 2, 3})               |

## Set Methods

Sets also come with a variety of methods that allow you to manipulate and perform operations on them. Below is a table listing these methods:

| Method                | Description                                                                       | Syntax                      | Example                                                 |
|:-----------------------:|:-----------------------------------------------------------------------------------:|:-----------------------------:|:---------------------------------------------------------:|
| `add(elem)`           | Adds an element to the set.                                                       | `set.add(elem)`             | `s = {1, 2}; s.add(3); print(s)` → {1, 2, 3}            |
| `remove(elem)`        | Removes an element from the set. Raises a `KeyError` if the element is not found.  | `set.remove(elem)`          | `s = {1, 2, 3}; s.remove(2); print(s)` → {1, 3}         |
| `discard(elem)`       | Removes an element from the set if it is a member. Does nothing if the element is not found. | `set.discard(elem)` | `s = {1, 2, 3}; s.discard(4); print(s)` → {1, 2, 3}     |
| `pop()`               | Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty. | `set.pop()`                 | `s = {1, 2, 3}; elem = s.pop(); print(elem)` → 1 (or 2 or 3) |
| `clear()`             | Removes all elements from the set.                                                | `set.clear()`               | `s = {1, 2, 3}; s.clear(); print(s)` → set()            |
| `copy()`              | Returns a shallow copy of the set.                                                | `set.copy()`                | `s = {1, 2, 3}; scopy = s.copy(); print(scopy)` → {1, 2, 3} |
| `update(iterable)`    | Updates the set, adding elements from all given iterables.                        | `set.update(iterable)`      | `s = {1}; s.update([2, 3]); print(s)` → {1, 2, 3}       |
| `union(*sets)`        | Returns a new set with elements from the set and all others.                      | `set.union(*sets)`          | `s = {1, 2}; print(s.union({2, 3}))` → {1, 2, 3}        |
| `intersection(*sets)` | Returns a new set with elements common to the set and all others.                 | `set.intersection(*sets)`   | `s = {1, 2, 3}; print(s.intersection({2, 3, 4}))` → {2, 3} |
| `difference(*sets)`   | Returns a new set with elements in the set that are not in the others.            | `set.difference(*sets)`     | `s = {1, 2, 3}; print(s.difference({2, 3, 4}))` → {1}   |
| `symmetric_difference(set)` | Returns a new set with elements in either the set or other but not both.    | `set.symmetric_difference(set)` | `s = {1, 2, 3}; print(s.symmetric_difference({2, 3, 4}))` → {1, 4} |
| `issubset(set)`       | Returns `True` if the set is a subset of another set.                             | `set.issubset(set)`         | `s = {1, 2}; print(s.issubset({1, 2, 3}))` → True       |
| `issuperset(set)`     | Returns `True` if the set is a superset of another set.                           | `set.issuperset(set)`       | `s = {1, 2, 3}; print(s.issuperset({1, 2}))` → True     |
| `isdisjoint(set)`     | Returns `True` if the set has no elements in common with another set.             | `set.isdisjoint(set)`       | `s = {1, 2, 3}; print(s.isdisjoint({4, 5}))` → True     |

## Examples

### Using `add()`, `remove()`, and `discard()`

```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

s.remove(3)
print(s)  # Output: {1, 2, 4}

s.discard(2)
print(s)  # Output: {1, 4}
```

### Using `union()`, `intersection()`, and `difference()`

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

union_set = s1.union(s2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = s1.intersection(s2)
print(intersection_set)  # Output: {3}

difference_set = s1.difference(s2)
print(difference_set)  # Output: {1, 2}
```

### Using `issubset()`, `issuperset()`, and `isdisjoint()`

```python
s1 = {1, 2}
s2 = {1, 2, 3}

print(s1.issubset(s2))  # Output: True
print(s2.issuperset(s1))  # Output: True
print(s1.isdisjoint({4, 5}))  # Output: True
```

## Conclusion 📚

Sets in Python are versatile and come with a range of functions and methods to perform various operations. Understanding these functions and methods allows for efficient and effective manipulation of set data. Whether you're checking for membership, performing mathematical operations, or simply iterating over elements, sets provide a robust tool for handling unique collections of data.

> [!TIP]  
> Link to Next Article  
> 🡺 [Frozen Sets](/Python/Articles/30_frozenset.md)