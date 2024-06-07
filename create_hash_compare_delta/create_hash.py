import hashlib
import csv
import hashlib
import csv
import os

def create_hash(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()

def add_hash_to_csv(file_path, hash_table_path):
    filename = file_path.split('\\')[-1]

    file_hash = create_hash(file_path)

    with open(hash_table_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([filename, file_hash])

# Usage example
folder_path = 'create_hash_compare_delta\hash_folder'
hash_table_path = 'hash_table.csv'

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    add_hash_to_csv(file_path, hash_table_path)