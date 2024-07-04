# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP] Link to Previous Article  
> 🡸 [Data Types in Python](/Python/Articles/3_data_types.md) 💊

## Python is a Dynamically Typed Language ⚡
In programming languages, "*typing*" refers to *how a language handles and enforces the data types of variables*. When we say that Python is a dynamically typed language, it means several things:

1. **Variable Types are Determined at Runtime**:
   - In Python, you don't need to declare the type of a variable when you create it. The type is inferred when the variable is first assigned a value and can change dynamically as the program executes.
   ```python
   a = 10        # a is an integer
   print(type(a))  # Output: <class 'int'>
   
   a = "hello"   # Now a is a string
   print(type(a))  # Output: <class 'str'>
   ```

2. **Type Flexibility**:
   - Since the type of a variable can change, you can assign different types of values to the same variable during execution.
   ```python
   a = 5         # a is an integer
   a = [1, 2, 3] # Now a is a list
   ```

3. **No Need for Explicit Type Declarations**:
   - Unlike statically typed languages (like C or Java), where you must declare the type of a variable before using it, Python does this automatically.
   ```python
   # In C:
   # int a = 10;
   
   # In Python:
   a = 10  # Python automatically determines that a is an integer
   ```

4. **Type Checking is Done at Runtime**:
   - Python performs type checking at runtime, meaning that it verifies the types of variables and ensures they are used correctly as the code runs.
   ```python
   a = 10
   a = "hello"
   print(a + 5)  # This will raise a TypeError at runtime
   ```

5. **Duck Typing**:
   - Python uses the concept of "duck typing," which means that the type or class of an object is less important than the methods it defines or the way it behaves. If an object behaves like a duck (supports certain methods), it is treated as a duck.
   ```python
   class Duck:
       def quack(self):
           print("Quack!")
   
   class Person:
       def quack(self):
           print("I'm quacking like a duck!")
   
   def make_it_quack(duck):
       duck.quack()
   
   d = Duck()
   p = Person()
   
   make_it_quack(d)  # Output: Quack!
   make_it_quack(p)  # Output: I'm quacking like a duck!
   ```

6. **Type Inference**:
   - Python's interpreter determines the type of a variable based on the value assigned to it. This allows for more concise and readable code.
   ```python
   a = 10            # int
   b = 10.5          # float
   c = "hello"       # str
   d = [1, 2, 3]     # list
   ```

### Advantages of Dynamic Typing:
- **Ease of Use**: Writing code is more straightforward and requires fewer lines, as you don't need to specify types.
- **Flexibility**: You can write more generic and reusable code that works with multiple types.
- **Rapid Development**: Development is faster because you don't need to manage type declarations and conversions.

### Disadvantages of Dynamic Typing:
- **Runtime Errors**: Type-related errors can only be detected at runtime, potentially making debugging more challenging.
- **Performance**: Dynamic typing can be slower than static typing, as type checks are performed at runtime.
- **Lack of Explicitness**: The lack of type declarations can make the code less clear and harder to understand, especially in large codebases.

### Tips for Working with Dynamic Typing:
- **Use Comments and Docstrings**: Document the expected types of variables and function parameters.

  ```python
  def add_numbers(a, b):
      """
      Add two numbers.

      :param a: int or float
      :param b: int or float
      :return: int or float
      """
      return a + b
  ```
- **Leverage Type Hints**: Use type hints to indicate the expected types, improving code readability and enabling better static analysis tools.
  ```python
  def add_numbers(a: int, b: int) -> int:
      return a + b
  ```

Understanding Python's dynamic typing nature helps in writing more flexible and maintainable code. 😊

> [!TIP] Link to Next Article
> 🡺 [Comments in Python](/Python/Articles/5_comments.md) 💬