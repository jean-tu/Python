#Notes
This is just going to be a readme file that will kind of just document what I've learned from the codeacademy class and the index.txt is the file that lists how I am using the things that I am learning.

##Random good to knows
* You can take the max of arguments with `max(arg1, arg2,....)`
* You can take the min of arguments with `min(arg1, arg2,....)`
* You can take the absolute value of a number with `abs(number)`
* You can figure out the type of something with `type(value)`


##Comments
You can comment the code using 3 Quote marks at the beginning and at the end of the statement or you can use a hashtag

```python
  #This is the hashtag way to comment
  """This is the quotation way to comment"""
```

##Functions
You declare a function by using `def function_name(): `
To call on a function, you just do `function_name()` when ever you want to call on it

You can take in all of the arguments passed into a function with `def function_name(*args)` the  `*args` is what allows you to take in all of the arguments, however, it would be hard to know which one is which because every time you would have to just reference  `args`


##Import statements
You can use import statements to use previously defined functions, it's bascially importing a library.

```python
import math
print math.sqrt(25) #this will allow you to print 5 because the sqrt function is defined within the math library
```
You can also only import a specific function from a library by using `from library import function`

```python
from math import sqrt
```

You can also print everything that is inside a library by doing:
```python
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!
```

##Lists
* It seems like lists are similar to arrays in Java & C++ b/c an empty list is `empty_list = []` and you can use indexing to access a value
* You can add additional items to the list with `list_name.append(value)`

###Slicing strings

```python
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]   # The fourth through sixth characters
frog = animals[6:10]  # From the seventh character to the end
```

###How to replace an item within a list that is kind of like a map

```python
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"
# Your code here!
animals.insert(duck_index, "cobra")
print animals # Observe what prints after the insert operation
```
