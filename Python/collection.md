* deque
    * deque supports thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction
    
  * Operations
  
    ```
    deque().append
    deque().pop
    deque().appendleft
    deque().popleft
    ```
  
    
  

* defaultdict

  * defaultdict is a subclass of the built-in dict class. It assign a default value for each element.

  * Operations:

    ```
    d = defaultdict(str)
    
    for i in range(3):
        d[i] += 'y'
    ######################
    d = defaultdict(int)
    
    for i in range(3)
        d[i] += 1
    ```



* namedtuple

  * Named tuple assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used whenever regular tuples are used, and they add the ability to access fields by **name** instead of of **position index**.

  * Operations

    ```
    # Format: namedtuple(typename, field_name_list)
    namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=12)
    p = Point(11, y=12)
    p[0] + p[1] = 23
    p.x + p.y = 23
    #####################
    namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
    for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    	print emp.name, emp.title
    ```

    

* OrderedDict

  * Ordered dictionary is just like regular dictionary but they remember the order that the items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added.

  * Operations

    ```
    d = collections.OrderedDict()
    d['a'] = 'A'
    d['b'] = 'B'
    ```

    