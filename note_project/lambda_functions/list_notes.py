import json
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    try:
        response = dynamodb.scan(TableName=table_name)
        items = response.get('Items', [])
        notes = [deserialize_item(item) for item in items]
        return {
            'statusCode': 200,
            'body': json.dumps(notes)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def deserialize_item(item):
    # Implement logic to deserialize a DynamoDB item to a Python dictionary
    # This should convert DynamoDB types to Python types as needed
    return {
        'noteId': item['noteId']['S'],
        'title': item['title']['S'],
        'content': item['content']['S'],
        'createdAt': item['createdAt']['S'],
        'updatedAt': item['updatedAt']['S']
    }
