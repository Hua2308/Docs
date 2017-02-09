1. deploy project with dockerfile
  * create dockerfile 'my_project_docker_image'
    * FROM \<base_docker_image\>
    * COPY \<local_project_dir\> \<work_dir e.g. /usr/src/container_project_dir\>
  * run
    * docker run -w \<work_dir> my_project_docker_image \<init_command e.g. node install>
    * docker run -w \<work_dir\> -p \<host_port>:\<container_port\> my_project_docker_image \<init_command e.g. node app.js\>

2. deploy project without dockerfile
  * run
    * docker run -v \<local_project_dir e.g. "$PWD"\>:\<work_dir> -w \<work_dir\> \<base_docker_image\> \<init_command e.g. npm install\>
    * docker run -v \<local_project_dir e.g. "$PWD"\>:\<work_dir\> -w \<work_dir\> \<base_docker_image\> \<init_command e.g. npm app.js\>
