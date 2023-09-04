import json
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    try:
        note_id = event['pathParameters']['noteId']
        response = dynamodb.get_item(
            TableName=table_name,
            Key={'noteId': {'S': note_id}}
        )
        item = response.get('Item')
        if item:
            note = deserialize_item(item)
            return {
                'statusCode': 200,
                'body': json.dumps(note)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Note not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
