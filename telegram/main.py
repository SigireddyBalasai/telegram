import aiohttp


class App:
    base_url = "https://api.telegram.org/bot"
    token: str
    answer: str

    def __init__(self):
        self.token: str

    @classmethod
    async def get(cls, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                answer = await response.json()
                return answer

    @classmethod
    async def run(cls, token):
        App.token = token
        url = App.base_url + App.token + "/deleteWebhook"
        cls.answer = await cls.get(url)
        return cls.answer


def content(context, ids):
    if ids in context.keys():
        return context[ids]
    else:
        return None


class Message:
    hello = "hi"
