* Flat is bettern than nested - The Zen of Python
	* **For loop:**

	```
		result = []
		for item in item_list:
			new_item = do_something_with(item)
			result.append(new_item)
	```
	
	*  	**List Comprehension:**

	```
		result = [do_something_with(item) for item in item_list]
	```
	
	* **Generator Expression**

	```
		result = (do_something_with(item) for item in item_list)
	```
	
	* **Map reduce**
	
	```
		map(lambda x: x * 2, item_list)
	```