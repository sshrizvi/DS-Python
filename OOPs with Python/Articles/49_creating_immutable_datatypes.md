# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Pass by Value and Pass by Reference in Python](/OOPs%20with%20Python/Articles/48_pass_by_value_and_reference.md)

### Making User-Defined Classes Immutable in Python

In Python, user-defined classes are mutable by default. This means that instances of these classes can be modified after they are created, allowing attributes to be changed, added, or removed. However, in certain cases, it is desirable to make a class immutable to ensure that once an instance is created, its state cannot be altered.

#### **Understanding Mutability in Python**

Before diving into how to make a class immutable, it's essential to understand what mutability means:

- **Mutable Objects:** These are objects whose state can be changed after they are created. Lists, dictionaries, and sets are examples of mutable objects in Python.
  
- **Immutable Objects:** These are objects whose state cannot be changed after they are created. Tuples, strings, and integers are examples of immutable objects in Python.

By default, user-defined classes fall into the mutable category. However, Python provides mechanisms to enforce immutability on such classes.

### **Why Make a Class Immutable?**

There are several reasons why you might want to make a class immutable:

1. **Thread Safety:** Immutable objects are inherently thread-safe since their state cannot be changed after creation, avoiding potential race conditions.
  
2. **Simplified Reasoning:** With immutable objects, you don't have to worry about changes in state, making it easier to understand and reason about your code.
  
3. **Hashability:** Immutable objects can be made hashable (by implementing the `__hash__` method), allowing them to be used as keys in dictionaries or elements in sets.

### **Making a Class Immutable**

To make a class immutable in Python, follow these steps:

1. **Override `__setattr__` and `__delattr__`:** By overriding these special methods, you can prevent the modification or deletion of attributes after the object is created.

2. **Use `__slots__`:** This feature restricts the attributes that can be added to the class, which helps in controlling the state of the object.

3. **Use Frozen Data Classes:** Python's `dataclasses` module offers a `frozen=True` parameter that makes the class immutable automatically.

### **Example 1: Basic Immutable Class**

Let's create a basic immutable class:

```python
class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)
    
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify an immutable object")

    def __delattr__(self, name):
        raise AttributeError("Cannot delete attribute of an immutable object")
```

**Explanation:**
- In this example, any attempt to modify or delete the attributes `x` or `y` will raise an `AttributeError`.

### **Example 2: Using `__slots__`**

Using `__slots__` can be combined with the previous approach to make the class more memory-efficient and control attribute access.

```python
class ImmutablePoint:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify an immutable object")

    def __delattr__(self, name):
        raise AttributeError("Cannot delete attribute of an immutable object")
```

**Explanation:**
- `__slots__` restricts the object to only having `x` and `y` attributes, preventing the addition of any other attributes.

### **Example 3: Using Frozen Data Classes**

If you are working with Python 3.7 or later, you can use the `dataclasses` module to create a frozen (immutable) class easily.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int
```

**Explanation:**
- The `frozen=True` parameter makes the class immutable by automatically disabling the ability to modify the attributes.

### **Tricky Example: Preventing Mutability Through References**

Even if a class is immutable, if it contains mutable objects (like lists or dictionaries), those objects can still be modified. Here’s how you can ensure that even mutable objects within an immutable class remain unchanged:

```python
class ImmutableWithMutable:
    def __init__(self, items):
        super().__setattr__('items', tuple(items))

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify an immutable object")

    def __delattr__(self, name):
        raise AttributeError("Cannot delete attribute of an immutable object")

# Example usage:
obj = ImmutableWithMutable([1, 2, 3])
print(obj.items)  # Output: (1, 2, 3)
# Attempt to modify:
obj.items[0] = 10  # Raises TypeError
```

**Explanation:**
- By converting the list to a tuple, we ensure that even the items cannot be modified.

### **Advantages of Immutable Classes**

1. **Safety and Security:** Immutable objects can't be accidentally or maliciously changed after creation.
2. **Easier Debugging:** Since the object's state cannot change, it reduces the complexity when debugging.
3. **Suitability for Hashing:** Immutable objects can be safely used as dictionary keys or set elements.

### **Conclusion**

Immutability in Python can be achieved with user-defined classes by carefully controlling attribute assignment and deletion. While Python's default behavior favors mutability, understanding how to create immutable objects is crucial for situations requiring safety, simplicity, and reliability.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is Encapsulation?](/OOPs%20with%20Python/Articles/50_encapsulation.md)