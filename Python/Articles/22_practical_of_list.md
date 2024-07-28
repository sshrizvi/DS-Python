# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Lists in Python](/Python/Articles/21_lists.md) 📝

# Practical Use of Lists in Python 🛠️

Lists are one of the most versatile and commonly used data structures in Python. This article explores various practical aspects of working with lists.

## 1. Creating a List 🛠️

### 1D List
A one-dimensional list is a simple list of elements.
```python
one_d_list = [1, 2, 3, 4, 5]
```

### 2D List
A two-dimensional list is a list of lists.
```python
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 3D List
A three-dimensional list is a list of lists of lists.
```python
three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
```

### Heterogeneous List
A heterogeneous list contains elements of different types.
```python
heterogeneous_list = [1, "apple", 3.14, True, [2, 4, 6]]
```

### List Using Type Conversion
Lists can be created from other iterable types using type conversion.
```python
string = "hello"
string_list = list(string)  # ['h', 'e', 'l', 'l', 'o']

tuple = (1, 2, 3)
tuple_list = list(tuple)  # [1, 2, 3]
```

## 2. Accessing Elements from the List 🎯

### Indexing
Elements in a list can be accessed using their index.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry (negative index)
```

### Slicing
A subset of the list can be accessed using slicing.
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[:3])  # Output: [1, 2, 3]
print(numbers[2:])  # Output: [3, 4, 5]
print(numbers[::2])  # Output: [1, 3, 5] (step of 2)
```

## 3. Adding Items to a List ➕

### append()
Adds a single element to the end of the list.
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### extend()
Adds elements from another list to the end of the list.
```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

### insert()
Inserts an element at a specified index.
```python
fruits = ["apple", "banana"]
fruits.insert(1, "cherry")
print(fruits)  # Output: ['apple', 'cherry', 'banana']
```

## 4. Modifying Lists ✏️

Lists can be modified by changing elements at specific indices.
```python
numbers = [1, 2, 3, 4, 5]
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]
```

## 5. Deleting Items ❌

### del
Deletes an element at a specified index.
```python
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry']
```

### remove()
Removes the first occurrence of a specified value.
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
```

### pop()
Removes and returns the element at a specified index. If no index is specified, it removes the last element.
```python
fruits = ["apple", "banana", "cherry"]
popped_fruit = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print(popped_fruit)  # Output: banana
```

### clear()
Removes all elements from the list.
```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
```

## 6. Operations on Lists ⚙️

### Arithmetic Operations
Concatenation and repetition can be performed on lists.
```python
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
print(list1 * 2)  # Output: [1, 2, 1, 2]
```

### Membership Operators
Check for the presence of an element.
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" not in fruits)  # Output: True
```

### Loop
Iterating through elements of a list.
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## 7. Traverse a List 🛤️

Traversing a list involves visiting each element.
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

## 8. zip() Function 🔄

The `zip()` function combines elements from multiple iterables (like lists) into tuples.
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

combined = list(zip(names, scores))
print(combined)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
```

Understanding the practical uses of lists in Python is crucial for efficient programming. Lists offer a robust and flexible way to store and manipulate data, making them an essential tool in any Python programmer's toolkit.

> [!TIP]  
> Link to Next Article  
> 🡺 [List Methods in Python](/Python/Articles/23_list_methods.md) 🛠️