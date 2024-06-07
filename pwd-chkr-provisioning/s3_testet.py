import gzip
from amazon.ion import simpleion

def read_file():
    with gzip.open('s3_data\\AWSDynamoDB\\abc\\data\\5wrxmtoly44itfqxemi5gfie3a.json.gz', 'rb') as f:
        for line in f:
            item = simpleion.loads(line)
            print(item)
    
# add more data to ion file

# data_item = {'Item': {'NODE':{'S': 'bhijeet'},'TYPE': {'S': 'Hada'}}}

# with gzip.open('DynamoDbExportEdit\\AWSDynamoDB
# \\01713865785529-ba8df9a7\\data\\e2f4ziqwyizhromzspz4uine2i.json.gz', 'ab') as f:
#     f.write(simpleion.dumps(data_item))


read_file()

