# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Functions and Methods in Python](/OOPs%20with%20Python/Articles/43_functions_vs_methods.md)

### What are Magic Methods in Python? (a.k.a DUNDER Methods)

**Magic methods**, also known as **DUNDER methods** (short for "Double UNDERscore"), are special methods in Python that are preceded and followed by double underscores, like `__init__`, `__str__`, `__add__`, etc. These methods are automatically invoked by Python to perform certain operations on objects, making it possible to customize the behavior of built-in operations for user-defined classes.

#### Key Characteristics of Magic Methods:
- **Automatically Invoked**: Magic methods are not called directly by the user; instead, they are triggered by certain built-in operations.
- **Customization**: They allow the customization of class behavior for operations like addition, comparison, string representation, etc.
- **Enhance Readability**: Magic methods can make user-defined classes behave like built-in types, making the code more intuitive and easier to read.

#### Common Magic Methods

1. **`__init__(self, ...)`**:
   - **Purpose**: This is the constructor method. It is called when an instance of a class is created.
   - **Example**:
     ```python
     class Dog:
         def __init__(self, name):
             self.name = name

     my_dog = Dog("Buddy")
     print(my_dog.name)  # Output: Buddy
     ```

2. **`__str__(self)`**:
   - **Purpose**: Defines the string representation of an object, which is what `print()` or `str()` outputs.
   - **Example**:
     ```python
     class Dog:
         def __init__(self, name):
             self.name = name

         def __str__(self):
             return f"Dog named {self.name}"

     my_dog = Dog("Buddy")
     print(my_dog)  # Output: Dog named Buddy
     ```

3. **`__repr__(self)`**:
   - **Purpose**: Defines the “official” string representation of an object, which can be used to recreate the object.
   - **Example**:
     ```python
     class Dog:
         def __init__(self, name):
             self.name = name

         def __repr__(self):
             return f"Dog('{self.name}')"

     my_dog = Dog("Buddy")
     print(repr(my_dog))  # Output: Dog('Buddy')
     ```

4. **`__add__(self, other)`**:
   - **Purpose**: Allows customization of the behavior of the `+` operator.
   - **Example**:
     ```python
     class Vector:
         def __init__(self, x, y):
             self.x = x
             self.y = y

         def __add__(self, other):
             return Vector(self.x + other.x, self.y + other.y)

         def __repr__(self):
             return f"Vector({self.x}, {self.y})"

     v1 = Vector(1, 2)
     v2 = Vector(3, 4)
     print(v1 + v2)  # Output: Vector(4, 6)
     ```

5. **`__len__(self)`**:
   - **Purpose**: Defines the behavior of the `len()` function when called on an object.
   - **Example**:
     ```python
     class MyList:
         def __init__(self, items):
             self.items = items

         def __len__(self):
             return len(self.items)

     my_list = MyList([1, 2, 3, 4])
     print(len(my_list))  # Output: 4
     ```

6. **`__getitem__(self, key)`**:
   - **Purpose**: Defines the behavior of accessing elements via indexing or slicing.
   - **Example**:
     ```python
     class MyList:
         def __init__(self, items):
             self.items = items

         def __getitem__(self, index):
             return self.items[index]

     my_list = MyList([1, 2, 3, 4])
     print(my_list[2])  # Output: 3
     ```

7. **`__call__(self, ...)`**:
   - **Purpose**: Allows an instance of a class to be called as if it were a function.
   - **Example**:
     ```python
     class Adder:
         def __init__(self, value):
             self.value = value

         def __call__(self, x):
             return self.value + x

     add_five = Adder(5)
     print(add_five(10))  # Output: 15
     ```

#### Why are Magic Methods Important?

Magic methods are crucial because they enable you to define how your objects behave with Python's built-in operations. This can make your classes behave more like built-in types, improving the readability and intuitiveness of your code.

**Key Points to Remember**:
- **Customization**: You can define custom behaviors for operators and built-in functions using magic methods.
- **Readability**: By overriding magic methods, you make your objects interact naturally with Python’s syntax, enhancing code readability.
- **Best Practices**: Use magic methods to extend the behavior of objects, but avoid overusing them as they can make the code harder to understand for those unfamiliar with the concept.

To list down all the magic (dunder) methods in Python, you can use Python's built-in `dir()` function on an empty class or object. This function returns a list of all attributes and methods associated with an object, including magic methods.

### Example to List All Magic Methods:
```python
# Using an empty class to list all magic methods
class EmptyClass:
    pass

# Listing all attributes and methods of the EmptyClass
all_methods = dir(EmptyClass)

# Filtering out magic methods (those that start and end with '__')
dunder_methods = [method for method in all_methods if method.startswith('__') and method.endswith('__')]

print(dunder_methods)
```

### Output:
This code will output a list of all the magic methods like:
```python
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

### Common Dunder Methods:
- **`__init__`**: Called when an instance is created (constructor).
- **`__str__`**: Returns a string representation of an object.
- **`__repr__`**: Returns an “official” string representation of an object.
- **`__add__`**: Defines behavior for the addition `+` operator.
- **`__getitem__`**: Called to retrieve an item by index.
- **`__setitem__`**: Called to set an item by index.
- **`__delitem__`**: Called to delete an item by index.
- **`__call__`**: Makes an object callable as a function.

### Exploring Further:
If you want to explore or understand the purpose of each magic method, you can look up each one individually in Python's documentation or specialized resources on Python magic methods. Here's a [link to Python’s data model documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names), which provides detailed explanations on these methods.

> [!TIP]  
> Link to Next Article  
> 🡺 [What are Class Diagrams?](/OOPs%20with%20Python/Articles/45_class_diagrams.md)