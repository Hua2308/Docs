* Logging better than print
    * Add additional diagnostic information such as time, location, function name and etc.
    * Categorize information in order to silence certain levels
    
* Three ways to config [logging](http://docs.python-guide.org/en/latest/writing/logging/)
    * config file .ini
    * json dictionary
    * code

* Three components
    * logger (specifiy handler, level)
    * handler (specify formatter, level)
    * formatter
Note: logger level and handler level are two chained filters, which work together to determine the final level. For example, logger level is debug and handler level is info, then final level is info. Another example, logger level is info, and handler level is debug, then final level is still info.

* Six logging [levels](https://docs.python.org/2/library/logging.html#levels)
    * CRITICAL	50
    * ERROR	40
    * WARNING	30
    * INFO	20
    * DEBUG	10
    * NOTSET
    
