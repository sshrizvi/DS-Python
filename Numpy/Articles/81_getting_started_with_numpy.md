# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> Numpy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [NumPy - An Introduction](/Numpy/Articles/80_numpy.md)

## Getting Started with Numpy

### The Basics
- NumPy's main object is the *homogeneous multidimensional array.*
- It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.
- In NumPy *dimensions* are called *axes*.
- > **Example**  
  > - `[1,2,3]` has `1` axes, as it is a 1D array.
  > - `[[1., 0., 0.], [0., 1., 2.]]` has `2` axes, as it is a 2D array.
- NumPy's array class is called `ndarray`.
- It is also known by the alias `array`.
- Note that `numpy.array` is not the same as the Standard Python Library class `array.array`, which only handles one-dimensional arrays and offers less functionality.

### Attributes of `ndarray` Object
1. `ndarray.ndim`  
   It returns the *number of axes* (dimensions) of the array.  
   **Example**  
   ```python
   import numpy as np
   arr = nd.array([1,2,3])
   print(arr.ndim)
   ```
   **Output**  
   ```bash
   1
   ```
2. `ndarray.shape`  
   - It return the the dimensions of the array.  
   -  This is a tuple of integers indicating the size of the array in each dimension.
   -  For a matrix with *n* rows and *m* columns, `shape` will be `(n,m)`. The length of the `shape` tuple is therefore the number of axes, `ndim`.  
   - **Example**  
        ```python
        import numpy as np
        arr = nd.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
        print(arr.shape)
        ```  
   - **Output**  
        ```bash
        (3,3) # 3 rows and 3 columns
        ```
3. `ndarray.size`  
   It returns the *total number of elements* of the array. This is equal to the *product of the elements of `shape`*.  
   **Example**  
   ```python
    arr = nd.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
    print(arr.size)
   ```
   **Output**  
   ```bash
   9
   ```
4. `ndarray.itemsize`  
   It returns the *size in bytes of each element* of the array. For example, an array of elements of type `float64` has `itemsize` 8 (=64/8), while one of type `complex32` has `itemsize` 4 (=32/8). It is equivalent to `ndarray.dtype.itemsize`.  
   **Example**  
   ```python
    a = np.array([[ 0,  1,  2,  3,  4],
                  [ 5,  6,  7,  8,  9],
                  [10, 11, 12, 13, 14]])
    print(a.itemsize)
   ```  
   **Output**  
   ```bash
    8   # 8 Bytes
   ```
5. `ndarray.dtype`  
   It returns an object describing the *type of the elements* in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.  
   **Example**  
   ```python
    a = np.array([[ 0,  1,  2,  3,  4],
                  [ 5,  6,  7,  8,  9],
                  [10, 11, 12, 13, 14]])
    print(a.dtype)
   ```  
   **Output**  
   ```bash
    int64
   ```
6. `ndarray.data`  
   It returns the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.

### Creating an Array  
#### 1. Using `np.array()` Function
- You can create an array from a regular Python *list* or *tuple* using the `array` function.
- The `type` of the resulting array is *deduced from* the `type` of the elements in the sequences.
- **Example**  
  ```python
    import numpy as np
    a = np.array([2, 3, 4])
    b = np.array([1.2, 3.5, 5.1])
    print(a)
    print(b)
  ```
- **Output**  
  ```bash
    [2, 3, 4]
    [1.2, 3.5, 5.1]
  ```
- `array` transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.
- **Example**  
  ```python
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b)
  ```
- **Output**  
  ```bash
    [[1.5, 2. , 3. ],
     [4. , 5. , 6. ]]
  ```
- The type of the array can also be explicitly specified at creation time.
- **Example**  
  ```python
    c = np.array([[1, 2], [3, 4]], dtype=complex)
    print(c)
  ```
- **Output**  
  ```bash
    [[1.+0.j, 2.+0.j],
     [3.+0.j, 4.+0.j]]
  ```
> [!TIP]  
> Documentation Link : 
> [numpy.array()](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

#### 2. Using `np.zeros()` Function  
- The function `zeros` creates an array full of zeros.
- **Example**  
  ```python
    d = np.zeros((3, 4))
    print(d)
  ```
- **Output**  
  ```bash
    [[0., 0., 0., 0.],
     [0., 0., 0., 0.],
     [0., 0., 0., 0.]]
  ```

#### 3. Using `np.ones()` Function  
- The function `ones` creates an array full of ones.
- **Example**  
  ```python
    e = np.ones((2, 3, 4), dtype=np.int16)
    print(e)
  ```
- **Output**  
  ```bash
    [[[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],

     [[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]]
  ```

#### 4. Using `np.empty()` Function  
- The function `empty` creates an array whose initial content is *random* and depends on the state of the memory.
- **Example**  
  ```python
    f = np.empty((2, 3))
    print(f)
  ```
- **Output**  
  ```bash
    [[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
     [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]]
  ```

> [!CAUTION]
> By default, the `dtype` of the created array is `float64`, but it can be specified via the keyword argument `dtype`.

#### 5. Using `np.arange()` Function
- To create sequences of numbers, ***NumPy*** provides the `arange` function which is *analogous to the Python built-in* `range`, *but returns an array*.
- **Example**  
  ```python
    g = np.arange(10, 30, 5)
    print(g)
  ```
- **Output**  
  ```bash
    [10, 15, 20, 25]
  ```
- Here, in the above example:
  - The first and second argument determines the range of the elements to be taken in the array.
  - The third argument determines the step to be taken from the starting range.
> [!CAUTION]
> When `arange` is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function `linspace` that receives as an argument ***the number of elements*** that we want, instead of the step.

#### 6. Using `np.linspace()` Function
- When `arange` is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function `linspace` that receives as an argument ***the number of elements*** that we want, instead of the step.
- **Example**  
  ```python
    h = np.linspace(0, 2, 9)
    print(h)
  ```
- **Output**  
  ```bash
    [0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ]
  ```
- Here, in the above example: 
  - First Argument - Starting Element of Array
  - Second Argument - Last Element of Array
  - Third Argument - Number of elements that we want.
- Hence, the `linspace` function automatically determines the step to be taken to acheive the number of elements that we want.


#### 7. Using `np.identity()` Function
- It returns the identity array.
- The identity array is a square array with ones on the main diagonal.
- - **Example**  
  ```python
    i = np.identity(3)
    print(i)
  ```
- **Output**  
  ```bash
    [[1.,  0.,  0.],
     [0.,  1.,  0.],
     [0.,  0.,  1.]]
  ```

#### 8. Using `np.random.random()` Function
- It returns random floats in the half-open interval $[0.0, 1.0)$.
- **Example**  
  ```python
    r = np.random.random((2,4))
    print(r)
  ```
- **Output**  
  ```bash
    [[ 0.95423066  0.35595927  0.76048569  0.90163066],
     [ 0.41903408  0.85596254  0.21666156  0.05734769]]
    # May Vary
  ```


> [!TIP]  
> Link to Next Article  
> 🡺 [Numpy Array Operations](/Numpy/Articles/82_operations_on_numpy_arrays.md)