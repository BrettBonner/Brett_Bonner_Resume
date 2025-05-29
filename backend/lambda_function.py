import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("visitor_count")

def lambda_handler(event, context):
    # TODO implement
    response = table.update_item(
        #Row I want to update
        Key={'id': 'resume'},
        UpdateExpression='Set #c = if_not_exists(#c, :start) + :inc',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':inc': 1, ':start': 0},
        ReturnValues='UPDATED_NEW'
    )
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps({'count': int(response['Attributes']['count'])})
    }
