from telegram.App import App
import asyncio

loop = asyncio.new_event_loop()
ok = App(command_prefix="!")
loop.run_until_complete(ok.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))


@App.command()
async def hello(ctx):
    oa = await ctx.update()
    print(oa.__dict__)
    # if (ok == '!hello'):
    # print(oa.message.chat.__dict__)
    # oa.message.send_message(chat_id=oa.message.chat.chat_id, text="Hello")
