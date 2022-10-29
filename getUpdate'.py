from telegram.main import App
import asyncio
import aiohttp
from telegram.update import update
asyncio.run(App.run(token = "5764436314:AAHqvTxI4LLfkK6ilKC2Y4hEo-OW9-oM0g0"))
url = App.base_url+App.token+"/getUpdates"
async def hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            answer = await response.json()
            context = list(i for i in context['result'])
            for i in context:
                print(update(i).__dict__())
print("Hello")
asyncio.run(hello(url))