import json
import uuid
import boto3

dynamodb = boto3.client('dynamodb')
table_name = 'your-dynamodb-table-name'

def lambda_handler(event, context):
    try:
        note_data = json.loads(event['body'])
        note_id = str(uuid.uuid4())
        note_data['noteId'] = note_id
        dynamodb.put_item(
            TableName=table_name,
            Item=serialize_item(note_data)
        )
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Note created successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def serialize_item(note):
    # Implement logic to serialize a Python dictionary to a DynamoDB item
    # This should convert Python types to DynamoDB types as needed
    return {
        'noteId': {'S': note['noteId']},
        'title': {'S': note['title']},
        'content': {'S': note['content']},
        'createdAt': {'S': note['createdAt']},
        'updatedAt': {'S': note['updatedAt']}
    }
