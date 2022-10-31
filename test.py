#from telegram.Update import ctx
from telegram.App import App
import asyncio
import os
from telegram.Update import Update
ok = App(command_prefix="!")
asyncio.run(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
ctx = Update()
async def hello(ctx):
    oa = await (ctx())
    print(oa.__dict__)
    ok = oa.message.text
    print(ok)
    if(ok== '!hello'):
        print(oa.message.chat.__dict__)
        await oa.message.send_message(chat_id = oa.message.chat.chat_id, text="Hello")

while True:
    try:
        asyncio.run(hello(ctx))
        asyncio.run(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
    except:
        os.system('python test.py')
