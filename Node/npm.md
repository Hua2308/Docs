1. Show npm configurations: ``` $npm config list```
 * __Note__: default configs like registry are NOT shown by cmd above, to show all, use ```$npm config list -l```

2. Install package 
 * locally(../node_modules) ```npm install <package_name>```
 * globally({prefix}/lib/node/node_modules) ```npm install <pakcage_name> --global```
 
3. List local package ```npm list```

4. Enable proxy ```npm set proxy=<proxy_url>``` and ```npm set https-proxy=<proxy_url>```

   #### [Reference](https://www.sitepoint.com/beginners-guide-node-package-manager/)
