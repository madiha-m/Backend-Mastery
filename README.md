## Backend-Mastery

### cmd

### get name space for any instance : **dict**

### TypeError: can only concatenate str (not "int") to str

#### error when trying to concatenate string with integer use str() or repr() to convert integer to string, or use , to concatenate string with integer

#### Difference Between % Formatting and {} (f-strings) in Python

- %s = String placeholder, %d → Integer, %f → Float,, it is old style, slower, and less flexible

### Types of Functions:

- Perform a task
- Return a value

### \'Iterable things in python\'

- range ()
- list
- tuple
- string

### Falsy Menus in Python

- 1- \"\"
- 2- 0
- 3- None

### Lambada anonymous Function

lambda arguments : expression

### Python Data Structures Comparison Table

| Feature                    | **List (`list`)**              | **Tuple (`tuple`)**             | **Set (`set`)**                  | **Dictionary (`dict`)**                 |
| -------------------------- | ------------------------------ | ------------------------------- | -------------------------------- | --------------------------------------- |
| **Ordered?**               | ✅ Yes                         | ✅ Yes                          | ❌ No (Unordered)                | ❌ No (Unordered)                       |
| **Indexed?**               | ✅ Yes (0-based index)         | ✅ Yes (0-based index)          | ❌ No                            | ❌ No (Uses keys instead)               |
| **Mutable?**               | ✅ Yes (Can modify)            | ❌ No (Immutable)               | ✅ Yes (Can modify)              | ✅ Yes (Can modify values)              |
| **Allows Duplicates?**     | ✅ Yes                         | ✅ Yes                          | ❌ No (Unique values only)       | ✅ Yes (but keys must be unique)        |
| **Change Size?**           | ✅ Yes (Dynamic)               | ❌ No (Fixed)                   | ✅ Yes (Can grow/shrink)         | ✅ Yes (Can grow/shrink)                |
| **Data Type Flexibility?** | ✅ Mixed types                 | ✅ Mixed types                  | ✅ Mixed types                   | ✅ Keys & values can be different types |
| **Performance**            | 🔸 Slower (due to flexibility) | 🔹 Faster (due to immutability) | 🔹 Faster (for lookups)          | 🔹 Very Fast (for key-value access)     |
| **Access Speed**           | 🔸 Slower (Iterative search)   | 🔹 Faster (Indexed)             | 🔹 Faster (Hashing)              | 🔹 Fastest (Direct key lookup)          |
| **Use Case**               | General-purpose storage        | Fixed data (constants)          | Unique elements & set operations | Key-value pairs for fast lookups        |

### Diff. b/w array and lists, what is used in python

Array: all elements in order form, changeable, duplicates allowed, all elements must be of same data type
List: all elements in order form, changeable, duplicates allowed, all elements must be of same data type

### Tuple

- Tuple is an ordered, immutable, and indexed collection of elements.
- To create single tuple use , e.g. single_tuple = ('abc',) if we not use comma then it will be string
  > - In Python, variable names are just references to objects in memory. When you assign a new tuple to names, the old tuple is no longer accessible unless it was assigned to another variable.

### Sets

- A set is an unordered collection of unique elements.
- Sets are mutable, meaning they can be modified after creation.
  > - Create **Empty Set** using set() function, not with {} as it is dictionary in python
- Diff b/w set() and set(())
  > - set() is mutable, empty set,
  > - set(()) is immutable, empty tuple in a set
-

#### Diff. b/w remove() and discard() methods

- Remove(): if any item not found in sets, It will raise **KeyError**
- Discard(): if any item not found in sets, It will **not raise any Error**

### Dictionary

#### Difference b/w {dictionary_name[<key>]} and {dictionary_name(<key>)}

> - dictionary_name[<key>]: Direct key access using square brackets ([]), Raises a **KeyError** if the key does not exist.
> - {dictionary_name(<key>)}: **Does NOT raise an error** if the key is missing. **Returns None** instead of crashing the program. **Needs to provide a default value** if the key is not found.

#### Difference Between dict.update() and dict[key] = value When Adding Items in a Dictionary

> - dictionary_name.update({<key>: <value>}): Can add multiple key-value pairs at once. Accepts a dictionary, allowing merging of dictionaries. Cannot access a value directly (unlike dictionary_name[<key>]).
> - dictionary_name[<key>] = <value>: Adds a new key-value pair if the key doesn’t exist. Updates the value if the key already exists. Only works for one key at a time.

### Additional Operators: Has 2 types

Identity Operators: Used to compare obj. It has 2 types:

- is: compare 2 values, are those actually **same** value markdown
- is not: compare 2 values, are those actually **not same** value markdown

Membership Operators: Used to check sequence , if value is present in sequence or not. It has 2 types:

- in: check value is present in sequence or not
- not in: check value is not present in sequence or not

### Class vs. Instance

- class is a blueprint, while an instance is a unique object created from that class. Each instance has its own memory location
- Instance variables hold data unique to each instance, while class variables are shared among all instances
- Class methods: bound to the class and can be called without creating an instance of
  the class. Used to define class-level functionality
- Static methods: belong to a class rather than an instance of the class. Used to define class-level functionality that does not depend on the state of the class or its instances

### **init** method

- The **init** method (constructor) initializes instance variables when an object is created, allowing for automatic assignment of attributes.
- The first argument of methods in a class is conventionally named **self**, representing the instance itself

### self

- self represents the instance of the class.
- It is used to access variables/object’s attributes and methods.
- It must be the first parameter in instance methods (but can be named differently).
- It is not a keyword, but a convention, and can be named anything, but it is conventional to name it **self**.

### Instance Variables vs Class Variables

- Instance variables: Unique to each instance of a class.
- Class variables: Shared among all instances of a class, meaning they hold the same value for every instance.
- To access class variables, Referenced through the class itself or through an instance of the class.

### Modules

- A module is just a .py file, contains reusable code (like functions, classes, or variables).
- while using **dictionary** if key is missing, it return **KeyError**. To avoid or handle use get method
  > - **dictionary_name.get(key, default_value)**

### File Handling

Python supports built-in file handling. The open() method used to create, read, write, and delete files.

### File Opening Modes

| **Mode** | **Description**                                                   |
| -------- | ----------------------------------------------------------------- |
| `"r"`    | Read mode (default) – Opens a file for reading, error if missing. |
| `"w"`    | Write mode – Creates or overwrites a file.                        |
| `"a"`    | Append mode – Adds content to the file’s end.                     |
| `"x"`    | Create mode – Creates a new file, errors if it exists.            |
| `"t"`    | Text mode (default) – Reads/writes text files.                    |
| `"b"`    | Binary mode – Reads/writes binary files (images, PDFs, etc.).     |

**Use `open("filename", "mode")` to handle files efficiently.**

#### Troubleshooting File Read Issues

| **Possible Issue**       | **Fix**                                 |
| ------------------------ | --------------------------------------- |
| File is empty            | Add content before reading              |
| Cursor at end            | Use `file.seek(0)` before `read()`      |
| File not found           | Check with `os.path.exists("file.txt")` |
| File not closed properly | Use `with open()`                       |

#### File Reading Methods

| **Method**    | **Returns**                  | **Output Format**        |
| ------------- | ---------------------------- | ------------------------ |
| `readlines()` | List of all lines            | `['line1\n', 'line2\n']` |
| `read()`      | Full file as a single string | `"line1\nline2\n"`       |
| `readline()`  | Reads one line at a time     | `"line1\n"`              |

#### Use **with** in File Handling

- Used for better file handling.
- Automatically manages file closing and ensures resources are properly released, even if an error occurs.
- Prevents file corruption or memory leaks.
- More readable and cleaner code.


