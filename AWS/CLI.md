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

3. List Instances Name/ID/AMI by Contact tag:
```
aws ec2 describe-instances --filters Name=tag:OwnerContact,Values=your@emailaddress --query "Reservations[].Instances[].{InstanceID:InstanceId, AMI:ImageId, Name:Tags[?Key=='Name']|[0].Value}" --output table
```
Note: `--output table` print a table view. `{InstanceID:InstanceId, AMI:ImageId, Name:Tags[?Key=='Name']|[0].Value}"` can be `[InstanceId, ImageId, Tags[?Key=='Name']|[0].Value]` to skip table head.

4. List AutoScalingGroup Name by Contact tag:
```
aws autoscaling describe-tags --query Tags[?Value=="'Earthquake@capitalone.com'"].{AutoScalingGroupName:ResourceId} --output table
```
Note: ```"'Earthquake@capitalone.com'"``` single quotes has to be inside double quotes, not the other way around of just one pair of quotes.

[Query Syntax Reference](http://jmespath.org/tutorial.html#filter-projections)
