###To install the Amazon ECS container agent on a non-Amazon Linux EC2 instance (digest version)

Steps:

1. Install Docker
  * [Instructions](https://github.com/Hua2308/Docs/blob/master/Docker/installation.md)
  
2. Set up directories, and necessary rules to enable IAM roles for tasks
  ```
  $ mkdir -p /var/log/ecs /etc/ecs /var/lib/ecs/data
  $ touch /etc/ecs/ecs.config
  $ sysctl -w net.ipv4.conf.all.route_localnet=1
  $ iptables -t nat -A PREROUTING -p tcp -d 169.254.170.2 --dport 80 -j DNAT --to-destination 127.0.0.1:51679
  $ iptables -t nat -A OUTPUT -d 169.254.170.2 -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 51679
  ```
  
3. Run the agent
  ```bash
  sudo docker run --name ecs-agent \
  --detach=true \
  --restart=on-failure:10 \
  --volume=/var/run/docker.sock:/var/run/docker.sock \
  --volume=/var/log/ecs/:/log \
  --volume=/var/lib/ecs/data:/data \
  --net=host \
  --env=ECS_LOGFILE=/log/ecs-agent.log \
  --env=ECS_LOGLEVEL=info \
  --env=ECS_DATADIR=/data \
  --env=ECS_ENABLE_TASK_IAM_ROLE=true \
  --env=ECS_ENABLE_TASK_IAM_ROLE_NETWORK_HOST=true \
  # Fill in cluster name
  --env=ECS_CLUSTER=<HERE_IS_CLUSTER_NAME_TO_REPLACE> \
  # Add http proxy if needed
  --env=HTTP_PROXY=<PROXY_URL>
  --env=HTTPS_PROXY=<PROXY_URL>
  --env=NO_PROXY=<NO_PROXY_URL>
  amazon/amazon-ecs-agent:latest
  ```

4. Verify agent is up and running:

  `$ sudo curl http://localhost:51678/v1/metadata` (it has to run with root permission)


* Reference: 
  * [Installing the Amazon ECS Container Agent](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-install.html)
  * [Container Agent source code](https://github.com/Hua2308/Docs/blob/master/Docker/installation.md)

