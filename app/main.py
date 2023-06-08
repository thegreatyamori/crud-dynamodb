from fastapi import FastAPI

import typing
from .client import dynamo_client
from .dependency_injection import implementations_di

app = FastAPI()

def initialize_tables(client):
    table_name = 'miTabla'
    key_schema = [
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ]
    attribute_definitions = [
        {'AttributeName': 'id', 'AttributeType': 'S'}
    ]
    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

    client.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )

@app.get("/")
def check_health() -> typing.Dict:
    return {"status": "Ok"}

@app.get("/dynamo-create")
def dynamo_create() -> typing.Dict:
    initialize_tables(dynamo_client())
    return {"status": "table created"}

@app.get("/dynamo-add")
def dynamo_add() -> typing.Dict:
    item = {'id': '2', 'name': 'Victor', 'lastname': 'Morocho'}
    item_added = implementations_di.get_dynamo_implementation().add(
        'miTabla',
        **item
    )
    return item_added

@app.get("/dynamo-get/{id}")
def dynamo_get(id: str) -> typing.Dict:
    item = implementations_di.get_dynamo_implementation().get(
        'miTabla',
        id=id
    )
    return item

@app.get("/dynamo-delete/{id}")
def dynamo_get(id: str) -> typing.Dict:
    item = implementations_di.get_dynamo_implementation().delete(
        'miTabla',
        id=id
    )
    return item
