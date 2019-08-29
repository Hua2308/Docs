# Find **first** match in a string 
### Usage: match = **re.search(pattern, str)**:
* Note: if match is not None, then it will return **a match object**, and match.group() will be the matched string. If there are _()_ part in the pattern, then match.group(1) will return the first (), match.group(2) return the second, and so on.

# Find **all** matches in a string 
### Usage: matches = **re.findall(pattern, str)**:
* Note: if match is not None, then it will return **a list of matched strings**.


# Find **first** match in the beginning of a string
### Usage: matches = **re.match(pattern, str)**:
* Note: if match is not None, then it will return **a match object**, and match.group() will be the matched string. If there are _()_ part in the pattern, then match.group(1) will return the first (), match.group(2) return the second, and so on.

 
