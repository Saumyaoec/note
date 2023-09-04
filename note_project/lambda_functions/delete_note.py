import json
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    try:
        note_id = event['pathParameters']['noteId']
        # Check if the note with the given ID exists
        existing_item = dynamodb.get_item(
            TableName=table_name,
            Key={'noteId': {'S': note_id}}
        ).get('Item')

        if existing_item:
            dynamodb.delete_item(
                TableName=table_name,
                Key={'noteId': {'S': note_id}}
            )
            return {
                'statusCode': 204,
                'body': json.dumps({'message': 'Note deleted successfully'})
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
