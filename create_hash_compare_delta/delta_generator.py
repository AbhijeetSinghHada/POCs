import difflib

def get_delta(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        # new_files_content = file1.readlines()
        # old_files_content = file2.readlines()
        # differ = difflib.Differ()
        # delta = list(differ.compare(new_files_content, old_files_content))
        delta = difflib.ndiff(file1.readlines(), file2.readlines())
        print(f"Length of delta: {len(delta)}")
    lines_changed = []   
    for line in delta:
        if line.startswith(('+ ', '- ','? ')):
            lines_changed.append(line)
            print(line)
    return lines_changed

file1_path = 'create_hash_compare_delta\\hash_folder\\file copy.txt'
file2_path = 'create_hash_compare_delta\\compare_folder\\file copy.txt'

get_delta(file1_path, file2_path)