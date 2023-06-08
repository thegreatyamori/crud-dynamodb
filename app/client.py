import os
import boto3


AWS_REGION = os.environ.get('AWS_REGION')
DYNAMO_ENDPOINT = os.environ.get('DYNAMO_ENDPOINT')

def dynamo_client():
    options = {
        "endpoint_url": DYNAMO_ENDPOINT, 
        "region_name": AWS_REGION,
    }
    return boto3.client('dynamodb', **options)
