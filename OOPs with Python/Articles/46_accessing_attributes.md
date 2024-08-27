# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What are Class Diagrams?](/OOPs%20with%20Python/Articles/45_class_diagrams.md)

### Accessing Attributes of a Class Using Objects

In Python, attributes are variables that belong to an instance (or object) of a class. You can access these attributes using the dot (`.`) notation. Here's how you can access and interact with attributes in a class:

### 1. Accessing Attributes

Once an object of a class is created, you can access its attributes using the syntax:

```python
object_name.attribute_name
```

#### Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating an object of the class
my_car = Car("Toyota", "Corolla")

# Accessing attributes
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Corolla
```

In this example, `my_car` is an instance of the `Car` class, and its attributes `make` and `model` are accessed using dot notation.

### 2. Attribute Creation Outside the Class

Python allows you to create or modify attributes outside of the class definition. This is a unique feature of Python that can sometimes lead to unexpected behaviors.

#### Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating an object of the class
my_car = Car("Toyota", "Corolla")

# Adding a new attribute outside the class definition
my_car.year = 2022

print(my_car.year)  # Output: 2022
```

In this example, the attribute `year` was not defined in the `Car` class, but it was created on the fly for the `my_car` object.

### Shocking Information: Python's Dynamic Attribute Handling

One of the more surprising behaviors in Python is that attributes can be dynamically added to objects at runtime. This means that different instances of the same class can have different attributes.

#### Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating two objects of the class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Adding a unique attribute to car1
car1.year = 2022

# Accessing the unique attribute
print(car1.year)  # Output: 2022

# Trying to access the same attribute in car2
print(car2.year)  # Raises AttributeError: 'Car' object has no attribute 'year'
```

**Key Point:**
- **AttributeError:** If you try to access an attribute that doesn’t exist for a particular object, Python will raise an `AttributeError`. This is important to keep in mind, especially when dynamically adding attributes to objects.

### Conclusion

Python’s flexibility in handling attributes allows for powerful and dynamic object-oriented programming. However, this can also introduce potential pitfalls, particularly if you're not careful about attribute management across different instances of a class. Understanding these behaviors is crucial for becoming an expert Python developer.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is a Reference Variable in Python?](/OOPs%20with%20Python/Articles/47_reference_variables.md)