# Credits to Achu biju

import asyncio
import tgcrypto

from pyrogram import Client

print("Made For")
print("")
print('''
Died''')
print("")
print('''
nothing                         
''')
print("")
print("Enter All Required Things To Generate String Session.")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
