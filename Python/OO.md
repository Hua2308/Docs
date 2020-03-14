* Overloading vs Overriding:
    * Overriding is supported
    * Overloading is NOT supported
  
* Namespace:
    * Local: {var a}
    * Nonlocal: {nonlocal a}
    * Global: {global a}

* Class definition:
    * Can be anywhere(under if statement, or inside function, etc.)
    * Can have various statements other than function

* Static variable vs instance variable:
    * Static varible is defined within class
    * Instance variable is defined within __init__(self) method

* Method call
    
* someClassObj.method() is equavilent to someClass.method(someClassObj)
    
* Multiple inheritance
    
* no namespace conflicts. Python just searches inherited super class( such as subclass(SuperClassA, SuperClassB, SuperClassC)) from left to right, and once found a attribute/method, then call it.
    
* Private member
    
    * two leading underscores: __variable or __function()
    
* Staticmethod vs classmethod

    * @classmethod can take a `cls` parameter. `cls` class reference can be used to instantiate a new instance e.g. `cls(param1, param2)`  It can be called by class, e.g ClassA.classmethodA

    * @staticmethod does not need to take a `cls` parameter. It can be called by classB.staticmethodB

    * @staticmethod is one way to notate state method. Alternatively, if a method does not take a `self` parameter, by default it is also a static method. E.g. 

        ```
        def i_am_a_static_method():
        	print("static")
        
        # is equvilent to
        
        @staticmethod
        def i_am_also_a_static_method():
        	print("static too!")
        ```

