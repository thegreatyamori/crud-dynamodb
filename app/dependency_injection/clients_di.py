from ..clients import aws_client


def get_aws_client():
    return aws_client.AWSClient()
