from telegram import ctx
from telegram.App import App
import asyncio
import os

ok = App(command_prefix="!")
asyncio.run(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))


def hello(ctx):
    oa = ctx.update()
    ok = oa.message
    print(ok)
    if (ok == '!hello'):
        print(oa.message.chat.__dict__)
        oa.message.send_message(chat_id=oa.message.chat.chat_id, text="Hello")


hello(ctx)
asyncio.run(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
