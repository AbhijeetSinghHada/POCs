import csv
import multiprocessing

csv_file_path = 'hash_table.csv'

def write_random_filenames_and_hashes(filename):
    file_hash = '1e9a53eecafb3f0c7cbdeaa016d4708664cba3f34a61e2f2078f69537f5a08a4'
    return [filename, file_hash]

if __name__ == '__main__':
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        pool = multiprocessing.Pool(processes=4)
        filenames = [f"file_{i}.txt" for i in range(1000000)]
        results = pool.map(write_random_filenames_and_hashes, filenames)
        writer.writerows(results)
