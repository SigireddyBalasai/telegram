import aiohttp
import asyncio
import typing
import json
class App:
    base_url = "https://api.telegram.org/bot"
    token : str
    answer : str
    def __init__(self):
        self.token: str
    @classmethod
    async def get(cls,url):
        async with  aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                answer = await response.json()
                return answer

    @classmethod
    async def run(cls,token):
        App.token = token
        loop = asyncio.get_event_loop()
        url = App.base_url+App.token+"/deleteWebhook"
        cls.answer =await cls.get(url)
        return cls.answer

def content(context,id):
    if(id in context.keys()):
        return context[id]
    else:
        return None

class Message:
    hello = "hi"

