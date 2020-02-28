* Logging format
    * Timestamp - Level - Process - Thread - Function Name - Message (Message needs to be at the end for clarity. Line number is not needed as function name is sufficient to locate code)
    
      For example (Python):
    
      ```
      %(asctime)s %(levelname)5.5s %(process)d --- [%(threadName)s] %(funcName)s : %(message)s
      ```
    
