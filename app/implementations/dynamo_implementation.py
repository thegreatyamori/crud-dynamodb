from cerealbox.dynamo import as_dynamodb_json
from ..clients.aws_client import AWSClient


class DynamoImplementation:
    def __init__(self, client: AWSClient) -> None:
        self.client = client.get_client('dynamodb')
    
    def __get_table(self, name: str):
        return self.client.Table(name)
    
    def scan_all(self, table_name: str):
        table = self.__get_table(table_name)
        return table.scan()

    def get(self, table_name: str, **kwargs):
        table = self.__get_table(table_name)
        response = table.get_item(Key=kwargs)
        return response.get('Item')
    
    def add(self, table_name: str, **kwargs):
        table = self.__get_table(table_name)
        body = as_dynamodb_json(kwargs)
        table.put_item(Item=body)
        return kwargs
        
    def update(self, table_name: str, id: str, **kwargs):
        table = self.__get_table(table_name)
        response = table.update_item(
            Key={'id': id},
            UpdateExpression=(
                'SET '
                ', '.join(f"{key} = :new{key}" for key in kwargs.keys())
            ),
            ExpressionAttributeValues={
                f":new{key}": value for (key, value) in kwargs.items()
            },
            ReturnValues="UPDATED_NEW"
        )
        return response['Attributes']
    
    def delete(self, table_name: str, **kwargs):
        table = self.__get_table(table_name)
        response = table.delete_item(Key=kwargs)
        return response.get('Item')
