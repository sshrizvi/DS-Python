# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Some Useful Functions for Data Scientists](/Python/Articles/38_miscellaneous_functions.md)


### Object-Oriented Programming (OOP)

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object is a self-contained component that contains properties (attributes) and behaviors (methods). OOP is based on several principles that promote modularity, reusability, and flexibility in code.

### Classes and Objects

#### What is a Class?
A **class** in OOP is a blueprint or prototype from which objects are created. It defines a set of attributes and methods that the created objects will have.

- **Attributes**: These are the data stored in the object, typically variables.
- **Methods**: These are functions defined inside the class that describe the behaviors of the objects.

**Example of a Class:**

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.make} {self.model} is now running."

    def stop_engine(self):
        return f"The engine of the {self.make} {self.model} is now stopped."
```

In this example, `Car` is a class with attributes `make`, `model`, and `year`, and it has methods `start_engine` and `stop_engine`.

#### What is an Object?
An **object** is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created. The object represents the actual entity in the real world and can use the methods and attributes defined in the class.

**Example of Creating Objects:**

```python
# Creating an object of the class Car
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the object's attributes
print(my_car.make)  # Output: Toyota
print(my_car.model) # Output: Corolla
print(my_car.year)  # Output: 2020

# Using the object's methods
print(my_car.start_engine())  # Output: The engine of the Toyota Corolla is now running.
print(my_car.stop_engine())   # Output: The engine of the Toyota Corolla is now stopped.
```

In this example, `my_car` is an object of the `Car` class. We can access its attributes and call its methods.

### Conclusion
Object-Oriented Programming is a powerful paradigm that helps in organizing complex programs, making them more modular, reusable, and maintainable. Understanding classes and objects is fundamental to mastering OOP, as they are the building blocks for creating structured and efficient code.

### Further Reading
For a deeper understanding of OOP in Python, refer to the following resources:
- [Python OOP Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/python-oops-concepts/)
- [OOP in Python - Real Python](https://realpython.com/python3-object-oriented-programming/) 

These articles provide comprehensive insights and examples to help you master OOP concepts in Python.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is a Constructor in Python?](/OOPs%20with%20Python/Articles/40_constructors.md)