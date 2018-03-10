
>>> help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.

>>> list = [1,2,3,4,5,6,7]
>>> max(list)
7
>>> min(list)
1

>>> list[4]= 8
>>> 
>>> print(list[4])
8
>>> list = [4,56,3.57,7.98]
>>> round(3.57,1)
3.6
>>> round(3.57)
4

sorted() function
>>>first = [1.23,4.54]
>>> second = [2,4.5]
>>> full = first + second
>>> full_sorted = sorted(full, reverse = True)
>>> print(full_sorted)
[4.54, 4.5, 2, 1.23]
>>>first.index(4.54)
1

>>> list = ["nabin","kumar","timalsina"]
>>> print(list)
['nabin', 'kumar', 'timalsina']
>>> list.index("kumar") # method index()
1
>>> list.count("timalsina") # method count()
1
>>> list.count("nabin") 

brother = "nabin"  # stored name nabin in brother variable
>>> brother.capitalize()
'Nabin'
>>> brother.replace("na","sa")
'sabin'
>>>brother.index("b")
2


>>>r =0
>>> import math   #math package
>>> c = 2*math.pi*r
>>> print(c)
0.0
>>> r= 5
>>> from math import pi
>>> c = 2*r* math.pi
>>> 
>>> print(c)
31.41592653589793
>>>  









