# Python Operations

**1** **str** to **list** and **list** to **str**

* string to list: list(str)
* list to string: ''.**join**(lst) or ''.join(str(ch) for ch in lst )

**2** get 1st letter and rest part in str:

*  1st, rest = str[0], **str[1:]** 
  * Note: str[1:-1] will **NOT** return the rest because it is right side exclusive! For example, str = 'abc', then str[1:-1] will only return 'b'

**3** list.append() returns **None**, do **NOT** pass this into a function like foobar(lst.append())

