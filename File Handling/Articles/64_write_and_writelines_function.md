# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [An In-Depth Guide to the `open()` Function in Python](/File%20Handling/Articles/63_open_function.md)

### File Writing in Python: `write()` and `writelines()` Functions

When handling files in Python, understanding the mechanisms for writing data is essential. This article will dive into two key functions for writing to files—`write()` and `writelines()`—and discuss how to use each effectively, along with their potential pitfalls.

#### 1. Opening a File for Writing

The `open()` function is used to open a file in different modes. For writing, you generally use:

- **`w`** mode: Opens a file for writing, truncating it if it exists, or creating it if it doesn’t.
- **`a`** mode: Opens a file for appending, writing at the end of the file, if it exists, or creating it if it doesn’t.

##### Syntax:
```python
file = open("filename.txt", mode)
```

#### 2. `write()` Function

The `write()` function allows us to write a single string to a file.

##### Syntax:
```python
file.write(string)
```

##### Example of `write()`:
```python
# Open the file in write mode
with open("example_write.txt", "w") as file:
    file.write("Hello, World!")
    file.write("\nWriting more content to the file.")
```

In this example, `"Hello, World!"` is written to the file, and then an additional line is appended within the same write session.

### Points to Note:
1. **Overwrites Content**: In `w` mode, if the file already has content, `write()` overwrites it completely.
2. **Automatic `str()` Conversion**: `write()` only accepts strings. If you try to write non-string data types like integers, an error occurs.

    ```python
    with open("example_write.txt", "w") as file:
        file.write(123)  # Raises TypeError
    ```
   
   To avoid this, convert data to a string with `str()`:
   
   ```python
   file.write(str(123))
   ```

3. **Writing in Binary Mode**: For binary files, you need to use `'wb'` mode and ensure data is in bytes.
   
   ```python
   with open("binary_example.bin", "wb") as file:
       file.write(b"This is binary content.")
   ```

### Dead-Ends with `write()`:
- If the file is not opened in write mode, `write()` will raise an error.
- Large data writes can slow down performance, as the function handles each call separately. It’s efficient to batch data using `writelines()` or to manage data flow for large files.

#### 3. `writelines()` Function

The `writelines()` function is used for writing multiple lines (usually from a list of strings) to a file in one go.

##### Syntax:
```python
file.writelines(lines)
```

##### Example of `writelines()`:
```python
# Open the file in write mode
with open("example_writelines.txt", "w") as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)
```

In this example, each element in the `lines` list is written to the file as a new line.

### Points to Note:
1. **No Newline Insertion**: Unlike `print()`, `writelines()` does not automatically insert newlines. You must add `\n` manually in each list item if you want separate lines.
   
   ```python
   lines = ["Line 1", "Line 2", "Line 3"]  # This will write everything on the same line
   ```

2. **Only Accepts Iterable**: `writelines()` only accepts an iterable of strings (like a list or tuple of strings). Passing non-string data, like integers, will cause an error unless each element is converted.

   ```python
   # Convert integers to strings before using writelines
   numbers = [str(i) + "\n" for i in range(1, 4)]
   with open("numbers.txt", "w") as file:
       file.writelines(numbers)
   ```

### Dead-Ends with `writelines()`:
- Forgetting the newline character will lead to a single continuous line of text, making the output hard to read.
- `writelines()` does not add extra separation between items; each item in the list or tuple is written exactly as provided.

#### 4. Choosing Between `write()` and `writelines()`

| Feature      | `write()`                    | `writelines()`                       |
|--------------|------------------------------|--------------------------------------|
| Purpose      | Writes a single string       | Writes an iterable of strings        |
| Newline      | Must be included manually    | Must be included in each item        |
| Use Case     | Small content or one-liners  | Multiple lines or batch writing      |
| Limitations  | Cannot take lists directly   | Cannot add separators between items  |

##### Practical Use Case:
For data scientists handling large datasets, `writelines()` can speed up the output process when writing data to text files, as it avoids multiple calls to `write()` for each line. However, care is needed to ensure that each item in the list has a newline character if the data is intended to be separated line-by-line.

#### 5. Closing Files

Though files can be closed manually using `file.close()`, using the `with` statement ensures that files are closed automatically after their block is executed.

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed here
```

## Conclusion

Understanding when to use `write()` and `writelines()` is essential for efficient file handling in Python. The choice between these functions can have significant implications for the readability and performance of your code, especially when working with large datasets. By using the `with` statement and carefully formatting strings, Python offers flexible and powerful tools for managing file outputs, helping avoid common pitfalls and ensuring smooth data writing processes.

> [!TIP]  
> Link to Next Article  
> 🡺 [Advanced File Handling in Python: `with` Keyword, `tell()`, `seek()`, and Working with Binary Files](/File%20Handling/Articles/65_with_keyword.md)