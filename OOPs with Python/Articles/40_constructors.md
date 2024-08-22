# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Object-Oriented Programming (OOP)](../../OOPs%20with%20Python/Articles/39_intro_to_oops.md)

### What is a Constructor in Python?

A **constructor** in Python is a special method used to initialize the objects of a class. The constructor method is defined using the `__init__()` method and is automatically called when an object of the class is created. Constructors help set up initial states of the object, like initializing variables or setting default values.

### Types of Constructors in Python

1. **Default Constructor**
   - **Definition**: A default constructor is a simple constructor that doesn’t accept any arguments from the user except `self`.
   - **Example**:
     ```python
     class MyClass:
         def __init__(self):
             self.name = "John"
     
     obj = MyClass()
     print(obj.name)  # Output: John
     ```

2. **Parameterized Constructor**
   - **Definition**: A parameterized constructor allows you to pass arguments to the `__init__()` method to initialize the object with specific values.
   - **Example**:
     ```python
     class MyClass:
         def __init__(self, name, age):
             self.name = name
             self.age = age
     
     obj = MyClass("John", 25)
     print(obj.name)  # Output: John
     print(obj.age)   # Output: 25
     ```

3. **Non-parameterized Constructor**
   - **Definition**: Similar to the default constructor, but with custom initializations done within the method.
   - **Example**:
     ```python
     class MyClass:
         def __init__(self):
             self.data = []
     
     obj = MyClass()
     print(obj.data)  # Output: []
     ```

### Important Points and Tricks for Data Scientists

- **Mutable Default Arguments**: 
  - Be cautious when using mutable types (like lists or dictionaries) as default arguments in a constructor. They can lead to unexpected behavior because they maintain state between different object instances.
  - **Example**:
    ```python
    class MyClass:
        def __init__(self, data=[]):
            self.data = data

    obj1 = MyClass()
    obj1.data.append(1)
    print(obj1.data)  # Output: [1]

    obj2 = MyClass()
    print(obj2.data)  # Output: [1] - Expected []
    ```
  - **Solution**: Use `None` as the default value and initialize inside the constructor.
    ```python
    class MyClass:
        def __init__(self, data=None):
            if data is None:
                data = []
            self.data = data
    ```

- **Chaining Constructors**:
  - You can chain constructors in inheritance hierarchies by calling `super().__init__()` within the constructor of the child class to ensure that the parent class constructor is also executed.
  - **Example**:
    ```python
    class Parent:
        def __init__(self, name):
            self.name = name
            print(f"Parent Constructor called: {self.name}")

    class Child(Parent):
        def __init__(self, name, age):
            super().__init__(name)
            self.age = age
            print(f"Child Constructor called: {self.name}, Age: {self.age}")

    obj = Child("John", 25)
    ```

- **Immutability**:
  - Data scientists often deal with large datasets, where immutability can be important for maintaining data integrity. Constructors can be used to set up immutable attributes using properties or the `@dataclass(frozen=True)` decorator (from Python 3.7+).
  - **Example**:
    ```python
    from dataclasses import dataclass
    
    @dataclass(frozen=True)
    class MyClass:
        name: str
        age: int

    obj = MyClass("John", 25)
    # obj.name = "Doe"  # This will raise an error
    ```

### Conclusion

Constructors play a crucial role in object-oriented programming in Python by setting up the initial state of objects. Understanding the different types of constructors and their nuances is essential for building robust and error-free applications, especially in data-intensive domains like Data Science.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is the Real Use of a Constructor?](/OOPs%20with%20Python/Articles/41_use_of_constructors.md)