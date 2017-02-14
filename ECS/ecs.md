1. ALB/ELB:
  * ALB can connect to one service running tasks in different ports. (same ecs instance)
      * e.g. ALB -> service(task1:80, task2:443....)
  * ELB can connect to one service running tasks in same port
      * e.g. ELB1 -> service(task1:80, task2:80...)
      * ELB2 -> service(task1:443, task2:443)
      
2. ECS:
  * Scheduling
      * ECS monitors container instances and recover any unhealthy one.
      * Once upload a new Task Definition(new version), ECS will automatically stop the container instance running old image/deregister it from ELB, and start a new container instance running new image/register it with ELB.
