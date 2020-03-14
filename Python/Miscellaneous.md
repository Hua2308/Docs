* \* can convert __list/tuple__ into function's positional arguments, \*\* can convert __dictionary__ into function's positional arguments

* For a dictionary, it can be passed into a function as either positional arguments or key arguments:

  *   Positional arguments: 

  ```
  foobar(*dic)
  ```

  * Key arguments

  ```
  foobar(**dic)
  ```

* attr.s

  * Allow constructor takes dictionary with partial keys:

    ```
    @attr.s(kw_only=True)
    class SomeClass:
        a = attr.ib(default=None)
        b = attr.ib(default=None)
        c = attr.ib(default=None)
    ```

  * Allow dictionary output to ignore keys with empty value:

    ```
    attr.asdict(assay_detail, filter=lambda attr, value: value != None)
    ```

    