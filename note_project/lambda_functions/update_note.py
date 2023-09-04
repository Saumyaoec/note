import json
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    try:
        note_id = event['pathParameters']['noteId']
        note_data = json.loads(event['body'])
        # Check if the note with the given ID exists
        existing_item = dynamodb.get_item(
            TableName=table_name,
            Key={'noteId': {'S': note_id}}
        ).get('Item')

        if existing_item:
            dynamodb.put_item(
                TableName=table_name,
                Item=serialize_item(note_data)
            )
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Note updated successfully'})
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
