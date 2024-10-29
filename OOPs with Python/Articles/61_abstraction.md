# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is Polymorphism?](/OOPs%20with%20Python/Articles/60_polymorphism.md)

### What is Abstraction?

**Abstraction** is a core concept in object-oriented programming (OOP) that focuses on hiding the implementation details of an object and exposing only the essential features or functionalities to the user. The idea is to simplify complex reality by modeling classes appropriate to the problem, separating the "what" from the "how." 

In simpler terms, abstraction means providing a simple interface to interact with while hiding the complex underlying logic.

### How is Abstraction Implemented in Python?

Python implements abstraction through the use of **abstract classes** and **interfaces**. Python provides the `abc` module to define abstract classes. An abstract class can have abstract methods, which are methods that are declared but contain no implementation. These abstract methods must be implemented in any subclass of the abstract class, making it possible to define a common interface for a group of related classes.

#### Example of Abstraction Using Abstract Class:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating an object of Rectangle
rect = Rectangle(4, 5)
print("Area:", rect.area())         # Output: Area: 20
print("Perimeter:", rect.perimeter()) # Output: Perimeter: 18
```
In this example, `Shape` is an abstract class with abstract methods `area()` and `perimeter()`. The `Rectangle` class inherits from `Shape` and provides specific implementations for these methods.

### Concepts Under the Umbrella of Abstraction

1. **Abstract Classes**: Abstract classes cannot be instantiated directly. They are designed to be inherited by other classes that implement the abstract methods.

2. **Abstract Methods**: These methods are declared in the abstract class but contain no implementation. Subclasses must provide their implementation.

3. **Interfaces**: While Python doesn't have interfaces as in some other languages (like Java), abstract classes with only abstract methods can function as interfaces, providing a way to enforce certain methods in the child classes.

### How is Abstraction Useful?

Abstraction is incredibly useful for several reasons:

1. **Encapsulation of Complexity**: It allows developers to hide complex details and expose only what is necessary, making the code easier to use and understand.
  
2. **Enhancing Modularity**: By separating the interface from the implementation, abstraction promotes modularity, where different parts of a system can be developed, tested, and maintained independently.

3. **Promotes Reusability**: Abstraction allows you to define common interfaces that can be reused across different parts of an application, reducing redundancy.

4. **Eases Maintenance**: Because the implementation details are hidden, it becomes easier to make changes to the internal workings of the code without affecting other parts of the program that rely on the abstracted interface.

### What Problems Does Abstraction Solve?

1. **Managing Complexity**: Abstraction helps in managing the complexity of large systems by breaking them down into simpler, more manageable pieces.
  
2. **Code Duplication**: By defining common interfaces and behaviors in abstract classes, abstraction helps eliminate code duplication and promotes DRY (Don't Repeat Yourself) principles.

3. **Inconsistency**: It enforces a consistent interface across different parts of the code, ensuring that all subclasses behave in a predictable manner when interacting with the abstract class or interface.

### Conclusion

Abstraction is a key principle in object-oriented programming that enables developers to manage complexity, promote modularity, and ensure reusability and maintainability of code. By using abstract classes and methods, Python allows programmers to define clear interfaces and enforce consistent behavior across related classes, simplifying both the design and maintenance of software systems.

> [!TIP]  
> Link to Next Article  
> 🡺 [What Are Files?](/File%20Handling/Articles/62_file_handling.md)