import os
from pyrogram import Client, filters
from parcer import get_data
from models import write_to_db


BOT_NAME = os.getenv('BOT_NAME')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PUBLIC_NAME = os.getenv('PUBLIC_NAME')

app = Client(
    BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH
)

key_word = "БЮЛЕТЕНЬ СЕРЕДНЬОЗВАЖЕНИХ ЦІН"


@app.on_message(filters.chat(PUBLIC_NAME) & filters.text)
async def my_handler(client, message):
    try:
        if key_word in message['text']:
            url = message['entities'][1]['url']
            data_list = await get_data(url)

        await write_to_db(data_list)
    except (IndexError, UnboundLocalError):
        print("incorrect url")
    # await app.send_message("me", data)


if __name__ == '__main__':
    app.run()
