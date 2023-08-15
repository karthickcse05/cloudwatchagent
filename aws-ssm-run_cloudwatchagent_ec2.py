import boto3
import json

#change to the region you are looking up
region='us-east-1'
client = boto3.client('ssm', aws_access_key_id='',
    aws_secret_access_key='',
    #aws_session_token='',
    region_name=region)

response = client.send_command(
    InstanceIds=[''],
    DocumentName='AmazonCloudWatch-ManageAgent',
    DocumentVersion='7',
    Parameters={
        'action': [
            'configure',
        ],
        'mode': [
            'ec2',
        ],
        'optionalConfigurationSource': [
            'ssm',
        ],
        'optionalConfigurationLocation': [
            'AmazonCloudWatch-windows',
        ],
        'optionalRestart': [
            'yes',
        ]
    },
    TimeoutSeconds=600,
    MaxConcurrency='50',
    CloudWatchOutputConfig={
        'CloudWatchLogGroupName': 'Start-CloudWatch-Agent-Windows',
        'CloudWatchOutputEnabled': True
    },
)
#print(f"response is {response}")
print(f"command id is {response['Command']['CommandId']}")
feedback = client.get_command_invocation(CommandId=response['Command']['CommandId'], InstanceId='')
print(f"status is {feedback['StatusDetails']}")

