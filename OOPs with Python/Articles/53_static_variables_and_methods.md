# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [List and Dictionaries of Objects](/OOPs%20with%20Python/Articles/52_objects_are_elements.md)

### Static Variables

**Definition**: Static variables, also known as class variables, are variables that are shared among all instances of a class. They are defined within a class but outside any methods. Unlike instance variables, static variables have the same value for all instances of the class.

**Usage**: Static variables are useful when you want to maintain a value that should be consistent across all instances of a class. They are often used to store information that is common to all objects.

**Example**:
```python
class Employee:
    company_name = "Tech Corp"  # Static variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Accessing static variable
print(Employee.company_name)  # Output: Tech Corp

# Creating instances
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)

# Accessing static variable via instance
print(emp1.company_name)  # Output: Tech Corp
print(emp2.company_name)  # Output: Tech Corp
```

**Key Points**:
- Static variables are stored in the class itself, not in the objects.
- Changing the value of a static variable affects all instances of the class.

### Instance Variables

**Definition**: Instance variables are attributes or properties that are unique to each instance of a class. They are defined within a constructor or method using the `self` keyword.

**Usage**: Instance variables are used to store data that is specific to each object.

**Example**:
```python
class Employee:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Creating instances
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)

# Accessing instance variables
print(emp1.name)  # Output: Alice
print(emp2.name)  # Output: Bob
```

**Key Points**:
- Instance variables are stored in the object, not in the class.
- Each instance of a class can have different values for its instance variables.

### Static vs. Instance Variables

| **Feature**         | **Static Variables**                            | **Instance Variables**                        |
|---------------------|-------------------------------------------------|------------------------------------------------|
| **Scope**           | Shared among all instances                      | Specific to each instance                      |
| **Storage**         | Stored in the class                             | Stored in the object                           |
| **Access**          | Accessed using the class name or instance       | Accessed using the instance                    |
| **Modification**    | Affects all instances when modified             | Only affects the specific instance when modified |
| **Use Case**        | Common data across all instances                | Data unique to each instance                   |

**Example**:
```python
class Employee:
    company_name = "Tech Corp"  # Static variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Creating instances
emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)

# Modifying static variable
Employee.company_name = "New Tech Corp"

print(emp1.company_name)  # Output: New Tech Corp
print(emp2.company_name)  # Output: New Tech Corp

# Modifying instance variable
emp1.name = "Alicia"
print(emp1.name)  # Output: Alicia
print(emp2.name)  # Output: Bob
```

### Static Methods

**Definition**: Static methods are methods that belong to the class rather than any instance of the class. They do not have access to instance variables or `self`, and they are defined using the `@staticmethod` decorator.

**Usage**: Static methods are used when a function inside a class does not require access to instance-specific data or methods.

**Example**:
```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
print(MathOperations.add(5, 3))      # Output: 8
print(MathOperations.multiply(5, 3)) # Output: 15
```

**Key Points**:
- Static methods do not have access to the class or instance attributes.
- They can be called on the class itself or on instances.
- They are useful for utility functions that don't need to access or modify the class or instance state.

### Tricky Behavior and Warnings

- **Overriding Static Variables**: If you assign a static variable via an instance, Python creates a new instance variable with the same name, which can be confusing.
- **Accessing Static Methods**: Static methods can be called on the class or instance, but they don’t have access to `self` or `cls`.
- **Mutable Static Variables**: If a static variable is a mutable type (like a list), modifying it through an instance will affect all instances because they share the same reference.

These concepts are crucial for understanding how Python handles class and instance data, which is fundamental for writing effective and efficient code, especially in object-oriented programming.

> [!IMPORTANT]  
> If you have studied Article 46-53, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 8](/OOPs%20with%20Python/Tasks/task_8.ipynb)

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->