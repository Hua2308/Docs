* Computer can only save 0 and 1 digit. To be able to compute/store/transfer information, we need a encoding and decoding system to translate symbol into number. E.g. A -> 0000 0001. 
* Encoding system:
  * ASCII: 7 bits -> 128 symbols including letters, numbers, and etc.
  * UTF-8: 32 bits -> 1,112,064 symbols including characters from all languages
* Number vs. number in string: 
  * 1 vs "1": both 1 is stored as 092, however, in "1", 1 is stored together with quotes, such as 042 092 042, which can be understood by language interpreter that this is number in string.  