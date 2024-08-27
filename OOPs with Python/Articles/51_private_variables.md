# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is Encapsulation?](/OOPs%20with%20Python/Articles/50_encapsulation.md)

### Private Variables in Python

In Python, private variables are a way to indicate that a variable should not be accessed or modified directly outside of the class it belongs to. This is part of the encapsulation principle in object-oriented programming (OOP). 

### How to Make a Variable Private in Python

To make a variable private in Python, you use a double underscore `__` prefix before the variable name. For example:

```python
class MyClass:
    def __init__(self):
        self.__private_var = 42  # Private variable

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # Access via method: Works fine
print(obj.__private_var)      # Direct access: Raises AttributeError
```

In the example above, `__private_var` is a private variable, and it cannot be accessed directly from outside the class. Attempting to do so raises an `AttributeError`.

### What Happens to the Name of the Variable When It Is Made Private?

When you make a variable private by prefixing it with double underscores (`__`), Python performs a process known as **name mangling**. This means that Python changes the name of the private variable to include the class name as a prefix. This is done to ensure that the private variable is not easily accessible from outside the class, even if someone tries to access it directly.

For example, in the class `MyClass`, the private variable `__private_var` is internally renamed to `_MyClass__private_var`.

You can see this in action:

```python
print(obj._MyClass__private_var)  # Accessing the private variable using name mangling
```

This will output `42`, demonstrating that `__private_var` has been renamed to `_MyClass__private_var`.

### Key Points to Remember

- **Name Mangling:** When you declare a private variable with a `__` prefix, Python automatically renames it to `_ClassName__VariableName`. This helps to prevent accidental access or modification from outside the class.
  
- **Accessibility:** Despite name mangling, private variables can still technically be accessed from outside the class if you know the mangled name. However, doing so is strongly discouraged, as it goes against the principles of encapsulation.

- **Not Absolute:** The "privacy" provided by double underscores is not absolute. It’s more of a convention and a mechanism to avoid accidental name collisions in subclasses, rather than a strict access control feature.

By understanding how private variables work and how Python handles them with name mangling, developers can better protect the internal state of their objects and adhere to good OOP practices.

> [!TIP]  
> Link to Next Article  
> 🡺 [List and Dictionaries of Objects](/OOPs%20with%20Python/Articles/52_objects_are_elements.md)