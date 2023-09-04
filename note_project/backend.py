from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from botocore.exceptions import NoCredentialsError
import boto3
import os

User = get_user_model()

class CognitoAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        try:
            client = boto3.client(
                'cognito-idp',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                region_name=os.getenv('COGNITO_REGION')
            )

            response = client.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password,
                    'SECRET_HASH': 'YOUR_SECRET_HASH',  # Generate this based on your app client secret
                },
                ClientId=os.getenv('COGNITO_APP_CLIENT_ID')
            )

            if 'AuthenticationResult' in response:
                return User.objects.get_or_create(username=username)[0]

        except NoCredentialsError:
            pass

        return None
