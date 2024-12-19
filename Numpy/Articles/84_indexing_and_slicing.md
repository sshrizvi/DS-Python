# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> NumPy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Useful Numpy Methods](/Numpy/Articles/83_numpy_methods.md)

## Indexing and Slicing

### Indexing
- NumPy array indexing is a rich topic, as there are many ways you may want to select a subset of your data or individual elements.

#### 1D Array Indexing
- Indexing in one-dimensional arrays is simple. It is same like as indexing done in *Lists of Python*.
- **Syntax**
  ```python
  array_name[index]
  ```
- **Example**
  ```python
  import numpy as np
  a = np.arange(10)**3
  print(a)
  print(a[1])
  ```
- **Output**
  ```bash
  [  0   1   8  27  64 125 216 343 512 729] # a (Array)
  1 # a[1] - Element in `a` at index `1`
  ```

#### 2D Array Indexing
- Indexing in two-dimensional arrays is simpler as compared to *Tensors* (arrays having more than 2 dimensions). It is same like as indexing done in *Matrices*.
- **Syntax**
  ```python
  array_name[row_index, column_index]
  ```
- **Example**
  ```python
  def f(x, y):
    return 10 * x + y

  b = np.fromfunction(f, (5, 4), dtype=int)
  print(b)
  print(b[2,3])
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [10 11 12 13]
   [20 21 22 23]
   [30 31 32 33]
   [40 41 42 43]] # a (Array)

  23 # a[2,3] Element at 2th row and 3rd column
  ```
- We can also access a one-dimensional array that is in the 2D array by something like that.
- **Example**
  ```python
  def f(x, y):
    return 10 * x + y

  b = np.fromfunction(f, (5, 4), dtype=int)
  print(b)
  print(b[2])
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [10 11 12 13]
   [20 21 22 23]
   [30 31 32 33]
   [40 41 42 43]] # a (Array)

  [20 21 22 23] # a[2] 1D array at index `2`
  ```

#### 3D Array Indexing
- Indexing in 3D array (a.k.a Tensor) is a bit complex as compared to a 1D array (a.k.a Vector) and a 2D array (a.k.a Matrix). Since, it has 3 dimensions, therfore the syntax of indexing goes like this.
- **Syntax**
  ```python
  tensor_name[stacked_array_index, row_index, column_index]
  ```
- **Example**
  ```python
  c = np.array([[[0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
  print(c)
  print(c[1, 1, 1])
  ```
- **Output**
  ```bash
  [[[  0   1   2]
    [ 10  12  13]]

   [[100 101 102]
    [110 112 113]]] # c (3D Array)
  
  112 # c[1,1,1] Element in 1st Matrix's 1st row and 1st column 
  ```

> [!TIP]
> In the same manner, we can generalize the indexing for multidimensional arrays like, 4D, 5D and so on.

### Slicing
- Slicing is very similar to Indexing. Slicing, here, is just like slicing done in lists in Python.
- The syntax of slicing is something like `starting_range : ending_range`.
- All we need to do is to replace the `indexes` with the `slicing syntax`, that's it.
- Theoretically speaking, slicing takes the power of indexing to another level. It helps the programmer to access elements of any choice from the array.

#### 1D Array Slicing
- Slicing in one-dimensional array is very similar to slicing in *Lists in Python*.
- **Example**
  ```python
  a = np.arange(10)**3
  print(a)
  print(a[2:5])
  ```
- **Output**
  ```bash
  [  0   1   8  27  64 125 216 343 512 729] # a (Array)
  
  [ 8 27 64] # Elements from the index `2` (starting range) to index `4` (ending range - 1) 
  ```
- In case, we do not want to give a starting range, then we can leave it blank and by default the starting range will be assigned the index `0`.
- **Example**
  ```python
  a = np.arange(10)**3
  print(a)
  print(a[:5])
  ```
- **Output**
  ```bash
  [  0   1   8  27  64 125 216 343 512 729] # a (Array)
  
  [ 0  1  8 27 64] # Elements from the index `0` (starting range) to index `4` (ending range - 1) 
  ```
- In case, we do not want to give the ending range, then we can leave it blank and by default the ending range will be assigned the size of the array in case of 1D array i.e., `array.size`.
- **Example**
  ```python
  a = np.arange(10)**3
  print(a)
  print(a[2:])
  ```
- **Output**
  ```bash
  [  0   1   8  27  64 125 216 343 512 729] # a (Array)
  
  [  8  27  64 125 216 343 512 729] # Elements from the index `2` (starting range) to index `9` (ending range - 1) 
  ```

#### 2D Array Slicing
- Slicing in 2D arrays (matrices) becomes easier if we try to generalize the slicing concept used in 1D arrays (vectors).
- In 2D arrays, there are rows and columns, which are going to be replaced by the slicing syntax `starting_range : ending_range`.
- **Example**
  ```python
  def f(x, y):
    return 10 * x + y
  b = np.fromfunction(f, (5, 4), dtype=int)
  print(b)
  print(b[1:3, 2:4])
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [10 11 12 13]
   [20 21 22 23]
   [30 31 32 33]
   [40 41 42 43]] # b (Array)

  [[12 13]
   [22 23]] # b[1:3, 2:4] - Returns elements that are in rows 1,2 AND are also in columns 2,4.
  ```
- Likewise, as in 1D arrays , we can also leave starting and ending ranges blank, and the default will be assigned for the same.

#### 3D Array Slicing
- Slicing in 3D arrays (tensors) also becomes easier, if we try to generalize the concepts of slicing from 2D arrays (matrices).
- In a 3D array, ofcourse, there are three dimensions, where each one of them can be replaced with the slicing syntax `starting_range : ending_range`.
- **Example**
  ```python
  c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
                 [ 10, 12, 13]],
                [[100, 101, 102],
                 [110, 112, 113]]])
  print(c[1, :, :])
  ```
- **Output**
  ```bash
  [[100 101 102]
   [110 112 113]] # Elements from all rows and columns of 1st 2D array
  ```

> [!TIP]  
> Link to Next Article  
> 🡺 [Iterating Arrays and More](/Numpy/Articles/85_iterating_arrays_and_more.md)