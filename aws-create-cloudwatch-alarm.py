import boto3
import json

#change to the region you are looking up
region='us-east-1'
cloudwatch  = boto3.client('cloudwatch', aws_access_key_id='',
    aws_secret_access_key='',
    #aws_session_token='',
    region_name=region)

# Create alarm
response = cloudwatch.put_metric_alarm(
    AlarmName='Disk Utilization',
    AlarmDescription='Alarm for monitoring the  Disk Utilization when  exceeds 70%',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='LogicalDisk ''%'' Free Space',
    Namespace='CWAgent',
    Period=60,
    Statistic='Average',
    Threshold=35,
    ActionsEnabled=True,
    AlarmActions=[
        'arn:aws:sns:us-east-1:accountid:mymailsns',
    ],
    TreatMissingData='breaching',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': ''
        },
    ],
    Unit='Seconds'
)
print(f"response is {response}")
