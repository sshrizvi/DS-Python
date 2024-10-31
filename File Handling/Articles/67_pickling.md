# Python for Data Science <picture> <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.webp" type="image/webp"> <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f40d/512.gif" alt="🐍" width="32" height="32"> </picture>

> [!TIP]  
> Link to Previous Article  
> 🡸 [Understanding JSON, Serialization, and Deserialization in Python](/File%20Handling/Articles/66_json.md)

# Serialization in Python: Custom Data Types, Pickling, and JSON

Data serialization plays a critical role in many applications by enabling the storage, transmission, and retrieval of data. While JSON is a common format for simple data structures, serializing custom data types (like class instances) often requires more advanced techniques. Python provides both JSON and the `pickle` module for these needs, with each serving distinct purposes.

---

## 1. Serializing Custom Data Types (Classes and Objects)

When working with complex data in Python, such as objects created from user-defined classes, direct JSON serialization isn’t possible because JSON only supports basic data types like dictionaries, lists, strings, numbers, booleans, and null. To serialize these custom objects, we need to convert them into a JSON-compatible format, usually through custom encoding methods.

### Custom Encoding for JSON

For custom classes and objects, JSON serialization can be achieved by creating a method to convert the object into a dictionary. We can then use `json.dumps()` or `json.dump()` with a `default` parameter to specify a custom encoder.

### Example: JSON Serialization of a Custom Class
```python
import json

# Define a custom class
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

# Custom encoder function to convert object to dictionary
def employee_encoder(employee):
    if isinstance(employee, Employee):
        return {"name": employee.name, "age": employee.age, "department": employee.department}
    raise TypeError("Object of type Employee is not JSON serializable")

employee = Employee("Alice", 30, "HR")
# Serialize to JSON using the custom encoder
json_str = json.dumps(employee, default=employee_encoder)
print("Serialized JSON String:", json_str)
```

### Custom Decoding for JSON
When deserializing, a custom decoder can be used to convert JSON back into a class instance.

```python
def employee_decoder(json_data):
    return Employee(**json_data)

# Deserialize JSON string back to an object
employee_obj = json.loads(json_str, object_hook=employee_decoder)
print("Deserialized Object:", employee_obj.__dict__)
```

### Dead-Ends and Challenges
- **Complex Nested Structures**: JSON serialization becomes tricky when custom objects have nested or cyclic references. This requires recursive encoding.
- **Losing Method References**: JSON doesn’t serialize methods, so you cannot serialize an object’s behavior, only its data.

---

## 2. Pickling with the `pickle` Module

**Pickling** is Python’s built-in method for serializing and deserializing complex objects, including custom class instances, functions, and modules. The `pickle` module saves objects in a binary format, making it versatile for many data types. Unlike JSON, `pickle` handles both data and behavior, making it ideal for saving entire Python objects.

### Why Use Pickle?
1. **Complex Data Types**: `pickle` can serialize any Python object, including custom classes and functions.
2. **Binary Format**: The binary format is compact and fast to read/write.
3. **Preserves State**: `pickle` preserves the state of Python objects, enabling them to be restored later.

### Methods for Pickling
- **`pickle.dumps()`**: Serializes an object to a byte stream.
- **`pickle.dump()`**: Serializes an object and writes it directly to a file.
- **`pickle.loads()`**: Deserializes a byte stream back to a Python object.
- **`pickle.load()`**: Reads from a file and deserializes the byte stream.

### Example: Pickling a Custom Class
```python
import pickle

class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

employee = Employee("Bob", 40, "Engineering")

# Pickle to file
with open("employee.pkl", "wb") as file:
    pickle.dump(employee, file)

# Load from pickle file
with open("employee.pkl", "rb") as file:
    loaded_employee = pickle.load(file)
    print("Loaded Object:", loaded_employee.__dict__)
```

### Dead-Ends and Challenges
- **Security Risk**: `pickle` can execute arbitrary code, making it vulnerable to malicious code injection. Only unpickle data you trust.
- **Platform Dependency**: Pickled files may not be compatible across different Python versions or platforms.
- **File Corruption**: Binary files can become corrupt, especially if transferred improperly, leading to data loss during unpickling.

---

## 3. Pickle vs. JSON

| Feature                    | JSON                                       | Pickle                                          |
|----------------------------|--------------------------------------------|-------------------------------------------------|
| **Format**                 | Text                                       | Binary                                          |
| **Use Case**               | Simple data types, web data exchange       | Complex objects, including classes and functions|
| **Human-Readable**         | Yes                                        | No                                              |
| **Security**               | Secure if handled carefully                | Vulnerable to code execution risks              |
| **Speed**                  | Slower for large datasets                  | Faster, especially with binary data             |
| **Cross-Language Support** | Yes (JSON is language-agnostic)            | No, Python-specific                             |
| **Supported Data Types**   | Primitive types (dict, list, str, int)     | Almost any Python object, including functions   |
| **Error Handling**         | Graceful handling with JSONDecodeError     | Limited, prone to EOFError and UnpicklingError  |

### Key Takeaways
- **Use JSON** when you need a human-readable, cross-platform format suitable for configuration files, data sharing, and APIs.
- **Use Pickle** for saving complex objects within Python applications where cross-language compatibility is unnecessary and security is not a concern.

---

### Additional Considerations for Data Scientists

When working with model parameters, experimental configurations, or cached data, **JSON** is typically safer and more versatile. However, **Pickle** is highly effective when storing pre-trained models or large datasets for use within Python applications.

By mastering both JSON and Pickle, you gain flexibility in data serialization options, each tailored to specific needs in your data science workflows.

> [!IMPORTANT]  
> Watch the video on Recursion as upcoming task contains questions on Rescursion.  
> [Link to Recursion](https://www.youtube.com/watch?v=9bsK03SlmNM)

> [!IMPORTANT]  
> If you have studied Article 62-67, I would suggest you to perform some task so that you can check on your learning. Here is the link : [Task 10](/File%20Handling/Tasks/task_10.ipynb)

> [!TIP]  
> Link to Next Article  
> 🡺 [Understanding Errors in Python: Types, Causes, and Examples](/Exception%20Handling/Articles/68_errors_in_python.md)