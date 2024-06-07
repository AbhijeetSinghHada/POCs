import boto3

client = boto3.client('secretsmanager')

def get_secret(secret_name):
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

def main():
    secret_name = 'arn:aws:secretsmanager:ap-south-1:090824000808:secret:prod/secret-QONiKT'

    secret = get_secret(secret_name)
    print(secret)

if __name__ == "__main__":
    main()