# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Raising Exceptions in Python. Exception Hierarchy.](/Exception%20Handling/Articles/71_raising_exceptions.md)

# Custom Exceptions : Benefits and Examples

## 1. Introduction to Custom Exceptions

In Python, exceptions are objects that represent errors that occur during the execution of a program. While Python provides many built-in exceptions, such as `ValueError`, `TypeError`, and `KeyError`, there are times when these built-in types may not fully convey the nature of a specific error. In such cases, creating custom exceptions allows for clearer error reporting tailored to specific situations or applications.

Custom exceptions enhance code readability and debugging, as they can communicate unique issues that standard exceptions might not.

## 2. Why Use Custom Exceptions?

Custom exceptions offer several benefits:

- **Clarity**: They make it easy to understand the nature of the error, especially for domain-specific issues.
- **Control**: Custom exceptions give developers greater control over error handling, as they can be raised intentionally when specific conditions are met.
- **Specificity**: They allow differentiation between standard Python errors and application-specific errors, making it easier to pinpoint issues during debugging.
- **Granularity**: By defining different types of custom exceptions, developers can provide more granular error handling, especially useful in large applications.

For example, in a data science project, instead of using a generic `ValueError` when missing data is detected, a custom exception like `MissingDataError` can be used, providing more context.

## 3. How to Create a Custom Exception in Python

Creating a custom exception in Python involves defining a new class that inherits from Python's `Exception` class or any of its subclasses. This ensures that the custom exception behaves like a standard exception and can be caught in `try-except` blocks.

### Basic Structure of a Custom Exception

```python
class CustomException(Exception):
    """Custom exception for specific use case."""
    pass
```

### Example: Creating a Custom Exception for Missing Data

```python
class MissingDataError(Exception):
    """Raised when required data is missing in the dataset."""
    def __init__(self, missing_fields, message="Data is missing for required fields"):
        self.missing_fields = missing_fields
        self.message = f"{message}: {', '.join(missing_fields)}"
        super().__init__(self.message)
```

### Explanation

In this example, `MissingDataError` accepts a list of `missing_fields` and constructs a message that includes the names of those fields. This can be helpful in data science, where missing data is common and can cause downstream issues if not handled correctly.

### Using the Custom Exception

```python
def validate_data(data):
    required_fields = ["age", "income", "gender"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise MissingDataError(missing_fields)

# Sample use case
try:
    sample_data = {"age": 30, "income": None}  # Missing 'gender'
    validate_data(sample_data)
except MissingDataError as e:
    print(f"Error: {e}")
```

In this example, if `sample_data` is missing a required field, the `MissingDataError` is raised with an informative message that lists the missing fields.

## 4. Example of Custom Exceptions in Data Science

### Scenario: Handling Invalid Data Types

In data science, you may encounter invalid data types during data processing. For instance, a model might expect numeric data, but a column contains strings. A custom exception can handle this specific scenario.

#### Defining the Custom Exception

```python
class InvalidDataTypeError(Exception):
    """Raised when a dataset contains invalid data types."""
    def __init__(self, column_name, expected_type, found_type):
        self.column_name = column_name
        self.expected_type = expected_type
        self.found_type = found_type
        self.message = f"Invalid data type in '{column_name}': expected {expected_type}, found {found_type}."
        super().__init__(self.message)
```

#### Using the Custom Exception

```python
def validate_column_type(data, column_name, expected_type):
    if not isinstance(data[column_name], expected_type):
        found_type = type(data[column_name]).__name__
        raise InvalidDataTypeError(column_name, expected_type.__name__, found_type)

# Sample data
sample_data = {"age": "thirty"}  # 'age' should be an int, but is a str
try:
    validate_column_type(sample_data, "age", int)
except InvalidDataTypeError as e:
    print(f"Error: {e}")
```

This example raises `InvalidDataTypeError` if the `age` column is not of type `int`. This approach is more informative and specific than using a generic exception.

## 5. Potential Dead-ends and Difficult Situations

### 1. **Overusing Custom Exceptions**

   While custom exceptions can be useful, overusing them can clutter your code and make it harder to debug. It’s best to create custom exceptions only when they provide a clear benefit over using built-in exceptions.

### 2. **Cascading Errors**

   Custom exceptions can sometimes mask the root cause of an error, especially if exceptions are raised in multiple layers of code. It’s crucial to ensure that custom exceptions add clarity and do not obscure underlying issues.

### 3. **Multiple Levels of Exception Handling**

   When creating custom exceptions, be mindful of complex exception handling flows where multiple exceptions might need to be handled together. This can be common in data science workflows where different data validation checks are stacked.

### 4. **Ensuring Compatibility with Existing Code**

   Custom exceptions are unique to your application, so if you plan to use them in a library or share code, you need to document them well. Other developers using your code might not be familiar with your custom exceptions and could struggle to handle them without sufficient context.

## Conclusion

Custom exceptions in Python are powerful tools for providing clarity, specificity, and control over error handling. They help ensure that unique scenarios, especially in fields like data science, are clearly flagged, making debugging easier. However, custom exceptions should be used sparingly and with caution to avoid unnecessary complexity and ensure maintainable, understandable code.

With careful planning and strategic use, custom exceptions improve both code readability and robustness, particularly when working with complex data workflows.


> [!IMPORTANT]  
> If you have studied Article 68-72, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 11](/Exception%20Handling/Tasks/task_11.ipynb)

<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->