# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [String Methods in Python](/Python/Articles/19_string_methods.md) 🧰

## Complexity Analysis in Programming 📊

Complexity analysis helps in determining the efficiency of an algorithm, mainly focusing on time and space usage. It’s crucial to understand how the algorithm scales with the size of the input.

### Ways to Analyze an Algorithm

1. **Time Complexity**: Measures the amount of time an algorithm takes to complete as a function of the length of the input.
2. **Space Complexity**: Measures the amount of memory an algorithm uses as a function of the length of the input.

### Notations Used in Analyzing Algorithms 📈

1. **Big O Notation (O)**: Represents the upper bound of an algorithm's running time. It provides the worst-case scenario.
   - **Example**: $O(n^2)$ means the running time increases quadratically as the input size increases.

2. **Big Ω Notation (Ω)**: Represents the lower bound of an algorithm's running time. It provides the best-case scenario.
   - **Example**: $Ω(n)$ means the running time increases linearly with the input size at a minimum.

3. **Big Θ Notation (Θ)**: Represents the tight bound of an algorithm's running time. It indicates both the upper and lower bounds.
   - **Example**: $Θ(n \log n)$ means the running time grows asymptotically as $n \log n$.

4. **Little o Notation (o)**: Represents an upper bound that is not tight. It’s used to describe an upper bound that is not asymptotically tight.
   - **Example**: $o(n^2)$ means the running time grows slower than $n^2$.

5. **Little ω Notation (ω)**: Represents a lower bound that is not tight.
   - **Example**: $ω(n)$ means the running time grows faster than $n$.

### Complexity Classes

1. **Constant Time – $O(1)$**: The algorithm's running time is constant and does not change with the input size.
   - **Example**: Accessing an element in an array by index.

2. **Logarithmic Time – $O(\log n)$**: The running time grows logarithmically as the input size increases.
   - **Example**: Binary search in a sorted array.

3. **Linear Time – $O(n)$**: The running time grows linearly with the input size.
   - **Example**: Iterating through an array.

4. **Linearithmic Time – $O(n \log n)$**: The running time grows as $n \log n$.
   - **Example**: Efficient sorting algorithms like mergesort and heapsort.

5. **Quadratic Time – $O(n^2)$**: The running time grows quadratically with the input size.
   - **Example**: Simple sorting algorithms like bubble sort, insertion sort.

6. **Cubic Time – $O(n^3)$**: The running time grows cubically with the input size.
   - **Example**: Some dynamic programming algorithms.

7. **Exponential Time – $O(2^n)$**: The running time grows exponentially with the input size.
   - **Example**: Algorithms for the traveling salesman problem, certain recursive algorithms without memoization.

8. **Factorial Time – $O(n!)$**: The running time grows factorially with the input size.
   - **Example**: Generating all permutations of a set.

### Additional Information 📝

1. **Amortized Analysis**: Analyzes the average time per operation over a sequence of operations, ensuring that the average is small, even if some operations are expensive.
   - **Example**: Dynamic array resizing.

2. **Best, Worst, and Average Case**: Analyzing the performance of an algorithm in different scenarios helps to understand its efficiency comprehensively.
   - **Best Case**: The minimum time taken (ideal scenario).
   - **Worst Case**: The maximum time taken (worst scenario).
   - **Average Case**: The expected time taken for a typical scenario.

3. **Practical Considerations**: While Big O notation provides an upper bound, real-world performance can be influenced by constants, lower-order terms, and hardware specifics.

### Example Analysis: Binary Search

- **Best Case**: $Ω(1)$ – The element is found in the first comparison.
- **Worst Case**: $O(\log n)$ – The element is found after logarithmic comparisons.
- **Average Case**: $Θ(\log n)$ – On average, logarithmic comparisons are needed.

### Example Analysis: Bubble Sort

- **Best Case**: $Ω(n)$ – The array is already sorted, and only one pass is needed.
- **Worst Case**: $O(n^2)$ – The array is sorted in reverse order, requiring quadratic passes.
- **Average Case**: $Θ(n^2)$ – On average, quadratic passes are needed.

Understanding complexity analysis allows developers to choose the most efficient algorithms for their specific problems, ensuring better performance and scalability. 😊

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->