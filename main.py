from pyrogram import Client, filters

app = Client(
    "ALEXXX",
    api_id=7132287,
    api_hash="d2d60a6c0a3e7715dd107f6e772d047d"
)

key_word = "БЮЛЕТЕНЬ СЕРЕДНЬОЗВАЖЕНИХ ЦІН"



#
# @app.on_message(filters.channel & filters.text)
# async def my_handler(client, message):
#     print(message)
#     print("=======================================")
#     if message['chat']['id'] == -1001585147403 and key_word in message['text']:
#         url = message['entities'][1]['url']
#         print(url)
#         # await message.forward("me")
#         await app.send_message("me", url)
#
#
# app.run()


# app.run()
#
# if __name__ == '__main__':
#     target = "ueex_lpg"  # Target channel/supergroup
#     print("sfsd")
#     print(app.get_history(target))
with app:
    t = app.get_chat("KyivOperativ")
    print(t)