# Lambda, Map, Filter, and Reduce in Python

## Introduction

This README provides a brief overview of lambda functions, `map`, `filter`, and `reduce` in Python. These are powerful functional programming tools that allow you to write concise and efficient code for data manipulation and transformation.

## Lambda Functions

A lambda function is a small anonymous function that can take any number of arguments and return a single expression result.   
They are defined using the `lambda` keyword and are often used for short, one-line operations where a full function definition is unnecessary. The general syntax of a lambda function is:

```python
lambda arguments: expression
```

#### Example:

````python
add = lambda x, y: x + y
result = add(2, 3)  # Result will be 5
````
## `map` function
The `map` function applies a given function to all items in an iterable (e.g., list, tuple) and returns a new iterable with the results. The syntax of `map` is:
````python
map(function, iterable)
````
#### Example: 
````python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
# squared_numbers will be an iterable: [1, 4, 9, 16, 25]
````

## `filter` function
The `filter` function constructs a new iterable by selecting the items from an iterable for which a given function returns `True`. The syntax of `filter` is:

````python
filter(function, iterable)
````

#### Example

````python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# even_numbers will be an iterable: [2, 4, 6]
````

## `reduce` function
The `reduce` function (originally from the `functools` module) applies a rolling computation to the items of an iterable.  
It takes two arguments: a function that specifies the computation and an iterable to apply the function cumulatively from left to right. The syntax of `reduce` is:

````python
from functools import reduce

reduce(function, iterable)
````
#### Example:
````python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# product will be 120 (1 * 2 * 3 * 4 * 5)
````

### To conclude:

Lambda functions, `map, filter, and reduce` are powerful tools in Python for functional programming. They allow you to write more concise and elegant code for various data manipulation and transformation tasks.  
By understanding and utilizing these functions effectively, you can improve the efficiency and readability of your Python code.  

**Happy Coding!** 🫡