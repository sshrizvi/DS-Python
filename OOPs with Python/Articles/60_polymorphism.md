# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is the `super` Keyword in Python?](/OOPs%20with%20Python/Articles/59_super_keyword.md)

### What is Polymorphism?

Polymorphism is a fundamental concept in object-oriented programming (OOP) that refers to the ability of different objects to be treated as instances of the same class through a common interface. The word "polymorphism" is derived from Greek roots meaning "many forms." In simpler terms, polymorphism allows one interface to be used for a general class of actions, with the specific action being determined by the exact nature of the situation.

### How is Polymorphism Implemented in Python?

Python, being a dynamically typed and object-oriented language, implements polymorphism in a natural and flexible way. Polymorphism in Python can be achieved in several ways:

1. **Duck Typing**:
   - Python follows the principle of "duck typing," where the type or class of an object is less important than the methods it defines or the operations it supports. If an object can perform the required behavior (i.e., it "quacks like a duck"), it is treated as that type.
   - Example:
     ```python
     class Dog:
         def speak(self):
             return "Woof!"

     class Cat:
         def speak(self):
             return "Meow!"

     def animal_sound(animal):
         print(animal.speak())

     dog = Dog()
     cat = Cat()

     animal_sound(dog)  # Output: Woof!
     animal_sound(cat)  # Output: Meow!
     ```

2. **Method Overriding**:
   - Inheritance allows a child class to inherit properties and methods from a parent class. Polymorphism comes into play when a child class provides a specific implementation of a method that is already defined in its parent class. This process is known as method overriding.
   - Example:
     ```python
     class Animal:
         def speak(self):
             return "Animal sound"

     class Dog(Animal):
         def speak(self):
             return "Woof!"

     class Cat(Animal):
         def speak(self):
             return "Meow!"

     animals = [Dog(), Cat(), Animal()]

     for animal in animals:
         print(animal.speak())

     # Output:
     # Woof!
     # Meow!
     # Animal sound
     ```

3. **Operator Overloading**:
   - Python allows operators to have different meanings based on the context in which they are used. This ability to define multiple behaviors for the same operator depending on the type of objects involved is known as operator overloading, a form of polymorphism.
   - Example:
     ```python
     class Vector:
         def __init__(self, x, y):
             self.x = x
             self.y = y

         def __add__(self, other):
             return Vector(self.x + other.x, self.y + other.y)

         def __repr__(self):
             return f"Vector({self.x}, {self.y})"

     v1 = Vector(2, 10)
     v2 = Vector(5, -2)
     print(v1 + v2)  # Output: Vector(7, 8)
     ```

### Concepts Under the Umbrella of Polymorphism

1. **Method Overriding**: This occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
  
2. **Method Overloading**: Although Python doesn't support method overloading in the traditional sense, it can be simulated using default arguments or variable-length arguments (`*args`, `**kwargs`).

3. **Duck Typing**: Python's dynamic typing system allows polymorphism through duck typing, where an object's suitability for a role is determined by its methods and properties rather than its actual type.

4. **Operator Overloading**: Polymorphism is also achieved through operator overloading, where operators like `+`, `-`, `*`, etc., are given different meanings based on the objects they operate on.

### Conclusion

Polymorphism in Python is a versatile and powerful feature that allows developers to write flexible and reusable code. By enabling objects of different classes to be treated as objects of a common superclass, polymorphism promotes the use of generalized code and is a cornerstone of effective object-oriented programming. Whether through duck typing, method overriding, or operator overloading, polymorphism makes it possible to design systems that are both extensible and easy to maintain.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is Abstraction?](/OOPs%20with%20Python/Articles/61_abstraction.md)