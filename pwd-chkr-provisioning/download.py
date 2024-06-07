import concurrent.futures
import requests

def download_link(url, basehash, session):  
    """Downloads the content for the given range and saves it to a file, using the provided session."""
    
    with session.get(url) as response:  
        save = ""
        for line in response.text.split():
            save += (basehash + line + '\n')

        with open('oldhashes/'+basehash + '.txt', 'w') as f:
            f.write(save)

def download_all():
    """Manages the concurrent downloading of ranges using a ThreadPoolExecutor and connection pooling."""

    baseurl = "https://api.pwnedpasswords.com/range/"

    with requests.Session() as session:  
        with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
            futures = []
            for index in range(0, 100):
                basehash = f'{index:x}'.zfill(5).upper()
                print(basehash)
                future = executor.submit(download_link, url=baseurl + basehash, basehash=basehash, session=session)  
                futures.append(future)
            
            concurrent.futures.wait(futures)

if __name__ == "__main__":
    download_all()
    
    print("All downloads completed!")
