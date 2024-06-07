import difflib

def get_delta(old_records, new_records):
    """Returns the delta between the old and new records."""
    differ = difflib.Differ()
    delta = differ.compare(old_records.splitlines(keepends=True), new_records.splitlines(keepends=True))
    added_records = set()
    removed_records = set()
    for line in delta:
        if line.startswith('+ '):
            added_records.add(line[2:].replace('\n',''))
        if line.startswith('- '):
            removed_records.add(line[2:].replace('\n',''))
    updated_records = find_updated_records(added_records, removed_records)
    return updated_records


def find_updated_records(added_records, removed_records):
    """Returns the updated records from the delta."""
    # left join added and removed records
    updated_records = added_records - added_records.intersection(removed_records)
    return updated_records


        
    