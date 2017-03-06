AMI Rehydration Steps:

1. In EC2 instance console, stop origin instance.

2. In EC2 instance console, choose 'launch more like this' and pick up the desired new AMI. (Other configs should remain the same)

3. In EBS volumes section, find EBS volume for origin instance (using EC2 ID), and detach it.
      * Optionally, create a snapshot from origin EBS volume as a backup.
  
4. In EBS volumes section, find EBS volume for new instance (using EC2 ID), and detach it.

5. In EBS volumes section, pick up original EBS volume and attach to new instance.
      * Specify the EC2 ID
      * Specify its path as root: __/dev/sda1__

6. In EC2 instance console, start new instance again. That's it!

7. Cleanup: original instance and new EBS volume.

8. Troubleshoot:
    * "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! ECDSA host key for 11.222.12.12 has changed and you have requested strict checking..." __Solution__: Edit local file /Users/name/.ssh/known_hosts to remove old instance IP address entry.
   
