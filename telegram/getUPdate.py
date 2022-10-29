from main import App
import asyncio
import aiohttp
from telegram.update import Update


asyncio.run(App.run(token="5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
url = App.base_url+App.token+"/getUpdates"


async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            answer = await response.json()
            print(answer)
            context = list(i for i in answer['result'])
            print(Update(context[0]).__dict__)
            print(Update(context[0]).message.chat.__dict__)

print("Hello")
asyncio.run(hello(url))
