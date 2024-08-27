# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is Encapsulation?](/OOPs%20with%20Python/Articles/50_encapsulation.md)

### List of Objects

In Python, a list of objects refers to a list where each element is an instance of a class. This is a powerful feature, as it allows you to store multiple objects, each potentially having its own attributes and methods, within a single list. Here's an example to illustrate this concept:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

# Creating a list of Student objects
students = [
    Student("Alice", 20),
    Student("Bob", 22),
    Student("Charlie", 21)
]

print(students)  # Output: [Student(Name: Alice, Age: 20), Student(Name: Bob, Age: 22), Student(Name: Charlie, Age: 21)]
```

In this example, `students` is a list containing three `Student` objects. Each object has its own `name` and `age` attributes.

### Dictionary of Objects

A dictionary of objects in Python refers to a dictionary where the keys are used to access instances of a class. This is useful when you want to store objects in a way that allows for quick lookup based on a specific key. Here's an example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

# Creating a dictionary of Student objects
students_dict = {
    "A001": Student("Alice", 20),
    "B002": Student("Bob", 22),
    "C003": Student("Charlie", 21)
}

print(students_dict["A001"])  # Output: Student(Name: Alice, Age: 20)
```

In this example, `students_dict` is a dictionary where the keys (`"A001"`, `"B002"`, `"C003"`) are associated with different `Student` objects. This allows you to access each `Student` object by using its corresponding key.

### Key Points

- **List of Objects:** Allows storing multiple instances of a class in a single list. You can iterate over the list to perform operations on each object.

- **Dictionary of Objects:** Provides a key-value pairing where the key is used to access a specific object in the dictionary. This is useful for fast lookups and organizing objects by identifiers.

- **Use Cases:** These structures are commonly used in scenarios where you need to manage collections of objects, such as maintaining records of students, employees, or any other entities in a program.

> [!TIP]  
> Link to Next Article  
> 🡺 [Static Variables and Methods](/OOPs%20with%20Python/Articles/53_static_variables_and_methods.md)