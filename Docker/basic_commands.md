* Authentication
   * Login
     * ```docker login <URL>```
   * Login bash
     * ```docker exec -it <container id> /bin/bash```
* Image
   * Create an image
     * ```docker build -t <tag>:<version> --build-arg http_proxy=<proxy_url> --build-arg https_proxy=<proxy_url> .``` 
   * Delete an image
     * ```docker rmi tag:version(or image ID)```
   * Tag an image
     * ```docker tag <image_id> <tag>:<version>```
   * List images
     * ```docker images```
   * Pull image to local
     * ```docker pull <tag>:<version>```
   * Push image to remote
     * ```docker push <tag>:<version>``` (tag has URL)
* Container
   * Run a container from local image
     * ```docker run -it --name <webapp_name> <tag>:<version>```
   * Stop all running containers
     * ```docker rm -f $(docker ps -aq)```
   * List all running containers  
     * ```docker ps```
* Workflow
  * a. Create a local image or pull it from remote
  * b. Run image as a container (-it as interactive mode)
  * c. Stop container
  * d. Delete image or push image
