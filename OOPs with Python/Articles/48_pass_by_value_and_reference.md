# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Accessing Attributes of a Class Using Objects](/OOPs%20with%20Python/Articles/46_accessing_attributes.md)

### Pass by Value and Pass by Reference in Python

When discussing function arguments, terms like "pass by value" and "pass by reference" often come up. These terms describe how arguments are passed to functions and how modifications to those arguments inside the function affect the original variables outside the function.

#### **Pass by Value vs. Pass by Reference:**
- **Pass by Value:** 
  - In languages that use pass by value, a copy of the argument's value is passed to the function. Any modifications to the parameter inside the function do not affect the original argument outside the function.
  
- **Pass by Reference:** 
  - In languages that use pass by reference, the reference (or address) of the argument is passed to the function. Therefore, any changes to the parameter inside the function directly affect the original argument outside the function.

#### **Python’s Argument Passing Mechanism:**
Python’s argument passing mechanism doesn’t neatly fall into either pass by value or pass by reference. Instead, Python uses a concept known as **“pass by object reference”** or **“pass by assignment.”** 

- When you pass a mutable object (like a list or a dictionary) to a function, the function receives a reference to the object. Any modifications made to the object inside the function will affect the original object.
- When you pass an immutable object (like an integer, string, or tuple) to a function, the function receives a reference to the object, but since the object is immutable, any modifications will result in a new object being created. The original object remains unchanged.

#### **Examples and Warnings:**

1. **Mutable Objects (e.g., Lists) - Behavior Similar to Pass by Reference:**

    ```python
    def modify_list(lst):
        lst.append(4)

    my_list = [1, 2, 3]
    modify_list(my_list)
    print(my_list)  # Output: [1, 2, 3, 4]
    ```

    - **Explanation:** Here, `my_list` is a list (a mutable object). When passed to `modify_list`, the list is modified in place, and these changes are reflected in the original list outside the function.

    - **Warning:** If you want to avoid modifying the original list, you should pass a copy of the list instead of the original.

    ```python
    modify_list(my_list[:])  # Passing a copy of the list
    ```

2. **Immutable Objects (e.g., Integers) - Behavior Similar to Pass by Value:**

    ```python
    def modify_number(num):
        num += 10
        print("Inside function:", num)

    my_num = 5
    modify_number(my_num)
    print("Outside function:", my_num)  # Output: 5
    ```

    - **Explanation:** Here, `my_num` is an integer (an immutable object). Inside the function, `num` is modified by creating a new integer object. However, this change does not affect `my_num` outside the function.

    - **Warning:** Although the variable inside the function is modified, this change does not propagate back to the original variable outside the function, which can lead to unexpected results if not properly understood.

3. **Mixing Mutable and Immutable - A Common Pitfall:**

    ```python
    def modify_elements(elements, number):
        elements.append(number)
        number += 10

    nums = [1, 2, 3]
    num = 5

    modify_elements(nums, num)
    print(nums)  # Output: [1, 2, 3, 5]
    print(num)   # Output: 5
    ```

    - **Explanation:** The list `nums` is modified because lists are mutable. However, `num`, being an integer, remains unchanged outside the function because it is immutable.

    - **Warning:** When working with functions that modify both mutable and immutable objects, be cautious about how each type of object behaves inside and outside the function.

#### **Conclusion:**
Python’s model of passing arguments is best described as “pass by object reference.” Understanding how Python handles mutable and immutable objects is crucial for effective function design and avoiding common pitfalls. When in doubt, remember that mutable objects like lists and dictionaries can be changed in place, while immutable objects like integers and strings cannot be modified, leading to the creation of new objects instead.

> [!TIP]  
> Link to Next Article  
> 🡺 [Making User-Defined Classes Immutable in Python](/OOPs%20with%20Python/Articles/49_creating_immutable_datatypes.md)