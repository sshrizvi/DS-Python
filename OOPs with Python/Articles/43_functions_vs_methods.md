# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is the `self` Keyword?](/OOPs%20with%20Python/Articles/42_self_keyword.md)

### Functions and Methods in Python

#### What are Functions in Python?

**Functions** in Python are blocks of reusable code designed to perform a specific task. They help in organizing code, reducing redundancy, and making the code more modular and readable. A function is defined using the `def` keyword, followed by the function name and parentheses containing any parameters. Once defined, a function can be called from anywhere in the code.

**Key Characteristics of Functions**:
- **Reusable**: Functions can be called multiple times in different parts of the program.
- **Modular**: Functions allow code to be organized into smaller, manageable chunks.
- **Encapsulation**: Functions can encapsulate logic, making code more understandable and maintainable.
  
**Example**:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

#### What are Methods in Python?

**Methods** in Python are similar to functions, but they are associated with objects. Methods are functions that are defined within a class and are called on an instance of that class. In other words, methods operate on the data that belongs to an object (instance of a class).

**Key Characteristics of Methods**:
- **Belong to Objects**: Methods are tied to the object instances of a class.
- **Implicit First Argument**: Methods take the object itself as the first argument, typically named `self`.
- **Access to Object's Data**: Methods can access and modify the object’s data.

**Example**:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.bark())  # Output: Buddy says Woof!
```

#### How Functions are Different from Methods in Python

| **Aspect**          | **Function**                                          | **Method**                                                      |
|---------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| **Definition**      | Defined outside of a class using the `def` keyword.   | Defined inside a class and operates on an instance of the class.|
| **First Parameter** | Does not require any specific first parameter.        | Requires `self` as the first parameter, referring to the object instance.|
| **Call**            | Called independently, using the function name.        | Called on an object instance, using the dot notation (`object.method()`).|
| **Association**     | Not tied to any object or data.                       | Tied to an object, can modify or access the object’s attributes.|
| **Usage Context**   | General purpose, used for performing standalone tasks.| Used to define the behavior of an object, often manipulating the object’s state.|

**Example Comparison**:
- **Function**:
  ```python
  def add(a, b):
      return a + b

  print(add(3, 4))  # Output: 7
  ```
- **Method**:
  ```python
  class Calculator:
      def add(self, a, b):
          return a + b

  calc = Calculator()
  print(calc.add(3, 4))  # Output: 7
  ```

**Key Points**:
- **Binding**: Methods are bound to objects and can access the object’s internal data (`self`), whereas functions are not bound to any data.
- **Usage**: Functions are more flexible and can be used in various contexts, while methods are specific to the behavior of an object.

Understanding the difference between functions and methods is crucial for effective programming in Python, especially when working with object-oriented programming (OOP). Functions allow for code reuse and modular design, while methods enable objects to have behavior and state encapsulation.

> [!TIP]  
> Link to Next Article  
> 🡺 [What are Magic Methods in Python?](/OOPs%20with%20Python/Articles/44_dunder_methods.md)