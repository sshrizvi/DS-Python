# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is Method Overriding in Python?](/OOPs%20with%20Python/Articles/58_method_overriding.md)

### What is the `super` Keyword in Python?

The `super` keyword in Python is a built-in function that returns a proxy object representing the parent class. This proxy object allows you to call methods and access properties from the parent class that have been overridden in the current class. The `super` function is most commonly used in inheritance when you want to extend or modify the behavior of the parent class method in the child class.

> [!IMPORTANT]  
> The `super` function can only be used inside the child class.

### What Does `super` Do?

The `super` function provides a way to access methods from a superclass (or parent class) without explicitly naming the parent class. This can be particularly useful when working with multiple inheritance or complex inheritance hierarchies.

### Syntax

The typical usage of `super` is:

```python
super().method_name(arguments)
```

Here, `method_name` is a method from the parent class, and `arguments` are the parameters you want to pass to that method.

### What Problem Does `super` Solve?

1. **Avoiding Redundancy**: Without `super`, you would need to explicitly name the parent class when calling its methods. This can lead to redundancy and potential errors, especially in cases of multiple inheritance.

2. **Facilitating Multiple Inheritance**: In cases of multiple inheritance, `super` simplifies the process of ensuring that the correct method resolution order (MRO) is followed. MRO is the order in which Python looks for a method in a hierarchy of classes. `super` ensures that the next class in the MRO is called, rather than potentially skipping over classes.

3. **Simplifying Maintenance**: By using `super`, you make your code more maintainable and flexible. If you change the class hierarchy, you don't need to update every reference to the parent class explicitly.

### Example of Using `super`

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the __init__ method of the parent class
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        # Extending the behavior of the sound method
        return f"{super().sound()}... Bark"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.sound())  # Output: Some sound... Bark
```

### Benefits of Using `super`

- **Cleaner Code**: Eliminates the need to hard-code the parent class name, leading to more readable and maintainable code.
  
- **Supports MRO**: Ensures that the correct order of method calls is maintained, especially in complex inheritance scenarios.

- **Adaptability**: If the class hierarchy changes, `super` automatically adjusts to the new structure without needing extensive code changes.

### Considerations

- **MRO and Multiple Inheritance**: In a multiple inheritance scenario, `super` ensures that the next class in the method resolution order is called, which might not always be the immediate parent. Understanding MRO is crucial when using `super` in such cases.

- **Not Limited to `__init__`**: While commonly used in constructors, `super` can be used with any method to access or extend its functionality.

### Conclusion

The `super` keyword is a powerful tool in Python that enhances the flexibility and maintainability of your code, especially when dealing with inheritance. It helps in avoiding redundancy, managing complex inheritance hierarchies, and ensuring that changes in the class structure don't lead to errors. Understanding and using `super` effectively is crucial for writing robust and scalable object-oriented programs in Python.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is Polymorphism?](/OOPs%20with%20Python/Articles/60_polymorphism.md)