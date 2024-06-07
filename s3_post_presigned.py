import boto3
import logging
from botocore.exceptions import ClientError

APPROVAL_S3_KEY = 'admin-portal-approval-record.json'
APPROVAL_S3_BUCKET = 'abhi-bucket-123'

def create_presigned_post(bucket_name, object_name, fields=None, conditions=None, expiration=3600):
    """
    Generate a presigned URL S3 POST request to upload a file
    :param bucket_name: string
    :param object_name: string
    :param fields: dictionary
    :param conditions: list
    :param expiration: int
    :return: dictionary
    """
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(
            Bucket=bucket_name,
            Key=object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration
        )
    except ClientError as e:
        logging.error(e)
        return None

    return response

def presigned_request():
    """
    Generate payload for and
    """
    payload = {
        'name' : "Abhijeet Singh Hada",
        'email' : 'abhi22hada@gmail.com',
        'phone' : '1234567890',
        'approver': 'admin'
    }

    s3_key = APPROVAL_S3_KEY
    presigned_post_resp = create_presigned_post(
        APPROVAL_S3_BUCKET, s3_key, fields={'file': payload}
    )
    return presigned_post_resp

def main():
    print(presigned_request())

if __name__ == '__main__':
    main()