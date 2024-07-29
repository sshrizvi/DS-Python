# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Dictionaries in Python](/Python/Articles/31_dictionary.md)

# Dictionary Functions and Methods

In Python, dictionaries come with a variety of built-in functions and methods that facilitate different operations. These methods are powerful tools for managing and manipulating dictionary data. Below is a comprehensive list of dictionary functions and methods, organized in a table format for easy reference.

| Method Signature               | Syntax                                      | Description                                                                                     | Return Type       | Example                                                                                              |
|:--------------------------------:|:---------------------------------------------:|:-------------------------------------------------------------------------------------------------:|:-------------------:|:------------------------------------------------------------------------------------------------------:|
| `dict.clear()`                 | `dictionary.clear()`                        | Removes all elements from the dictionary.                                                       | `None`            | `person.clear()`  ➔ `person` becomes `{}`                                                            |
| `dict.copy()`                  | `new_dict = dictionary.copy()`              | Returns a shallow copy of the dictionary.                                                       | `dict`            | `new_person = person.copy()`                                                                         |
| `dict.fromkeys()`              | `dict.fromkeys(seq, value=None)`            | Creates a new dictionary with keys from `seq` and values set to `value`.                         | `dict`            | `new_dict = dict.fromkeys(['a', 'b', 'c'], 0)`  ➔ `{'a': 0, 'b': 0, 'c': 0}`                         |
| `dict.get()`                   | `dictionary.get(key, default=None)`         | Returns the value for the specified key if key is in the dictionary, else `default`.             | Value or `default`| `person.get('name', 'Unknown')`  ➔ `'Alice'`                                                         |
| `dict.items()`                 | `dictionary.items()`                        | Returns a view object that displays a list of dictionary's key-value tuple pairs.                | `dict_items`      | `person.items()`  ➔ `dict_items([('name', 'Alice'), ('age', 25)])`                                   |
| `dict.keys()`                  | `dictionary.keys()`                         | Returns a view object that displays a list of all the keys in the dictionary.                    | `dict_keys`       | `person.keys()`  ➔ `dict_keys(['name', 'age'])`                                                      |
| `dict.pop()`                   | `dictionary.pop(key, default=None)`         | Removes the specified key and returns the corresponding value. If key is not found, `default` is returned. | Value or `default`| `person.pop('age')`  ➔ `25`, `person` becomes `{'name': 'Alice'}`                                     |
| `dict.popitem()`               | `dictionary.popitem()`                      | Removes and returns the last inserted key-value pair as a tuple.                                 | `(key, value)`    | `person.popitem()`  ➔ `('age', 25)`, `person` becomes `{'name': 'Alice'}`                            |
| `dict.setdefault()`            | `dictionary.setdefault(key, default=None)`  | Returns the value of the specified key. If the key does not exist, insert the key with the `default` value. | Value or `default`| `person.setdefault('city', 'New York')`  ➔ `'New York'`, `person` becomes `{'name': 'Alice', 'age': 25, 'city': 'New York'}` |
| `dict.update()`                | `dictionary.update([other])`                | Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs. | `None`            | `person.update({'city': 'New York'})`  ➔ `person` becomes `{'name': 'Alice', 'age': 25, 'city': 'New York'}` |
| `dict.values()`                | `dictionary.values()`                       | Returns a view object that displays a list of all the values in the dictionary.                  | `dict_values`     | `person.values()`  ➔ `dict_values(['Alice', 25])`                                                    |

### Practical Examples:

#### Using `clear()`

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
person.clear()
print(person)  # Output: {}
```

#### Using `copy()`

```python
person = {"name": "Alice", "age": 25}
new_person = person.copy()
print(new_person)  # Output: {'name': 'Alice', 'age': 25}
```

#### Using `fromkeys()`

```python
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

#### Using `get()`

```python
person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice
print(person.get("city", "Not Found"))  # Output: Not Found
```

#### Using `items()`

```python
person = {"name": "Alice", "age": 25}
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])
```

#### Using `keys()`

```python
person = {"name": "Alice", "age": 25}
print(person.keys())  # Output: dict_keys(['name', 'age'])
```

#### Using `pop()`

```python
person = {"name": "Alice", "age": 25}
age = person.pop("age")
print(age)  # Output: 25
print(person)  # Output: {'name': 'Alice'}
```

#### Using `popitem()`

```python
person = {"name": "Alice", "age": 25}
last_item = person.popitem()
print(last_item)  # Output: ('age', 25)
print(person)  # Output: {'name': 'Alice'}
```

#### Using `setdefault()`

```python
person = {"name": "Alice", "age": 25}
city = person.setdefault("city", "New York")
print(city)  # Output: New York
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### Using `update()`

```python
person = {"name": "Alice", "age": 25}
person.update({"city": "New York"})
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### Using `values()`

```python
person = {"name": "Alice", "age": 25}
print(person.values())  # Output: dict_values(['Alice', 25])
```

By understanding and utilizing these dictionary functions and methods, you can efficiently manage and manipulate dictionary data in Python, leading to more effective and powerful programming solutions.

> [!TIP]  
> Link to Next Article  
> 🡺 [Dictionary Comprehensions](/Python/Articles/33_dictionary_comprehensions.md)