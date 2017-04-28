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
aws autoscaling describe-tags --query Tags[?Value=="'Your@EmailAddress'"].{AutoScalingGroupName:ResourceId} --output table
```
Note: ```"'Your@EmailAddress'"``` single quotes has to be inside double quotes, not the other way around or just one pair of quotes.

5. List Elastic Load Balancer by Contact tag:
```
# All elbs in one region
elblist=$(aws elb describe-load-balancers --query LoadBalancerDescriptions[*].LoadBalancerName --output text)
# 20 elbs
elbs=""
# consent engine elbs
consent_elbs=""
# counter of 20 for limitation
counter=0
for elb in $elblist; do
    elbs="$elbs $elb"
    counter=$((counter+1))
    if [ $counter -gt 19 ]; then
        consent_elbs="$consent_elbs $(aws elb describe-tags --load-balancer-name $elbs --query TagDescriptions[?Tags[?Value=="'Your@EmailAddress'"]].LoadBalancerName --output text)"
        elbs=""
        counter=0
    fi
done
aws elb describe-tags --load-balancer-name $consent_elbs --query TagDescriptions[?Tags[?Value=="'Your@EmailAddress'"]].{ElbName:LoadBalancerName} --output table

```

[Query Syntax Reference](http://jmespath.org/tutorial.html#filter-projections)
