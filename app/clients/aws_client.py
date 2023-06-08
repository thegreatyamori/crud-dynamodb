import os
import boto3


class AWSClient:
    def __init__(self) -> None:
        self.region_name = os.environ.get('AWS_REGION')
        self.endpoint_url = os.environ.get('DYNAMO_ENDPOINT')

    def get_client(self, resource):
        options = {
            "endpoint_url": self.endpoint_url, 
            "region_name": self.region_name,
        }
        return boto3.resource(resource, **options)
