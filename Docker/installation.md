__Linux__
* Red Hat 7
  1. Create a yum repo file: /etc/yum.repos.d/docker.repo. File content is as below:
      
      ```
           [docker]  
           name=Docker Repository  
           baseurl=https://yum.dockerproject.org/repo/main/centos/7  
           enabled=1  
           gpgcheck=1  
           gpgkey=https://yum.dockerproject.org/gpg  
           proxy=<proxy_url>  
           proxy_username:<proxy_username>
           proxy_password:<proxy_password>
      ```
  2. Install docker: 
        
       `$ yum install -y docker-engine`
  
  3. **Optional**: [Setup http proxy](https://docs.docker.com/engine/admin/systemd/#http-proxy) for docker daemon:
       
       * Make a directory
         `$ mkdir -p /etc/systemd/system/docker.service.d`
       
       * Create a config file
         `$ touch /etc/systemd/system/docker.service.d/http-proxy.conf`
       
       * Add HTTP_PROXY, HTTPS_PROXY, and NO_PROXY env variables
         ```
          [Service]
          Environment="HTTP_PROXY=<proxy_url>" "HTTPS_PROXY=<proxy_url>" "NO_PROXY=[e.g. localhost,127.0.0.1]"
         ```
         
       * **Note:** This proxy is only for docker daemon. For individual container, proxy has to be configured **again** while starting a new container, e.g.:
       
       `$ docker run --name <image-name> ... --env=HTTP_PROXY=<proxy_url> --env=<proxy_url> --env=NO_PROXY=<no_proxy_url>`
       
  4. Finish up:
   
       `$ systemctl daemon-reload`  
       `$ systemctl start docker`  
       `$ systemctl enable docker` 
  
__Mac__
* Legacy solution: Docker toolbox
  * docker machine - tool to create and manage dockerized virtual host(i.e. with docker engine on it).
  * docker engine - consists of docker daemon(RESTFUL API) and docker client(CLI).
  * docker compose - tool to define and run application configuration(such as dockerfile)
  * VirtualBox
  * Installation directory: /usr/local/bin
* New solution:
  * [Mac app](https://docs.docker.com/docker-for-mac/)
  * HyperKit(not VirtualBox)
  * Manage VM directly(no docker machine)
  * Installation directory:/Applications

__Windows__
* Legacy solution: Docker toolbox
  * docker machine - tool to create and manage dockerized virtual host(i.e. with docker engine on it).
  * docker engine - consists of docker daemon(RESTFUL API) and docker client(CLI).
  * docker compose - tool to define and run application configuration(such as dockerfile)
  * VirtualBox
* New solution:
  * [Windows app](https://docs.docker.com/docker-for-windows/)
