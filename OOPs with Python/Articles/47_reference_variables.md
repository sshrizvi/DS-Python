# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Accessing Attributes of a Class Using Objects](/OOPs%20with%20Python/Articles/46_accessing_attributes.md)

### What is a Reference Variable in Python?

In Python, a reference variable is essentially a name that refers to a value or an object stored in memory. Unlike some other programming languages where variables hold actual data, Python variables act as references or pointers to objects. This concept is central to understanding how Python handles data, memory management, and object manipulation.

#### How Reference Variables Work with Objects

When you create an object in Python and assign it to a variable, the variable does not hold the object itself. Instead, it holds a reference to the object. This reference is like a pointer that tells Python where the actual object is stored in memory.

##### Example:

```python
# Creating an object (list) and assigning it to a variable
my_list = [1, 2, 3]

# my_list now refers to the list object in memory
```

In the example above, `my_list` is not storing the list `[1, 2, 3]` directly. Instead, it's storing a reference to where that list is located in memory.

#### Tricky Examples

1. **Multiple References to the Same Object:**

   ```python
   a = [1, 2, 3]
   b = a  # b now refers to the same list as a

   b.append(4)

   print(a)  # Output: [1, 2, 3, 4]
   print(b)  # Output: [1, 2, 3, 4]
   ```

   Here, both `a` and `b` refer to the same list object. When you modify the list using `b`, it also affects `a` because both variables point to the same object in memory.

2. **Reference Behavior in Functions:**

   ```python
   def modify_list(lst):
       lst.append(4)

   my_list = [1, 2, 3]
   modify_list(my_list)

   print(my_list)  # Output: [1, 2, 3, 4]
   ```

   In this case, the list passed to the function is modified because the function operates on the reference to the original list. Thus, the changes persist even outside the function.

3. **Rebinding Variables:**

   ```python
   x = [1, 2, 3]
   y = x  # y refers to the same list as x

   x = [4, 5, 6]  # x now refers to a new list

   print(x)  # Output: [4, 5, 6]
   print(y)  # Output: [1, 2, 3]
   ```

   Here, when `x` is reassigned to a new list, `y` still refers to the original list. This is because rebinding `x` doesn’t affect `y`; it only changes what `x` points to.

#### Key Points for Understanding Reference Variables:

1. **Immutability:** 
   - In the case of immutable objects (like integers, strings, and tuples), any operation that modifies the value will create a new object, and the reference will be updated to point to this new object.
   
   ```python
   a = 10
   b = a
   a = 20

   print(a)  # Output: 20
   print(b)  # Output: 10
   ```

   - Here, `a` was first pointing to `10`. When `a` is reassigned to `20`, a new integer object is created, and `a` now points to this new object. `b` still refers to the original integer object `10`.

2. **Mutability:**
   - Mutable objects like lists or dictionaries can be modified in place. Therefore, if multiple variables refer to the same object, changes made through one variable will reflect in all others.
  
   ```python
   dict_a = {'key': 'value'}
   dict_b = dict_a

   dict_b['new_key'] = 'new_value'

   print(dict_a)  # Output: {'key': 'value', 'new_key': 'new_value'}
   print(dict_b)  # Output: {'key': 'value', 'new_key': 'new_value'}
   ```

3. **Aliasing:**
   - When two or more variables refer to the same object, they are said to be "aliases." Changes made via one alias affect the object and are visible to all other aliases.

   ```python
   a = [1, 2, 3]
   b = a
   c = a

   c.append(4)

   print(a)  # Output: [1, 2, 3, 4]
   print(b)  # Output: [1, 2, 3, 4]
   print(c)  # Output: [1, 2, 3, 4]
   ```

Understanding reference variables is crucial for effective memory management, debugging, and avoiding unintended side effects in Python programs.

> [!TIP]  
> Link to Next Article  
> 🡺 [Pass by Value and Pass by Reference in Python](/OOPs%20with%20Python/Articles/48_pass_by_value_and_reference.md)