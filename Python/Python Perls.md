# Python Perls

**1** Python is an interpreted language

**2** Python code is typically shorter than C/C++/Java:  
	* no variable declaration.  
	* no brackets.  
	* single statement expresses complex operations.

**3** Print(r"user \name"): r will output raw value and ignore escape characters

**4** string can be concatenated with *: ```2 * "hello" = "hellohello"```, i.e. in Python, number can multiply string

**5** two or more string next to each other are automatically concatenated ```'hello' 'world' -> 'helloworld'```

**6** string can be indexed(subscripted). e.g. word = 'Python', word[0] is 'P'. index can also be negative numbers, to start counting from the right. Since -0 is 0. **Negative indeces start from -1**

**7** string can also be sliced, to get a substring. e.g.   
	* ```word[0:2]``` **#characters from position 0 (included) to 2 (excluded)**.  
	* ```word[:i] + word[i:]``` is the same as ```word``` **#start index is always included, and end always excluded**.   
	* ```word[-2:]``` **#characters from second last to the end**   
	Tips:   
	1. length of slice is the **difference of the indices**, e.g. ```word[1:3]```, length is 2.  
	2. **negative index = -[length - positive index]**, e.g. ```s = "Python", s[0] == s[-6], s[5] == s[-1]```

**8** string is immutable. Assign to an indexed position of string results in error

**9** ```//``` is floor operation. ```17 // 3 == 5```

**10** ```**``` is used to calculate powers

**11** ```4 * 3.75 - 1``` operators with mixed type operands convert the integer operands to floating point

**12** list, dictionary is **mutable**. Be aware of passing the same one while the intention is to clone

**13** to make a change of the list that is looping through, first make a copy of it:   
	 
		for w in words[:]
			if len(w) > 6:
				words.insert(0, 2)
		
		# Note: words[:] create a new copy of words

**14** Loop's else statement will be executed when exhaustion of the list, but not when the loop is terminated by a break statement.

**15** **kwargs must be behind *args. Args are mandatory, and Kwargs are optional**

	def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue')
		...
	
	Valid calling ways:
	parrot(1000)                                          # 1 positional argument
	parrot(voltage=1000)                                  # 1 keyword argument
	parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
	parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
	parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments. **Use position arguments to init keyward arguments**
	parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
	
	Invalid calling ways:
	parrot()                     # required argument missing
	parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
	parrot(110, voltage=220)     # duplicate value for the same argument
	parrot(actor='John Cleese')  # unknown keyword argument

**16** Arbitrary argument lists
	
	def parrot(*args, **kwargs)
		...
	
	Note: args is a tuple. kwargs is a dictionary.

**17** **Unpack argument lists.**  
when arguments are in a list/tuple or dictionary, we can unpack them to pass into a function. **Unpack means break one entity(list or tuple) into many elements.** So, * unpacks a list/tuple, and ** unpack dictionary.

**18** 
Queue implementation: insert or pop from the beginning of list is slow. Use collections.deque to implement a queue like ```deque(list_of_items)```

**19**
Control number precision: round(num, i) will round number to i decimal digits. E.g. round(pi, 2) = 3.14

**20**
Zip takes a list of tuples, or *(list_of_list), and zip together nth element.

**21**
```t = 1,2,3``` this initiated a tuple. And tuple is **immutable**. ```a,b,c = t``` unpack a tuple

**22**
dictionary key has to be immutable. If tuple contains list, then this tuple cannot be used as key.

**23**
list(dict) will return a list of all the keys. sort(dict) will sort dict by keys.

**24**   
Looping dict:   
		* keys&values: ```k, v in dict.items()```    
		* keys: ```k in dict.keys()```              
		* values: ```v in dict.values()```    
Looping sequence(with index)
		* for i,v in enumerate(['tic', 'tac', 'toe'])

**25**
range(a,b) is left inclusive, right exclusive. So range(1, 10) is 1 - 9, **range(10, 1, -1) is 10 - 2**        

**26**
```and``` and ```or``` are short-circuit operators, and the evaluation stops as soon as the outcome determines. E.g.

```
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

**27**
```From fibo import *``` will not import those beginning with **_**, and if \__all__ is not defined in __init__.py, it will NOT import any submodules.

**28**
```python fibo.py 50``` then, ```sys.argv[1]``` can retrieve it.

**29** any .py file can be a module, and any directory with __init__.py is a package

**30** ```with open('some_file') as f``` this is good practice as file will be automatically closed after its suite finishes

**31** ```try except``` only execute one except, which is the first one that catches it ( super/base exception first ). In ```try except else```, else will run if except does not execute. In ```try finally```, finally will always run no matter whether exception occurs.

**32** Multi-inheritance; derived class can override any methods of its base classes; Class is also an object.

**33** ```yield``` is used in a loop to save the state locally and can be resumed for next interation. Function that has yield is called generator, and will not run when call it, but only through interation.

**33** use ```import os``` instead of ```from os import *```, as __os.open()__ will shadow __open()__

**34**    
 ```map(function, sequence)```: apply function to each of element   
 ```filter(function, sequence)```: apply function to each of element, function has to return True or False to filter
 ```reduce(function, sequence)```: apply function to each of element, and combine the result

**35**
Change variable inside a function should use **global**:   

```
a = 3
def some_fun():
	global a
	a = 4
```

**36**

namedtuple:

from collections import namedtuple. namedtuple is a data structure that assign meaning to each position in a tuple. (i.e. create an object to automatically load tuple value)

```python
from collections import namedtuple
Point = namedtuple("poi", ['x', 'y'])
p = Point(1, 2)
# Then p.x => 1, p.y => 2
# p[0] => 1, p[1] => 2
# p => poi(x=1, y=2)
```





## Exam perls

a. **+1/-1** is valid and equals to -1.0.   
Explanation: positive/negative sign has a higher precedence than arithmatic *, -
     
b. ```[x ** 3 for x in 1..5]``` is invalid.   
Explanation: no .. in python.    

c. Function name can be re-defined as varible:   

```
	def func():
		return 2

	func = func() + 1
	print(func) # valid, 3
	print(func()) # invalid, because func is a variable now
```

d. data = [1, 2, 3], **data.index(3)** is 2

e. Subclass can call superclass constructor in two ways:

```
class SuperClass():
    def __init__(self, val):
        self.val = val
    def get_val(self):
        print(self.val)

class Sub(SuperClass):
    def __init__(self, val):
        SuperClass.__init__(self, val) # way 1
        super().__init__(val) # way 2
```
Explanation: **SuperClass** represents the class, and **super()** represents an instance of Super class.    
Note: super() is lower case.







​	  



