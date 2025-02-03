import boto3
import json
import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
client = boto3.client("secretsmanager", region_name=AWS_REGION)

def get_secret(secret_name):
    try:
        response = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in response:
            return json.loads(response['SecretString'])
        return response['SecretBinary']
    except Exception as e:
        raise Exception(f"Failed to retrieve secret: {str(e)}")
