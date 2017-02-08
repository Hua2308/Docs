1. Stop a container:
  * Check Container ID:  docker ps
  * Stop container: docker rm -fv <container_id>
    * -f flag is short for --force=false, which forces the removal of a running container. 
    * -v flag is short for --volumes=false, which removes the volumes associated with the container.

2. Disconnect client from server (while keep container running)
  * Check process ID: ps aux | grep docker
  * Kill process : kill -9 <process_id>

Reference: https://getcarina.com/docs/troubleshooting/stop-nonresponsive-running-container/
