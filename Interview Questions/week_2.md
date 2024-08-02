<div align = center>
    <h1>📚 <b>Interview Questions</b></h1>
</div>

## **Week 02 :** *Lists, Dictionaries, Tuples, Sets*


<details>
<summary>  ❓ <i>Question 16 : What is aliasing in Python ?</i> </summary>

***Answer :*** 
**Aliasing** in Python refers to the situation where multiple variable names refer to the same object in memory. This can happen with any mutable or immutable objects. Aliasing allows you to access and modify the object through different names.

### How Aliasing is Done

Aliasing occurs naturally when you assign an existing variable to another variable. Both variables will then refer to the same object.

### Examples of Aliasing

#### 1. Aliasing with Immutable Objects

Even though aliasing can occur with immutable objects (like integers, strings, and tuples), you cannot change the object itself. Any operation that appears to modify the object will actually create a new object.

```python
a = 42
b = a
print(a, b)  # Output: 42 42
b = 100
print(a, b)  # Output: 42 100
```

In this example, `a` and `b` initially refer to the same integer object `42`. When `b` is assigned a new value `100`, it creates a new object, and `a` remains unchanged.

#### 2. Aliasing with Mutable Objects

Aliasing is more impactful with mutable objects (like lists, dictionaries, and sets) because changes made through one alias affect the object and are visible through all aliases.

```python
# Aliasing with a list
list1 = [1, 2, 3]
list2 = list1

print(list1, list2)  # Output: [1, 2, 3] [1, 2, 3]

# Modify the list through list2
list2.append(4)
print(list1, list2)  # Output: [1, 2, 3, 4] [1, 2, 3, 4]
```

In this example, `list1` and `list2` both refer to the same list object. Modifying the list through `list2` also affects `list1`.

### Checking Aliases

You can check if two variables are aliases of the same object using the `is` operator, which checks for object identity.

```python
print(list1 is list2)  # Output: True
```

### Aliasing Pitfalls

Aliasing can lead to unintended side effects, especially with mutable objects, since changes through one alias affect all aliases. This can make the code harder to understand and debug.

### Avoiding Unwanted Aliasing

To avoid unwanted aliasing with mutable objects, you can create copies:

- **Shallow Copy**: A new object with references to the original objects' elements.

  ```python
  import copy

  list1 = [1, 2, 3]
  list2 = copy.copy(list1)  # or list1[:]

  list2.append(4)
  print(list1, list2)  # Output: [1, 2, 3] [1, 2, 3, 4]
  ```

- **Deep Copy**: A new object with copies of the original object's elements and their references.

  ```python
  list1 = [[1, 2], [3, 4]]
  list2 = copy.deepcopy(list1)

  list2[0].append(3)
  print(list1, list2)  # Output: [[1, 2], [3, 4]] [[1, 2, 3], [3, 4]]
  ```

### References

For more information about aliasing and object management in Python, you can refer to the following resources:

- **Python Documentation on Data Structures**: [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- **Python Documentation on Copying**: [Python Copy Module](https://docs.python.org/3/library/copy.html)

Understanding aliasing is crucial for managing references and ensuring the correct behavior of your code, especially when working with mutable objects.
</details>



<details>
<summary>  ❓ <i>Question 17 : What is garbage collection ?</i> </summary>

***Answer :*** 
**Garbage collection** in Python is the process of automatically freeing memory by destroying objects that are no longer in use by the program. Python uses a combination of **reference counting** and a **cyclic garbage collector** to manage memory.

### Key Concepts of Garbage Collection in Python

1. **Reference Counting**:
   - **Definition**: Each object in Python has a reference count, which is the number of references pointing to the object.
   - **Mechanism**: When an object's reference count drops to zero, meaning no references to the object exist, the memory occupied by the object is deallocated.
   - **Example**:

     ```python
     a = [1, 2, 3]  # Reference count of the list object is 1
     b = a          # Reference count of the list object is 2
     del a          # Reference count of the list object is 1
     del b          # Reference count of the list object is 0, memory is deallocated
     ```

2. **Cyclic Garbage Collection**:
   - **Definition**: Handles the deallocation of objects involved in reference cycles, which reference counting alone cannot handle.
   - **Cycles**: Occur when two or more objects reference each other, creating a loop that prevents their reference counts from dropping to zero.
   - **Mechanism**: Python’s cyclic garbage collector periodically looks for groups of objects that reference each other but are not accessible from the program and deallocates them.
   - **Example**:

     ```python
     class Node:
         def __init__(self, value):
             self.value = value
             self.next = None

     a = Node(1)
     b = Node(2)
     a.next = b
     b.next = a  # Creates a cycle
     del a
     del b       # Without cyclic GC, the cycle would prevent memory from being freed
     ```

### Controlling Garbage Collection

- **`gc` Module**: Python provides the `gc` module to interact with the garbage collector.

  ```python
  import gc

  # Disable garbage collection
  gc.disable()

  # Enable garbage collection
  gc.enable()

  # Manually run garbage collection
  gc.collect()
  ```

### Practical Implications

1. **Automatic Memory Management**: Garbage collection helps developers by automatically managing memory allocation and deallocation, reducing the risk of memory leaks.
2. **Performance Considerations**: While automatic garbage collection simplifies memory management, it can introduce performance overhead. In performance-critical applications, tuning or manually invoking the garbage collector may be necessary.
3. **Cyclic References**: Understanding cyclic references and how Python handles them can help developers avoid memory leaks in complex data structures.

### Summary

- **Reference Counting**: Frees memory when an object’s reference count drops to zero.
- **Cyclic Garbage Collection**: Handles memory deallocation for reference cycles.
- **`gc` Module**: Allows interaction with the garbage collector, including manual garbage collection.

### References

For more information on garbage collection in Python:

- **Python Documentation on Memory Management**: [Python Memory Management](https://docs.python.org/3/c-api/memory.html)
- **Python `gc` Module Documentation**: [Python `gc` Module](https://docs.python.org/3/library/gc.html)

Understanding garbage collection helps in writing efficient and memory-safe Python programs.
</details>



<details>
<summary>  ❓ <i>Question 18 : What is mutability and why is it dangerous in certain scenarios ?</i> </summary>

***Answer :*** 
**Mutability** in Python refers to the ability of an object to be changed after it has been created. Objects that can be modified are called **mutable** objects, while objects that cannot be modified are called **immutable** objects.

### Mutable and Immutable Objects

#### Mutable Objects

- **Examples**: Lists, dictionaries, sets, and user-defined objects.
- **Behavior**: The contents of a mutable object can be changed after it is created without changing the object itself.

  ```python
  my_list = [1, 2, 3]
  my_list.append(4)  # my_list is now [1, 2, 3, 4]
  ```

#### Immutable Objects

- **Examples**: Integers, floats, strings, tuples, and frozensets.
- **Behavior**: Once an immutable object is created, its contents cannot be changed. Any operation that appears to modify the object will create a new object.

  ```python
  my_string = "hello"
  new_string = my_string.upper()  # new_string is "HELLO", my_string remains "hello"
  ```

### Why Mutability Can Be Dangerous

#### 1. **Unintended Side Effects**

- **Shared References**: When a mutable object is assigned to multiple variables, all variables share the same object. Modifying the object through one variable affects all other variables that reference the same object.

  ```python
  a = [1, 2, 3]
  b = a
  b.append(4)
  print(a)  # Output: [1, 2, 3, 4]
  ```

  In this example, `a` and `b` reference the same list. Modifying `b` also modifies `a`.

#### 2. **Function Arguments**

- **Mutable Defaults**: Using mutable objects as default arguments in functions can lead to unexpected behavior, as the default value is shared across all calls to the function.

  ```python
  def append_to_list(value, my_list=[]):
      my_list.append(value)
      return my_list

  print(append_to_list(1))  # Output: [1]
  print(append_to_list(2))  # Output: [1, 2]
  print(append_to_list(3))  # Output: [1, 2, 3]
  ```

  In this example, the default list `my_list` is shared across all function calls, accumulating all appended values.

#### 3. **Concurrency Issues**

- **Thread Safety**: Mutable objects can cause problems in multi-threaded programs if multiple threads modify the same object simultaneously, leading to race conditions and inconsistent states.

  ```python
  import threading

  def add_to_list(shared_list, value):
      shared_list.append(value)

  my_list = []
  threads = [threading.Thread(target=add_to_list, args=(my_list, i)) for i in range(5)]

  for thread in threads:
      thread.start()
  for thread in threads:
      thread.join()

  print(my_list)  # Output might be inconsistent due to race conditions
  ```

  In this example, concurrent modifications to `my_list` by multiple threads can lead to unexpected results.

### Best Practices to Avoid Issues with Mutability

1. **Avoid Mutable Defaults**: Use `None` as the default value and create a new mutable object within the function.

  ```python
  def append_to_list(value, my_list=None):
      if my_list is None:
          my_list = []
      my_list.append(value)
      return my_list
  ```

2. **Copying Objects**: Create copies of mutable objects to avoid unintended side effects when passing them to functions or assigning them to new variables.

  ```python
  import copy

  original_list = [1, 2, 3]
  copied_list = copy.copy(original_list)
  ```

3. **Immutability for Shared Data**: Use immutable objects for data that is shared across different parts of the program or across threads to ensure consistency.

  ```python
  shared_tuple = (1, 2, 3)
  ```

### Summary

- **Mutability**: Refers to the ability to change an object after its creation.
- **Dangerous Scenarios**: Can lead to unintended side effects, issues with default function arguments, and concurrency problems.
- **Best Practices**: Avoid mutable defaults, copy objects when necessary, and prefer immutability for shared data.

### References

For more information on mutability and best practices:

- **Python Data Structures**: [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- **Python Programming FAQ**: [Python FAQ on Mutable Default Arguments](https://docs.python.org/3/faq/programming.html#what-does-it-mean-that-python-is-a-dynamic-language)
</details>



<details>
<summary>  ❓ <i>Question 19 : What is Cloning ?</i> </summary>

***Answer :*** 

</details>



<details>
<summary>  ❓ <i>Question 20 : Differentiate between Deep and Shallow copy.</i> </summary>

***Answer :*** 
Here's a detailed comparison between **deep copy** and **shallow copy** in Python:

### Shallow Copy

#### Definition
- A shallow copy creates a new object, but inserts references into it to the objects found in the original. It only copies the top-level structure of the object, not the nested objects.

#### Characteristics
- **References**: The new object references the same elements (objects) as the original.
- **Mutability**: Changes made to the mutable objects within the copied object will reflect in the original object and vice versa.
- **Use Cases**: Suitable for copying objects that contain only immutable elements or when you need a new collection with the same elements.

#### Example

```python
import copy

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

# Modify the nested list
shallow_copied_list[2].append(5)

print("Original:", original_list)        # Output: [1, 2, [3, 4, 5]]
print("Shallow Copy:", shallow_copied_list)  # Output: [1, 2, [3, 4, 5]]
```

#### Methods to Create
1. **Using `copy` module**:
   ```python
   import copy
   shallow_copied_obj = copy.copy(original_obj)
   ```
2. **Using slicing (for lists)**:
   ```python
   shallow_copied_list = original_list[:]
   ```
3. **Using constructors**:
   ```python
   shallow_copied_list = list(original_list)
   ```

### Deep Copy

#### Definition
- A deep copy creates a new object and recursively copies all objects found in the original. It duplicates everything, including nested objects.

#### Characteristics
- **Independent Copies**: The new object and the original object are completely independent.
- **No Shared References**: Changes made to the copied object do not affect the original object and vice versa.
- **Use Cases**: Necessary when the object contains other mutable objects and you need a completely independent copy.

#### Example

```python
import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list
deep_copied_list[2].append(5)

print("Original:", original_list)        # Output: [1, 2, [3, 4]]
print("Deep Copy:", deep_copied_list)     # Output: [1, 2, [3, 4, 5]]
```

#### Methods to Create
1. **Using `copy` module**:
   ```python
   import copy
   deep_copied_obj = copy.deepcopy(original_obj)
   ```

### Comparison Table

| Feature          | Shallow Copy                           | Deep Copy                             |
|:------------------:|:----------------------------------------:|:---------------------------------------:|
| **Definition**   | Copies the top-level structure only    | Recursively copies all nested objects |
| **References**   | References same objects as original    | Creates new, independent objects      |
| **Independence** | Changes in copy affect the original if mutable | Changes in copy do not affect the original |
| **Use Cases**    | Suitable for objects with immutable elements or when shared references are desired | Suitable for objects with nested mutable elements when complete independence is required |
| **Creation**     | `copy.copy()`, slicing, constructors   | `copy.deepcopy()`                     |

### Summary
- **Shallow Copy**: Creates a new object but references the same elements (objects) as the original. Suitable for non-nested objects or when shared references are acceptable.
- **Deep Copy**: Creates a completely independent new object, duplicating all nested objects. Necessary when full independence from the original object is required.

### References
For more detailed information on copying objects in Python:
- **Python Documentation on Copying**: [Python `copy` Module](https://docs.python.org/3/library/copy.html)
- **Real Python Article on Shallow and Deep Copy**: [Understanding Shallow and Deep Copy in Python](https://realpython.com/copying-python-objects/)
</details>



<details>
<summary>  ❓ <i>Question 21 : How nested lists are stored in memory ?</i> </summary>

***Answer :*** 
Nested lists in Python are stored in memory as a series of references. Each list in Python is a dynamic array of references to other objects. When you create a nested list, each element in the outer list is a reference to another list object (the inner list). This allows Python to efficiently manage and access the elements of the nested structure.

### Memory Representation of Nested Lists

#### Example of a Nested List

Consider the following nested list:

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
```

#### Memory Layout

1. **Outer List**:
   - `nested_list` is a reference to the outer list object.
   - The outer list contains references to three inner lists: `[1, 2, 3]`, `[4, 5]`, and `[6, 7, 8, 9]`.

2. **Inner Lists**:
   - Each inner list is a separate list object.
   - Each inner list object contains references to its individual elements (integers in this case).

### Visual Representation

Here's a visual representation of how the nested list `nested_list` is stored in memory:

```
nested_list -> [ Ref1, Ref2, Ref3 ]
               |      |      |
               v      v      v
             [1, 2, 3] [4, 5] [6, 7, 8, 9]
              |  |  |   |  |   |  |  |  |
              v  v  v   v  v   v  v  v  v
              1  2  3   4  5   6  7  8  9
```

- `Ref1`, `Ref2`, and `Ref3` are references to the inner lists.
- Each inner list contains references to its elements.

### Detailed Breakdown

1. **Outer List Object**:
   - The outer list object contains references (`Ref1`, `Ref2`, `Ref3`) to the inner lists.
   - The outer list itself is an array of pointers.

2. **Inner List Objects**:
   - Each inner list object (`[1, 2, 3]`, `[4, 5]`, `[6, 7, 8, 9]`) contains references to its elements (integers in this case).
   - These inner list objects are also arrays of pointers, but they point to integer objects.

3. **Element Objects**:
   - The individual integers (`1, 2, 3, 4, 5, 6, 7, 8, 9`) are stored as separate objects in memory.
   - The inner lists contain references to these integer objects.

### Implications

- **Efficient Access**: Accessing an element in a nested list involves following references, which is efficient due to Python's dynamic array implementation.
- **Shared References**: If multiple lists (inner lists) contain references to the same object, modifying that object through one list will affect the other lists as well.

  ```python
  a = [1, 2, 3]
  b = [a, a, a]
  b[0][0] = 10
  print(a)  # Output: [10, 2, 3]
  print(b)  # Output: [[10, 2, 3], [10, 2, 3], [10, 2, 3]]
  ```

- **Memory Usage**: Nested lists can lead to increased memory usage due to the overhead of storing multiple references, especially for large and deeply nested structures.

### Summary

- **Nested Lists**: Stored as lists of references, with each level of nesting involving additional references.
- **Efficiency**: Provides efficient access to elements through references.
- **Shared References**: Changes to shared objects affect all references, which can lead to unintended side effects.

### References

For more information on how Python handles lists and memory management:

- **Python Documentation on Data Structures**: [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- **Python's Memory Management and Object Model**: [Python Memory Management](https://realpython.com/python-memory-management/)
</details>



<details>
<summary>  ❓ <i>Question 22 : Why tuples take less memory than lists ?</i> </summary>

***Answer :*** 
Tuples in Python take less memory than lists primarily due to their immutability and simpler internal structure. Here are the key reasons:

### 1. Immutability

- **Tuples** are immutable, meaning that once they are created, their contents cannot be changed. This immutability allows Python to optimize their storage.
- **Lists**, on the other hand, are mutable and can be modified after creation, which requires more complex data structures to handle dynamic changes.

### 2. Internal Structure

- **Fixed Size**: Since tuples cannot be changed, Python can allocate a fixed amount of memory for them. This allows tuples to be stored more compactly.
- **No Extra Space for Modification**: Lists need to allocate extra space to accommodate potential modifications (like adding or removing elements). This extra space leads to additional memory overhead.

### 3. Overhead of Dynamic Arrays

- **Lists**: Python lists are implemented as dynamic arrays, which means they need to manage resizing when elements are added or removed. This requires additional memory for bookkeeping, such as maintaining a capacity and resizing when necessary.
- **Tuples**: Tuples do not need to manage resizing since they are fixed in size. This reduces the overhead associated with dynamic arrays.

### 4. Memory Overhead

- **Lists**: Each list in Python has a header that includes information about its size, capacity, and references to the elements. This header takes up additional memory.
- **Tuples**: Tuples have a simpler header since they do not need to manage capacity (only the size). This results in a smaller memory footprint.

### Example of Memory Usage

You can observe the difference in memory usage using the `sys` module:

```python
import sys

list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print("List size:", sys.getsizeof(list_example))  # Output: List size: 96 (value may vary)
print("Tuple size:", sys.getsizeof(tuple_example))  # Output: Tuple size: 80 (value may vary)
```

In this example, `sys.getsizeof` shows the memory size of a list and a tuple with the same contents. Typically, the tuple will have a smaller size due to the reasons mentioned above.

### Detailed Breakdown of Memory Usage

- **List**:
  - Header includes size, capacity, and reference count.
  - Each element has a reference to the actual data.
  - Additional memory for capacity to handle dynamic resizing.

- **Tuple**:
  - Header includes size and reference count.
  - Fixed-size array of references to elements.
  - No extra memory for capacity or resizing.

### Summary

- **Tuples**:
  - Immutable
  - Fixed-size
  - Simpler internal structure
  - Less memory overhead
- **Lists**:
  - Mutable
  - Dynamic-size
  - More complex internal structure
  - Additional memory overhead for resizing and capacity management

### References

For more details on memory management and data structures in Python:

- **Python Documentation on Data Structures**: [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- **Understanding Python's Memory Management**: [Real Python: Python Memory Management](https://realpython.com/python-memory-management/)
</details>



<!-- <details>
<summary>  ❓ <i>Question X : </i> </summary>

***Answer :*** 

</details> -->