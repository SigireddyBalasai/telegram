import aiohttp
import json


async def get_request(url: str) -> json:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            answer = await response.json()
    return answer



