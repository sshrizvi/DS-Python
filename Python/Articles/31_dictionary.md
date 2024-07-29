# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Frozen Sets](/Python/Articles/30_frozenset.md)

# Dictionaries in Python

## 1. Definition and Syntax

A dictionary in Python is an unordered collection of items. Each item is stored as a key-value pair. Dictionaries are optimized for retrieving values when the key is known.

**Syntax:**

```python
dictionary = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

Example:

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

## 2. Creation

### Empty Dictionary

```python
empty_dict = {}
```

### One-Dimensional Dictionary

```python
one_d_dict = {
    "name": "Alice",
    "age": 25
}
```

### Mixed Types

```python
mixed_dict = {
    "name": "Bob",
    "age": 22,
    "grades": [90, 85, 88]
}
```

### Two-Dimensional Dictionary

```python
two_d_dict = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}
```

### Using Sequence and `dict` Function

```python
seq_dict = dict([("name", "Eve"), ("age", 28)])
```

### Duplicate Keys

If duplicate keys are specified, the last occurrence will override the previous ones.

```python
dup_key_dict = {
    "name": "John",
    "name": "Doe"  # "Doe" will override "John"
}
```

### Mutable Items as Keys

Using mutable items (like lists) as keys is not allowed because they are unhashable.

```python
# Invalid: TypeError: unhashable type: 'list'
# invalid_dict = {[1, 2, 3]: "value"}
```

## 3. Accessing Items

### By Key

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

### Using `get()`

The `get()` method returns the value for the specified key if the key is in the dictionary.

```python
print(person.get("age"))  # Output: 25
print(person.get("city", "Not Found"))  # Output: Not Found
```

## 4. Adding New Key-Value Pair

```python
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

## 5. Removing Key-Value Pair

### Using `pop()`

Removes the item with the specified key and returns its value.

```python
age = person.pop("age")
print(age)  # Output: 25
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}
```

### Using `popitem()`

Removes the last inserted key-value pair.

```python
last_item = person.popitem()
print(last_item)  # Output: ('city', 'New York')
print(person)  # Output: {'name': 'Alice'}
```

### Using `del`

Deletes the item with the specified key.

```python
del person["name"]
print(person)  # Output: {}
```

### Using `clear()`

Empties the dictionary.

```python
person.clear()
print(person)  # Output: {}
```

## 6. Modifying Key-Value Pair

```python
person = {"name": "Alice", "age": 25}
person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26}
```

## 7. Operations

### Membership

Check if a key exists in the dictionary.

```python
print("name" in person)  # Output: True
print("city" in person)  # Output: False
```

### Iteration

#### Iterating Over Keys

```python
for key in person.keys():
    print(key)
# Output:
# name
# age
```

#### Iterating Over Values

```python
for value in person.values():
    print(value)
# Output:
# Alice
# 26
```

#### Iterating Over Key-Value Pairs

```python
for key, value in person.items():
    print(key, value)
# Output:
# name Alice
# age 26
```

### Practical Examples:

#### Creating Dictionaries:

```python
# Empty dictionary
empty_dict = {}

# 1D Dictionary
one_d_dict = {
    "name": "Alice",
    "age": 25
}

# Mixed types
mixed_dict = {
    "name": "Bob",
    "age": 22,
    "grades": [90, 85, 88]
}

# 2D Dictionary
two_d_dict = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}

# Using sequence and dict function
seq_dict = dict([("name", "Eve"), ("age", 28)])
```

#### Accessing Items:

```python
person = {"name": "Alice", "age": 25}

# By key
print(person["name"])  # Output: Alice

# Using get()
print(person.get("age"))  # Output: 25
print(person.get("city", "Not Found"))  # Output: Not Found
```

#### Adding, Removing, Modifying Items:

```python
person = {"name": "Alice", "age": 25}

# Adding
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Removing
age = person.pop("age")
print(age)  # Output: 25
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

last_item = person.popitem()
print(last_item)  # Output: ('city', 'New York')
print(person)  # Output: {'name': 'Alice'}

del person["name"]
print(person)  # Output: {}

person = {"name": "Alice", "age": 25}
person.clear()
print(person)  # Output: {}

# Modifying
person = {"name": "Alice", "age": 25}
person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26}
```

#### Operations:

```python
person = {"name": "Alice", "age": 25}

# Membership
print("name" in person)  # Output: True
print("city" in person)  # Output: False

# Iteration
for key in person.keys():
    print(key)
# Output:
# name
# age

for value in person.values():
    print(value)
# Output:
# Alice
# 26

for key, value in person.items():
    print(key, value)
# Output:
# name Alice
# age 26
```

In conclusion, dictionaries in Python are versatile and powerful collections for storing and retrieving data using key-value pairs. Understanding how to create, manipulate, and perform operations on dictionaries is essential for effective Python programming.

> [!TIP]  
> Link to Next Article  
> 🡺 [Dictionary Functions and Methods](/Python/Articles/32_dictionary_functions.md)