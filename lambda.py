import json
import logging
import boto3
from botocore.exceptions import ClientError


def handler(event, context):
    msg = 'Vijay'
                msg = json.loads(event["body"])
                msg = msg["message"]
                client= boto3.client("dynamodb")
                connection_id=event.get('requestContext', {}).get('connectionId')
                client.put_item(TableName="MVC_MESSAGE",Item={"connectionId":{"S":connection_id},"message":{"S":msg}})
                #print(connection_id)
                
                URL = 'https://8b4sl98zw5.execute-api.us-east-2.amazonaws.com/production/'
                apig_management_client = boto3.client('apigatewaymanagementapi', endpoint_url=URL)
                apig_management_client.post_to_connection(ConnectionId=connection_id,
                Data=json.dumps({"Violent Communication ":msg}))
                return {
        'body': json.dumps('Please, '+msg)

    return None
