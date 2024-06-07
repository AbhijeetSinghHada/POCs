import os
import logging
import requests
import concurrent.futures
from helpers.ddb import ProvisioningDDB
from utils.comparison import get_delta
from wg_python_utils.log.setup import init_logging
from helpers.file_helpers import check_exisiting_passwords_dir, update_existing_file

# set log file
logging.basicConfig(filename='pwd-chkr-provisioning.log', level=logging.INFO)
init_logging("pwd-chkr-provisioning")

logger = logging.getLogger("pwd-chkr-provisioning")
ddb = ProvisioningDDB()

def worker(url, basehash, session):  
    """Downloads the content for the given range and saves it to a file, using the provided session."""
    
    new_response = ""
    is_update_successful = False
    with session.get(url) as response:  
        for line in response.text.split():
            new_response += (basehash + line + '\n')
    if os.path.exists(f'./existing_hashed_passwords/{basehash}.txt'): # existing_hashed_passwords
        old_file_data = open(f'./existing_hashed_passwords/{basehash}.txt').read()
        diff = get_delta(old_file_data, new_response)
        is_update_successful = ddb.update_records(diff)
    else:
        logger.info(f"File {basehash}.txt not found")
        is_update_successful = ddb.update_records(new_response)

    if is_update_successful:
        update_existing_file(new_response, basehash)
        

def main():
    """Manages the concurrent downloading of ranges using a ThreadPoolExecutor and connection pooling."""

    baseurl = "https://api.pwnedpasswords.com/range/"
    check_exisiting_passwords_dir()
    with requests.Session() as session:  
        with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
            futures = []
            for index in range(0, 1):
                basehash = f'{index:x}'.zfill(5).upper()
                print(basehash)
                future = executor.submit(worker, url=baseurl + basehash, basehash=basehash, session=session)  
                futures.append(future)
            
            concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
    
    print("Completed :)")
