* 1. Definition: a mixin is a class that contains methods for other classes' usage but does not have to be their parent class. Mixin implementation varies by languages.

* 2. Advantage: Mixin promotes code reuse and can avoid multiple inheritance ambiguity - **diamond problem**, or as a workaround for language that lack of multiple inheritance. A Mixin can also be viewed as an **interface** with methods.

  **Note**: a diamond problem is as below:

  ​         

  ​     /   B  \

  A               D

​            \   C  /



​        If, B and C both overrided one method, then which one D is going to inherit?

​        Mitigation:

​        Java: After Java 8, interface D must reimplement the default method. Before Java 8, it is perfectly fine to have same name methods in different interfaces ( as they are not implemented anyway, no conflict. )

Code example in Java:

```public class HelloWorld{

     public static void main(String []args){
        System.out.println("Hello World");
        D d = new D();
        d.doSomething();
     }
}

interface A {
    public void doSomething();
}

interface B {
    public void doSomething();
}

interface C extends A, B {
    
}

class D implements C {
    public void doSomething(){
        System.out.println("D do something");
    }
}
```

​        Python: inherit based on order specified in the tuple of based classes, i.e. D, B, C, A, whichever first contains the method