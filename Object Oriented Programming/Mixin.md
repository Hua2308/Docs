* 1. Definition: a mixin is a class that contains methods for other classes' usage but does not have to be their parent class. Mixin implementation varies by languages.

* 2. Advantage: Mixin promotes code reuse and can avoid multiple inheritance ambiguity - **diamond problem**, or as a workaround for language that lack of multiple inheritance. A Mixin can also be viewed as an **interface** with methods.

  **Note**: a diamond problem is as below:

  ​         

  ​     /   B  \

  A               D

​            \   C  /



​        If, B and C both overrided one method, then which one D is going to inherit?

​        Mitigation:

​        Java: interface D must reimplement the default method. 

​        Python: inherit based on order specified in the tuple of based classes, i.e. D, B, C, A, whichever first contains the method