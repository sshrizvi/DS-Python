# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Comments in Python](/Python/Articles/5_comments.md) 💬

## Taking Inputs in Python 🖥️

In Python, the primary way to take user input is through the `input()` function. This function reads a line from the input (usually from the user) and returns it as a string.

### Using the `input()` Function:

1. **Basic Usage**:
   - The `input()` function can take an optional string argument which is displayed as a prompt to the user.
   ```python
   name = input("Enter your name: ")
   print("Hello, " + name + "!")
   ```

2. **Arguments and Settings**:
   - **`prompt`**: A string that is displayed to the user before taking the input. This is optional.
   ```python
   age = input("Enter your age: ")
   print("You are " + age + " years old.")
   ```

### Important Points and Edge Cases:

1. **Always Returns a String**:
   - The `input()` function always returns the input as a string. You may need to convert it to the appropriate type (e.g., `int`, `float`).
   ```python
   age = input("Enter your age: ")
   age = int(age)  # Convert to integer
   print("You will be " + str(age + 1) + " next year.")
   ```

2. **Handling Empty Input**:
   - If the user provides no input and just presses Enter, an empty string (`""`) is returned.
   ```python
   name = input("Enter your name: ")
   if name == "":
       print("You didn't enter your name!")
   else:
       print("Hello, " + name + "!")
   ```

3. **Handling Invalid Input**:
   - If you expect a certain type of input (e.g., a number), you should handle cases where the user provides invalid input.
   ```python
   try:
       age = int(input("Enter your age: "))
       print("You are " + str(age) + " years old.")
   except ValueError:
       print("That's not a valid number!")
   ```

4. **Multiline Input**:
   - For multiline input, you can use a loop to continuously read input until a certain condition is met (e.g., a blank line).
   ```python
   lines = []
   print("Enter text (type 'END' to stop):")
   while True:
       line = input()
       if line == "END":
           break
       lines.append(line)
   print("You entered:")
   print("\n".join(lines))
   ```

### Other Methods for Taking Input:

1. **Reading from Files**:
   - Input can also be taken from files using built-in functions like `open()`.
   ```python
   with open("input.txt", "r") as file:
       data = file.read()
       print(data)
   ```

2. **Command Line Arguments**:
   - Another way to take input is through command line arguments using the `sys` module.
   ```python
   import sys
   if len(sys.argv) > 1:
       print("Command line arguments:", sys.argv[1:])
   else:
       print("No command line arguments provided.")
   ```

3. **Using `getpass` for Secure Input**:
   - The `getpass` module can be used to securely input passwords without displaying them on the screen.
   ```python
   import getpass
   password = getpass.getpass("Enter your password: ")
   print("Password entered!")
   ```

### Summary

- The `input()` function is the primary way to take user input in Python, and it has a simple interface with an optional `prompt` argument.
- Always remember that `input()` returns a string, and you may need to convert it to the appropriate type.
- Handle edge cases like empty input and invalid input using appropriate checks and exception handling.
- Other methods for taking input include reading from files, command line arguments, and using the `getpass` module for secure inputs.

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->