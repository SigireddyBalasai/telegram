import builtins
from flask import Flask
import aiohttp
from aiohttp import web
import asyncio
from pyngrok import ngrok
from Update import ctx


async def hello(request):
    ctx.prase(await request.json())
class App:
    base_url = "https://api.telegram.org/bot"
    token: str
    answer: str
    commands = tuple()

    def __init__(self, command_prefix):
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
        routes = web.RouteTableDef()
        app = web.Application()
        http_tunnel = ngrok.connect(8443, bind_tls=True)
        url = http_tunnel.public_url
        baseurl = cls.base_url + token + f"/setWebhook?url={url}"
        cls.get(baseurl)
        app.add_routes([web.get('/', hello)])
        web.run_app(app,port=8443)


    @classmethod
    def command(func):
        def function(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        App.commands += (function,)
        print(App.commands)
        return function


def content(context, ids):
    try:
        if ids in context.keys():
            return context[ids]
        else:
            return None
    except:
        pass
