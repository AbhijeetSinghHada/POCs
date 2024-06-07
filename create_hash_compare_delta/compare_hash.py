import os
import csv
import hashlib
from delta_generator import get_delta

hash_folder_path = 'create_hash_compare_delta\hash_folder'
compare_folder_path = 'create_hash_compare_delta\compare_folder'
csv_file_path = 'hash_table.csv'

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def compare_hashes(folder_path, csv_file_path):
    csv_data = {}
    with open(csv_file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            filename, hash_value = row
            csv_data[filename] = hash_value

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_hash = calculate_hash(file_path)
            if filename in csv_data:
                if file_hash == csv_data[filename]:
                    print(f"{filename}: Hash matches")
                else:
                    print(f"{filename}: Hash does not match")
                    print(f"Generating Diff for {filename}")
                    hash_file_path = os.path.join(hash_folder_path, filename)
                    compare_file_path = os.path.join(compare_folder_path, filename)
                    lines_changed = get_delta(hash_file_path, compare_file_path)
                    print(lines_changed)
            else:
                print(f"{filename}: File not found in CSV")


compare_hashes(compare_folder_path, csv_file_path)