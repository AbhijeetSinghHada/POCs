import boto3

dynamodb = boto3.client('dynamodb')

def create_table():
    dynamodb.create_table(
        TableName='destination_migration_table',
        KeySchema=[
            {
                'AttributeName': 'NODE',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'TYPE',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'NODE',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'TYPE',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    )
    dynamodb.waiter('table_exists').wait(TableName='destination_migration_table')


def fill_mock_data_in_db():
    for i in range(100, 150):
        print(f'Inserting item {i}')
        dynamodb.put_item(
            TableName='destination_migration_table',
            Item={
                'NODE': {
                    'S': str(i)
                },
                'TYPE': {
                    'S': f'name_{i}'
                }
            }
        )


def main():
    # create_table()
    fill_mock_data_in_db()

if __name__ == '__main__':
    main()