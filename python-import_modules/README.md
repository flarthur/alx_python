# Python Import and Modules  

This readme offers a brief explanation of the Python concepts of import and modules with relevant examples.  

## Modules
Python uses the `import` statement to bring external code (`modules`), into the current python script.  
By doing this we can access functions, classes and variables defined in other files without duplicating them.  
This enhances code organizations and makes code reusable.  

### Creating Modules

You can create modules by writing functions, classes and variables in a seperate `.py` file. Now these modules can be imported to other scripts for their functionality.  

Example; `module_1.py`

````py
#module_1
def hello(name):
  return f"Hello, {name}."
````

and then use the module in a seperate script:

````py
import module_1

print(module_1.hello("ManChego"))

#output: Hello, ManChego
````

### Importing a Module

**To import a module**, use the keyword `import` followed by the module's name. Foe example:
````py
import math
````  

After importing the module, you can use its contents by referencing the module name followed by a dot and the specific item you want to use. For example:  
````py
import math

result = math.sum(7, 3)
````

If you want to import specific files from a module, python gives you the ability to do so using the `from` statement.  
You use `from` *module_name* `import` *item1, item2*  

 For example:
````py
from math import sum, sqrt

result = sum(7, 3)
````

By understanding these concepts you can easily and efficiently manage python projects, write clean-readable code and manage to reuse code across different projects.  

**Happy Coding!** 🫡