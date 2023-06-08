from ..implementations import dynamo_implementation
from .clients_di import get_aws_client


def get_dynamo_implementation():
    return dynamo_implementation.DynamoImplementation(
        client=get_aws_client()
    )
