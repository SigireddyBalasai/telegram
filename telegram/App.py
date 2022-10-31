import aiohttp
import asyncio
from asyncio import coroutine


class App:
    base_url = "https://api.telegram.org/bot"
    token: str
    answer: str
    commands = tuple()

    def __init__(self,command_prefix):
        self.token: str
        self.command_prefix = command_prefix

    @classmethod
    async def get(cls, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                answer = await response.json()
                return answer

    @classmethod
    async def run(cls, token):
        App.token = token

    def command(func):
        async def function(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result
        App.commands += (function,)
        print(App.commands)
        return function


def content(context, ids):
    if ids in context.keys():
        return context[ids]
    else:
        return None
