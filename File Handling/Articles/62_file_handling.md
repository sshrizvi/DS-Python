# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [What is Abstraction?](/OOPs%20with%20Python/Articles/61_abstraction.md)

### What Are Files?

A **file** is a named location on storage media that stores information permanently, unlike temporary data stored in memory (RAM), which is erased when the program exits. Files are typically used to store data in a structured format and can hold different types of data, such as text, images, videos, and more.

Files in programming are essential as they allow data to be stored and accessed across different runs of a program. In Python, we work with files through **file handling** techniques to read from, write to, and manipulate files on disk.

### What is File Handling?

**File handling** is the process of opening, reading, writing, and closing files from within a program. This enables a program to perform various operations on files, such as:

- **Reading** data from a file
- **Writing** data to a file
- **Appending** data to an existing file
- **Closing** a file after operations are complete

These operations allow data to be accessed, stored, and manipulated even after the program that created them has ended. File handling is crucial in data persistence, data analysis, and many real-world applications.

### How is File Handling Achieved in Python?

Python provides a built-in function, `open()`, to handle files. The basic syntax is:
```python
file_object = open("filename", "mode")
```

#### Modes of File Handling in Python

| Mode | Description |
|------|-------------|
| `"r"` | Opens a file for reading (default). Error if the file does not exist. |
| `"w"` | Opens a file for writing, creating a new file or truncating existing content. |
| `"a"` | Opens a file for appending data to the end without overwriting. |
| `"b"` | Opens in binary mode (for non-text files like images). |
| `"r+"` | Opens a file for both reading and writing. |

#### Example: Basic File Operations

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending a new line!")
```

The `with` statement is commonly used as it handles file closure automatically.

### Key Operations in File Handling

1. **Reading a File**: Python allows reading an entire file or reading line by line with `read()` and `readline()`.
   ```python
   # Read the entire content
   content = file.read()
   
   # Read line by line
   for line in file:
       print(line)
   ```

2. **Writing to a File**: Writing overwrites existing content if the file is opened in `"w"` mode.
   ```python
   file.write("New content!")
   ```

3. **Appending**: Adding data to the end without removing existing data.
   ```python
   file.write("\nAdded content at the end!")
   ```

4. **Closing a File**: While Python handles file closure with `with`, it can also be done manually with `file.close()`.

### Why Use File Handling in Python?

File handling is essential for:

- **Data persistence**: Storing data that can be retrieved and analyzed later.
- **Data logging**: Writing logs that can be used for debugging.
- **Data exchange**: Sharing data between different programs or systems.
  
Python's file handling is robust and flexible, making it suitable for applications ranging from web development to scientific computing.

> [!TIP]  
> Link to Next Article  
> 🡺 [An In-Depth Guide to the `open()` Function in Python](/File%20Handling/Articles/63_open_function.md)