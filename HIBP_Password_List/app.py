import asyncio
import aiohttp
from aiohttp.client import ClientSession
 
async def download_link(url:str, session:ClientSession, basehash:str):
    async with session.get(url) as response:
        save = ''
        result = await response.text()
        for line in result.split():
            hashes = (basehash+line+'\n')
            save += hashes
        with open(basehash+'.txt', 'w') as f:
            f.write(save)
       
async def download_all():
    baseurl = "https://api.pwnedpasswords.com/range/"
    my_conn = aiohttp.TCPConnector(limit=64) #adjust as needed
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for index in range(0,2):
            basehash = f'{index:x}'.zfill(5).upper()
            print (basehash)
            task = asyncio.ensure_future(download_link(url=baseurl+basehash,session=session,basehash=basehash))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True)
 
save = ''
asyncio.run(download_all())
# with open('your_file.txt', 'w') as f:
#     f.write(save)

