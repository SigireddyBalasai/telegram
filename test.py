from telegram.App import App
import asyncio
from telegram.MessageMain import MessageSending
from telegram.Commands import Commands

bot = App(command_prefix="!")
from telegram.prase import Praser
from telegram import User


async def hello(ctx: Praser):
    ok = MessageSending()
    ok.text = 'hello'
    await ctx.message.replay(ok)

async def Audio(ctx:Praser):
    print(ctx.message.voice.file_id)


async def how_are_you(ctx: Praser):
    await ctx.message.replay("Fine")


Commands.add_command(hello)
Commands.add_command(Audio)
Commands.add_command(how_are_you)
bot.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0")
