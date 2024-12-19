# <picture> <source srcset="https://numpy.org/images/logo.svg" type="image/webp"> <img src="https://numpy.org/images/logo.svg" width="32" height="32"> </picture> Numpy for Data Science 

> [!TIP]  
> Link to Previous Article  
> 🡸 [Getting Started with Numpy](/Numpy/Articles/81_getting_started_with_numpy.md)

## Numpy Array Operations

### Scalar Array Operations
- Here, the array is operated with a scalar quantity, like a number.
### Arithmetic Operations
- Arithmetic Operators on arrays apply *element-wise*.
- A new array is created and filled with the result.
#### 1. Addition of a Scalar to Array
- It adds the scalar quantity to every element of the array.
- **Example**  
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a + 5)
  ```
- **Output**  
  ```bash
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]] # Original Array (a)

  [[ 5,  6,  7,  8],
   [ 9, 10, 11, 12],
   [13, 14, 15, 16]] # New Array (a + 5)
  ```
- Here, the scalar quantity `5` is added to first element of array `0`, then to the second element of array `1`, then to the third element of array `2`, and so on till the last element of the array.

#### 2. Subtraction of a Scalar from an Array
- It subtracts the scalar quantity from every element of the array.
- **Example**  
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a - 5)
  ```
- **Output**  
  ```bash
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]] # Original Array (a)

  [[-5, -4, -3, -2],
   [-1,  0,  1,  2],
   [ 3,  4,  5,  6]] # New Array (a - 5)
  ```
- Here, the scalar quantity `5` is subtracted from the first element of array `0`, then from the second element of array `1`, then from the third element of array `2`, and so on till the last element of the array.

#### 3. Multiplication of a Scalar to an Array
- It multiplies the scalar quantity to every element of the array.
- **Example**  
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a * 5)
  ```
- **Output**  
  ```bash
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]] # Original Array (a)

  [[ 0,  5, 10, 15],
   [20, 25, 30, 35],
   [40, 45, 50, 55]] # New Array (a * 5)
  ```
- Here, the scalar quantity `5` is multiplied to the first element of array `0`, then to the second element of array `1`, then to the third element of array `2`, and so on till the last element of the array.

#### 4. Division of an Array by a Scalar
- It divides every element of an array by the scalar quantity.
- **Example**  
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a / 5)
  ```
- **Output**  
  ```bash
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]] # Original Array (a)

  [[0. , 0.2, 0.4, 0.6],
   [0.8, 1. , 1.2, 1.4],
   [1.6, 1.8, 2. , 2.2]] # New Array (a / 5)
  ```
- Here, the first element of the array `0` is divided by the scalar quantity, then second element of the array `1` is divided, then third element of the array `2` is divided, and so on till the last element of the array.

#### 5. Raising Power of Elements of an Array
- It raises the power of every element of the array to the scalar quantity.
- **Example**  
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a ** 5)
  ```
- **Output**  
  ```bash
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]] # Original Array (a)

  [[     0,      1,     32,    243],
   [  1024,   3125,   7776,  16807],
   [ 32768,  59049, 100000, 161051]] # New Array (a ** 5)
  ```
- Here, the first element of the array `0` is raised to the power of `5`, then second element of the array `1` is raised to the power of `5`, then the third element of array `2` is raised to the power of `5`, and so on till the last element of the array.

### Relational Operations
- Relational Operators on arrays apply *element-wise*.
- A new *boolean* array is created and filled with the result.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  print(a)
  print(a < 5)
  ```
- **Output**
  ```bash
  [[ True,  True,  True,  True],
   [ True, False, False, False],
   [False, False, False, False]]
  ```
- Here, the first element of the array `0` is compared with `5`, then second element of the array `1` is compared with `5`, then the third element of the array `2` is compared with `5`, and so on till the last element of the array.
- A new *boolean* array is created with new values according to the conditions.
- In the same manner, we can use other relational operators as well.


### Vector Array Operations
- Here, the array is operated with another array, which is ofcourse of the same shape as of the first.

#### 1. Addition of Two Arrays
- The addition operation is applied *element-wise* between the two arrays.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  b = np.arange(12, 24).reshape((3,4))
  print(a)
  print(b)
  print(a + b)
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]] # b

  [[12, 14, 16, 18],
   [20, 22, 24, 26],
   [28, 30, 32, 34]] # a + b
  ```
- Here, the corresponding element of the two arrays are added, and a new array with new added values is created.
- In depth, the first element of `a` is added to the first element of `b`, then the second element of `a` is added to the second element of `b`, then the third element of `a` is added to the third element of `b`, and so on till the last element of the arrays.

#### 2. Subtraction of Two Arrays
- The subtraction operation is applied *element-wise* between the two arrays.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  b = np.arange(12, 24).reshape((3,4))
  print(a)
  print(b)
  print(a - b)
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]] # b

  [[-12, -12, -12, -12],
   [-12, -12, -12, -12],
   [-12, -12, -12, -12]] # a - b
  ```
- Here, the corresponding element of the two arrays are subtracted, and a new array with new subtracted values is created.
- In depth, the first element of `b` is subtracted from the first element of `a`, then the second element of `b` is subtracted from the second element of `a`, then the third element of `b` is subtracted from the third element of `a`, and so on till the last element of the arrays.

#### 3. Product of Two Arrays
- The multiplication operation is applied *element-wise* between the two arrays.
- **Example**
  ```python
  a = np.arange(12).reshape((3,4))
  b = np.arange(12, 24).reshape((3,4))
  print(a)
  print(b)
  print(a * b)
  ```
- **Output**
  ```bash
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]] # a

  [[12 13 14 15]
   [16 17 18 19]
   [20 21 22 23]] # b

  [[  0,  13,  28,  45],
   [ 64,  85, 108, 133],
   [160, 189, 220, 253]] # a * b
  ```
- Here, the corresponding element of the two arrays are multiplied, and a new array with new multiplied values is created.
- In depth, the first element of `a` is multiplied to the first element of `b`, then the second element of `a` is multiplied to the second element of `b`, then the third element of `a` is multiplied to the third element of `b`, and so on till the last element of the arrays.


> [!NOTE]  
> In the same manner, we can apply other operators between two arrays, such as float division `/`, integer division `//`, exponent `**`, and many more.

> [!TIP]  
> Link to Next Article  
> 🡺 [Useful Numpy Methods](/Numpy/Articles/83_numpy_methods.md)