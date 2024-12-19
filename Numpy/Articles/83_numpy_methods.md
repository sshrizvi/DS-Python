# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> Numpy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Numpy Array Operations](/Numpy/Articles/82_operations_on_numpy_arrays.md)

## Useful Numpy Methods
- There are numerous amount of methods available in the NumPy.
- I am going to discuss selective and useful methods in this article. Rest of the methods can be seen in the official NumPy's documentation.

### 1. `numpy.max()`
- It returns the *maximum element* from the array.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.max(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
   11 # maximum element
  ```
- In case, we want to find *maximum element in every column* and *maximum element in every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.max(a, axis=0))
  print(np.max(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [ 8  9 10 11] # ColumnWise Maximum

  [ 3  7 11] # RowWise Maximum
  ```

### 2. `numpy.min()`
- It returns the *minimum element* from the array.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.min(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
   0 # minimum element
  ```
- In case, we want to find *minimum element in every column* and *minimum element in every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.min(a, axis=0))
  print(np.min(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [0 1 2 3] # ColumnWise Minimum

  [0 4 8] # RowWise Minimum
  ```

### 3. `numpy.sum()`
- It returns the *sum of the elements* of the array.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.sum(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
   66 # sum
  ```
- In case, we want to find *sum of every column* and *sum of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.sum(a, axis=0))
  print(np.sum(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [12 15 18 21] # ColumnWise Sum

  [6 22 38] # RowWise Sum
  ```

### 4. `numpy.prod()`
- It returns the *product of the elements* of the array.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.prod(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
   0 # product
  ```
- In case, we want to find *product of every column* and *product of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.prod(a, axis=0))
  print(np.prod(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [0 45 120 231] # ColumnWise Product

  [0 840 7920] # RowWise Product
  ```

### 5. `numpy.mean()`
- It returns the *mean of the elements* of the array.
- **Example**
  ```python
  a = np.arange(1,6)
  print(a)
  print(np.mean(a))
  ```
- **Output**
  ```bash
  [1 2 3 4 5] # a (Array)
  3.0 # Mean
  ```
- In case, we want to find *mean of every column* and *mean of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.mean(a, axis=0))
  print(np.mean(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [4. 5. 6. 7.] # ColumnWise Mean

  [1.5 5.5 9.5] # RowWise Mean
  ```

### 5. `numpy.median()`
- It returns the *median of the elements* of the array.
- **Example**
  ```python
  a = np.arange(1,6)
  print(a)
  print(np.median(a))
  ```
- **Output**
  ```bash
  [1 2 3 4 5] # a (Array)
  3.0 # median
  ```
- In case, we want to find *median of every column* and *median of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.median(a, axis=0))
  print(np.median(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [4. 5. 6. 7.] # ColumnWise Median

  [1.5 5.5 9.5] # RowWise Median
  ```


### 6. `numpy.std()`
- It returns the *standard deviation of the elements* of the array.
- **Example**
  ```python
  a = np.arange(1,6)
  print(a)
  print(np.std(a))
  ```
- **Output**
  ```bash
  [1 2 3 4 5] # a (Array)
  1.4142135623730951 # Standard Deviation
  ```
- In case, we want to find *standard deviation of every column* and *standard deviation of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.std(a, axis=0))
  print(np.std(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [3.26598632 3.26598632 3.26598632 3.26598632] # ColumnWise Standard Deviation

  [1.11803399 1.11803399 1.11803399] # RowWise Standard Deviation
  ```

### 7. `numpy.var()`
- It returns the *variance of the elements* of the array.
- **Example**
  ```python
  a = np.arange(1,6)
  print(a)
  print(np.var(a))
  ```
- **Output**
  ```bash
  [1 2 3 4 5] # a (Array)
  2.0 # variance
  ```
- In case, we want to find *variance of every column* and *variance of every row*, then we can use the `axis` parameter.
  - For column - `axis = 0`
  - For row - `axis = 1`
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.std(a, axis=0))
  print(np.std(a, axis=1))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)

  [10.66666667 10.66666667 10.66666667 10.66666667] # ColumnWise Standard Deviation

  [1.25 1.25 1.25] # RowWise Standard Deviation
  ```

### 8. `numpy.dot()`
- It takes two matrices as arguments and returns the dot product of it.
- The dot product here means the matrix multiplication of two matrices.
- **Example**
  ```python
  a = np.arange(4).reshape((2,2))
  b = np.arange(4).reshape((2,2))
  print(a)
  print(b)
  print(np.dot(a, b))
  ```
- **Output**
  ```bash
  [[0 1]
   [2 3]] # a (Array)

  [[0 1]
   [2 3]] # b (Array)

  [[ 2,  3],
   [ 6, 11]] # np.dot(a,b)
  ```

> [!CAUTION]  
> Keep in mind that the shape of the argument arrays needs to be aligned for matrix multiplication.  
> $$No. of Columns In First Matrix = No. of Rows In Second Matrix$$

- **Example**
  ```python
  a = np.arange(4).reshape((2,2))
  b = np.arange(4).reshape((1,4))
  print(a)
  print(b)
  print(np.dot(a, b))
  ```
- **Output**
  ```bash
  [[0 1]
   [2 3]] # a (Array)

  [[0 1 2 3]] # b (Array)

  ValueError: shapes (2,2) and (1,4) not aligned: 2 (dim 1) != 1 (dim 0)
  ```
- Here, the error occurs as the shape of the argument arrays is not same.

### 8. `numpy.log()`
- It returns an `ndarray` of natural logarithm, *element-wise*.
- The natural logarithm $log$ is the inverse of the exponential function, so that $log(exp(x)) = x$. The natural logarithm is logarithm in base $e$.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.log(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
  [[      -inf 0.         0.69314718 1.09861229]
   [1.38629436 1.60943791 1.79175947 1.94591015]
   [2.07944154 2.19722458 2.30258509 2.39789527]] # np.log(a)
  ```

### 9. `numpy.exp()`
- It calculates the exponential of all elements in the input array.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(np.exp(a))
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a (Array)
   
  [[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01]
   [5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03]
   [2.98095799e+03 8.10308393e+03 2.20264658e+04 5.98741417e+04]] # np.log(a)
  ```

### 10. `numpy.round()`
- It evenly rounds to the given number of decimals.
- **Example**
  ```python
  a = np.linspace(0, 2, 9).reshape((3,3))
  print(a)
  print(np.round(a))
  ```
- **Output**
  ```bash
  [[0.   0.25 0.5 ]
   [0.75 1.   1.25]
   [1.5  1.75 2.  ]] # a (Array)
   
  [[0. 0. 0.]
   [1. 1. 1.]
   [2. 2. 2.]] # np.round(a)
  ```

### 11. `numpy.ceil()`
- It returns the ceiling of the input, element-wise.
- The ceil of the scalar `x` is the smallest integer `i`, such that `i >= x`. It is often denoted as $\left\lceil x \right\rceil$.
- **Example**
  ```python
  a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
  print(np.ceil(a))
  ```
- **Output**
  ```bash
  [-1. -1. -0.  1.  2.  2.  2.] # np.ceil(a)
  ```

### 12. `numpy.floor()`
- It returns the *floor* of the input, *element-wise*.
- The floor of the scalar `x` is the largest integer `i`, such that `i <= x`. It is often denoted as $\left\lfloor x \right\rfloor$.
- **Example**
  ```python
  a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
  print(np.floor(a))
  ```
- **Output**
  ```bash
  [-2., -2., -1.,  0.,  1.,  1.,  2.] # np.floor(a)
  ```


> [!TIP]
> It is advised not to learn all these methods of numpy, as there are numerous of them available for specific purposes. Hence, try focusing on concepts rather than mugging up. We will google methods when we have the usecase.

> [!TIP]  
> Link to Next Article  
> 🡺 [Indexing and Slicing](/Numpy/Articles/84_indexing_and_slicing.md)