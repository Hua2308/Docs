# CORS - Cross Origin Resource Sharing
### Error:
* ```Access to XMLHttpRequest at 'https://my_application_server.com' from origin 'https://my_client.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on requested resource.```

### Explanation:
* There are two types of http requests. One is regular http request, and the other is XHR - XML Http Request.(mostly used in Ajax). For XHR, CORS is a mechnism that allows restricted resource to be requested from another domain rather than the server host. And remote server has to give permission, in the response header, to allow browser/XHR to do so.

### Solution:
```        
if request.headers['Host'] in [Constants.LOCAL_HOST_IP, Constants.LOCAL_HOST, Constants.DEV_HOST]:

    response.headers['Access-Control-Allow-Origin'] = request.headers['Host']
    
    response.headers['Access-Control-Allow-Headers'] = \
            "Origin, X-Requested-With, Content-Type, Accept, Authorization, userName",
            
	response.headers['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, PUT, DELETE"
```

 
