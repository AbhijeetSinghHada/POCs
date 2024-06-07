import asyncio
import time
import aiohttp

async def call_api(url,_):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            if response.status != 200:
                print(f"Error: {result} Call Count {_}")
            else:
                print(f"Call Count : {_}")

async def make_multiple_api_calls(url, num_calls):
    tasks = []
    for _ in range(num_calls):
        tasks.append(call_api(url, _))
    await asyncio.gather(*tasks)

async def main():
    url = "https://grdjwuudpk.execute-api.ap-south-1.amazonaws.com/dev/approval/MTcxMjc0NTc1MSMxNzE0NTQ1NDcz?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWJoaWplZXQgIiwiZXhwIjoxNzE0NTQ2MTM3LCJhcHByb3ZlciI6ImFiaGlqZWV0LmhhZGFAd2F0Y2hndWFyZC5jb20ifQ.I7CDOcUGuBHdPNG4TZaz0WTd8vZsmPBhEo0fxcVeVx4&action=approved"
    # url = "https://i8rsdkvo6b.execute-api.ap-south-1.amazonaws.com/dev/approval/MTcxMjY0MTc5NCMxNzE0MzgzODQ1?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWJoaXNoZWsgIiwiZXhwIjoxNzE0Mzg0NTEwLCJhcHByb3ZlciI6ImFiaGlqZWV0LmhhZGFAd2F0Y2hndWFyZC5jb20ifQ.ywQR8X4Ij7KjeQwhoiEHsb7xazWUxz0gw6z3EhIQ16M&action=approved"
    num_calls = 100
    await make_multiple_api_calls(url, num_calls)

if __name__ == "__main__":
    # for _ in range(5):
        # time.sleep(0.5)
        # asyncio.run(main())
    asyncio.run(main())