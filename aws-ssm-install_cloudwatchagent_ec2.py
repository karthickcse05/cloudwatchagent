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
    DocumentName='AWS-ConfigureAWSPackage',
    DocumentVersion='1',
    Parameters={
        'action': [
            'Install',
        ],
        'installationType': [
            'Uninstall and reinstall',
        ],
        'name': [
            'AmazonCloudWatchAgent',
        ]
    },
    TimeoutSeconds=600,
    MaxConcurrency='50'
)
#print(f"response is {response}")
print(f"command id is {response['Command']['CommandId']}")
feedback = client.get_command_invocation(CommandId=response['Command']['CommandId'], InstanceId='')
print(f"status is {feedback['StatusDetails']}")

