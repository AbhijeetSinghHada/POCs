import os
import logging
from boto3.dynamodb.conditions import Key, Attr
from wg_python_utils.dynamodb.dynamodb_helper import DDBApi


logger = logging.getLogger("pwd-chkr-provisioning")
# TABLE_NAME = os.getenv("TABLE_NAME")
# DEPLOY_REGION = os.getenv("AWS_REGION")

# if TABLE_NAME is None:
#     raise ValueError("TABLE_NAME not present in environment!")
# if DEPLOY_REGION is None:
#     raise ValueError("DEPLOY_REGION not present in environment!")

TABLE_NAME = "pwd-chkr-provisioning-DB"
DEPLOY_REGION = "us-west-2"

class Settings:
    DDB_MAX_RETRIES = 3
    DDB_RETRY_SLEEP_TIME = 2


class ProvisioningDDB(DDBApi):
    def __init__(self, endpoint_url=None):
        DDBApi.__init__(
            self,
            table_name=TABLE_NAME,
            settings=Settings,
            region_name=DEPLOY_REGION,
            endpoint_url=endpoint_url,
        )


    def update_records(self, records: str | set):
        """Updates the records in the DynamoDB table."""
        failed_records = []
        if isinstance(records, str):
            records = records.split('\n')
        for record in records:
            hash_value, count = record.split(':')
            hash_root = hash_value[:5]
            hash_tail = hash_value[5:]
            try:
                print(hash_root, hash_tail, count)
                # self._update_records(hash_root, hash_tail, count)
            except Exception as e:
                logger.error(f"Failed to update record: {record}. Error: {e}")
                failed_records.append(record)
        if failed_records:
            logger.error(f"Failed to update records: {failed_records}")
            return False
        return True


    def _update_records(self, hash_root, hash_tail, count):
        key = {'HashRoot': hash_root, 'HashTail': hash_tail}
        update_expression = "SET #hash_count = :hash_count"
        update_expression_values = {":hash_count": count}
        update_attribute_name = {"#hash_count": "count"}

        self._put_item(key, update_expression, update_expression_values, update_attribute_name)

    