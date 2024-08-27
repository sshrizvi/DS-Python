# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Types of Inheritance in Python](/OOPs%20with%20Python/Articles/56_inheritance.md)

### What is Method Overriding in Python?

**Method Overriding** is a feature in object-oriented programming where a subclass provides a specific implementation for a method that is already defined in its superclass. The method in the subclass has the same name, return type, and parameters as the method in the superclass.

When the overridden method is called on an object of the subclass, the implementation in the subclass is executed, effectively "overriding" the behavior of the method in the superclass.

### Why is Method Overriding Useful?

1. **Polymorphism**: Method overriding is a key aspect of polymorphism, allowing different classes to be treated as instances of the same parent class. This enables the use of the same method call in different contexts, depending on the object type.

2. **Extending or Modifying Superclass Behavior**: It allows you to extend or completely change the behavior of a method in the parent class. This is useful when you want the child class to have a specialized behavior while still inheriting most of its functionality from the parent class.

3. **Code Reusability**: By overriding methods, you can reuse code and avoid redundancy. You can take advantage of the base class's logic and only modify what needs to be changed in the subclass.

4. **Flexibility**: It provides the flexibility to define different behaviors for the same method across various subclasses, leading to more flexible and maintainable code.

### Example of Method Overriding in Python

```python
class Animal:
    def sound(self):
        return "This animal makes a sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()

# Calling the overridden methods
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
```

In this example, the `Dog` and `Cat` classes override the `sound` method of the `Animal` class to provide their specific implementations. When `sound` is called on a `Dog` or `Cat` object, the method in the respective subclass is executed.

### Considerations and Warnings

- **Calling the Parent Class Method**: Sometimes, you may want to use the method from the parent class in addition to the overridden behavior in the child class. You can do this using the `super()` function.

  ```python
  class Animal:
      def sound(self):
          return "This animal makes a sound"

  class Dog(Animal):
      def sound(self):
          base_sound = super().sound()
          return f"{base_sound} and it barks"

  dog = Dog()
  print(dog.sound())  # Output: This animal makes a sound and it barks
  ```

- **Overriding vs. Overloading**: Python does not support method overloading (having multiple methods with the same name but different parameters). Method overriding should not be confused with overloading.

- **Dynamic Nature of Python**: Because Python is dynamically typed, method overriding provides a powerful tool to dynamically change behavior at runtime, but it also requires careful management to avoid unexpected results.

### Conclusion

Method overriding in Python is a powerful tool that allows subclasses to alter or extend the behavior of methods inherited from a superclass. It is a fundamental concept in object-oriented programming that enhances code reusability, flexibility, and supports polymorphism. Understanding and properly utilizing method overriding can lead to more organized, maintainable, and scalable code.

> [!TIP]  
> Link to Next Article  
> 🡺 [What is the `super` Keyword in Python?](/OOPs%20with%20Python/Articles/59_super_keyword.md)