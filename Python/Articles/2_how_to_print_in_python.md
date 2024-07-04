# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP] Link to Previous Article
> 🡸 [What is Python ?](/Python/Articles/1_what_is_python.md)


## Printing in Python 🖨️

The `print()` function in Python is used to output text or other data to the console. It's one of the most commonly used functions, especially for debugging and displaying information.

#### Basic Usage
```python
print("Hello, World!")
```

#### Parameters and Settings of `print()` function

The `print()` function has several parameters that allow you to customize its behavior:

1. **`objects`**: One or more objects to be printed. Multiple objects can be separated by commas.
2. **`sep`**: Specifies the separator between multiple objects. The default is a space.
3. **`end`**: Specifies what to print at the end. The default is a newline character (`\n`).
4. **`file`**: Specifies the file-like object to which the output is sent. The default is `sys.stdout`.
5. **`flush`**: A boolean that specifies whether to forcibly flush the stream. The default is `False`.

#### Examples

1. **Basic Printing**:
    ```python
    print("Hello, World!")  # Prints "Hello, World!"
    ```

2. **Printing Multiple Objects**:
    ```python
    print("Hello", "World", "!")  # Prints "Hello World !"
    ```

3. **Using `sep` Parameter**:
    ```python
    print("Hello", "World", "!", sep="-")  # Prints "Hello-World-!"
    ```

4. **Using `end` Parameter**:
    ```python
    print("Hello, World!", end="")  # Prints "Hello, World!" without a newline
    print("This is on the same line.")
    ```

5. **Redirecting Output to a File**:
    ```python
    with open("output.txt", "w") as f:
        print("Hello, World!", file=f)  # Writes "Hello, World!" to the file
    ```

6. **Flushing the Output Buffer**:
    ```python
    import time

    for i in range(5):
        print(i, end=" ", flush=True)
        time.sleep(1)  # Prints numbers 0 to 4 with a 1-second interval
    ```
This is how printing in Python works. 😊

> [!TIP] Link to Next Article
>  🡺 [Data Types in Python](/Python/Articles/3_data_types.md) 💊