# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is the Real Use of a Constructor?](/OOPs%20with%20Python/Articles/41_use_of_constructors.md)

### What is the `self` Keyword? What Does it Do?

The `self` keyword in Python is a reference to the current instance of the class. It is used to access variables that belong to the class. In essence, `self` represents the object that the method is being called on, and it allows access to the class attributes and methods within the class's scope.

### Working of `self` Keyword

1. **Accessing Instance Variables**:
   - When you define an instance variable (an attribute specific to an object) inside a class, you use `self` to refer to it. This allows you to store data within an object and retrieve or modify it later.
   
   - **Example**:
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age
         
         def display_info(self):
             print(f"Name: {self.name}, Age: {self.age}")

     person = Person("Alice", 30)
     person.display_info()
     ```

2. **Calling Other Methods Within the Class**:
   - The `self` keyword is also used to call other methods within the same class. This is important for maintaining a proper object-oriented design, where methods work together to perform tasks on the object's data.
   
   - **Example**:
     ```python
     class Calculator:
         def __init__(self, number):
             self.number = number
         
         def add(self, value):
             return self.number + value
         
         def multiply(self, value):
             return self.number * value
         
         def operate(self):
             addition = self.add(10)
             multiplication = self.multiply(2)
             return addition, multiplication

     calc = Calculator(5)
     print(calc.operate())
     ```

3. **Distinguishing Between Local and Instance Variables**:
   - In a method, `self` helps distinguish between instance variables and local variables. Without `self`, Python would not know whether you're referring to an instance variable or a local variable within the method.
   
   - **Example**:
     ```python
     class Example:
         def __init__(self, value):
             self.value = value  # Instance variable
         
         def change_value(self, value):
             value = value  # Local variable
             self.value = value  # Assigning local variable to instance variable

     obj = Example(10)
     obj.change_value(20)
     print(obj.value)  # Output: 20
     ```

4. **`self` is Not a Reserved Keyword**:
   - Although `self` is widely used by convention, it is not a reserved keyword in Python. You can technically use any other name in place of `self`, but it is strongly recommended to stick with `self` for clarity and consistency.

   - **Example**:
     ```python
     class Example:
         def __init__(myself, value):
             myself.value = value
         
         def display(myself):
             print(myself.value)

     obj = Example(10)
     obj.display()
     ```

### Important Points to Remember

- **Always Explicit**: In Python, `self` is always explicitly included as the first parameter in instance methods. This is different from some other programming languages where the equivalent of `self` is implicit.

- **Instance Specific**: `self` is specific to the object that is invoking the method. This allows each object to have its own set of attributes.

- **Not Used for Class or Static Methods**: The `self` keyword is only relevant in instance methods. For class methods and static methods, `self` is replaced by `cls` and no instance is passed, respectively.

- **It’s a Convention**: Using `self` is a convention and a standard practice in Python. Breaking this convention can make your code difficult to read and maintain.

### Conclusion

The `self` keyword is fundamental in Python's object-oriented programming, allowing methods to interact with instance attributes and other methods. It ties the data (attributes) and behavior (methods) together in a class, making it possible to create objects that function correctly and maintain their state throughout their lifecycle. For data scientists, understanding `self` is crucial when building classes to encapsulate data and functions in a clean, maintainable way.

> [!TIP]  
> Link to Next Article  
> 🡺 [Functions and Methods in Python](/OOPs%20with%20Python/Articles/43_functions_vs_methods.md)