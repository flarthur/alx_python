# Defining Functions

Functions are reusable blocks of code that allow you to consolidate specific tasks, making your code more organized and easier to maintain.  

They are defined using the `def` keyword, they can also take inputs and return outputs.  


### Defining a function  
The following syntax is followed when defining a function:  
````py
def function_name(parameter...):

  return result
````

- `"function_name"` is the name of the function. Choose a descriptive name, indicating what the function does.  
- `"parameter..."` is an optional input parameter (argument) that the function can accept. You can have none, or several parameters.  
- `"return"` .Return statement is used to make the function produce an output.  
If there is no return statement, the function will return `None` by default.

### Example of a function  

Here is a function that calculates the sum of a given number with 2:

````py
def sum(number):

  answer = number + 2
  return answer

````  

Once the function is defined, you are able to call it in your code, using appropriate arguments. E.g:  
````py
# calling our sum function and storing the answer we get in a variable
number = int(input("Give me a number between 0 and 10 \n"))
answer = sum(number)

print("The sum of {} + 2 is {} ".format(number, answer))
````  

Using functions in python allows you to break down complex problems into smaller doable tasks.  
This promotes code usability and enhances code readability.  

Consider creating a function the next time you find yourself repeating a task or some given operations.

**Happy Coding!** 🫡