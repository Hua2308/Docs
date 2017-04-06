1. Get Instance ID by Name Tag:
```
aws --region us-east-1 ec2 describe-instances --filters 'Name=tag:Name,Values=<Instance_Name>' --query 'Reservations[].Instances[].InstanceId' --output text
```
Note: `--output text` removes square bracket from result.

2. Get Instance PrivateIp by Name Tag:
```
aws --region us-east-1 ec2 describe-instances --filters 'Name=tag:Name,Values=<Instance_Name>' --query 'Reservations[].Instances[].PrivateIpAddress' --output text
```
Note: `PrivateIpAddress` is case sensitive. `PRIVATEIPADDRESS` does NOT work.
