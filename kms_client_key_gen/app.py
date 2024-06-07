import base64
import binascii
import boto3

def _generate_random_string(kms_client):
    # Use KMS to generate random 
    
    random_bytes_response = kms_client.generate_random(NumberOfBytes=46)
    hex_data = binascii.hexlify(random_bytes_response["Plaintext"]).decode('utf-8')
    
    print(hex_data)

    api_access_info = {
        "access_id": hex_data[:16] + "_id",
        "access_pwd": hex_data[16:32] + "_PWD",
        "api_key_id": base64.b64encode(bytes.fromhex(hex_data[32:])).decode('utf-8')
    }
    print(api_access_info)

if __name__ == "__main__":
    
    kms_client = boto3.client("kms")
    _generate_random_string(kms_client)