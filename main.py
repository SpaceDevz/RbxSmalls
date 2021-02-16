from ro_py import Client
import asyncio

client=Client()

async def main():
    print(await client.get_asset(494291269))

asyncio.get_event_loop().run_until_complete(main())

