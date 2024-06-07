import os

EFS_MOUNT_PATHS = os.getenv("EFS_MOUNT_PATH")

def update_existing_file(new_response, basehash):
    """Updates the existing file with the new data."""
    
    with open(f'existing_hashed_passwords/{basehash}.txt', 'w') as f:
        f.write(new_response)

def check_exisiting_passwords_dir():
    """Checks if the existing_hashed_passwords directory exists, and creates it if it doesn't."""
    
    if not os.path.exists('existing_hashed_passwords'):
        os.makedirs('existing_hashed_passwords')