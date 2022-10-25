import aiohttp
import asyncio
import typing
import json
class App:
    base_url = "https://api.telegram.org/bot"
    token : str
    def __init__(self):
        self.token: str

    async def get(self,url):
        async with  aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                answer = await response.json()


    async def run(self,token):
        App.token = token
        self.loop = asyncio.get_event_loop()
        url = App.base_url+self.token+"/getMe"
        self.answer =await self.get(url)
        return self.answer

def content(context,id):
    if(id in context.keys()):
        return context[id]
    else:
        return None

class Message:
    hello = "hi"

