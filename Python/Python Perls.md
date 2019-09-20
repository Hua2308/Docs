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

	  


 
