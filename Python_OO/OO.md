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
