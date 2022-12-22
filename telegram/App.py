import aiohttp
from aiohttp import web
import asyncio
from .Tokensaver import TokenSaver
from typing import Union
from pyngrok import ngrok
from .Update import Server
loop = asyncio.get_event_loop()

class App:
    base_url = "https://api.telegram.org/bot"
    token: str

    def __init__(self, command_prefix):
        self.base_url = "https://api.telegram.org/bot"
        self.token: str
        self.command_prefix = command_prefix

    def run(self, token):
        App.token = token
        self.token = token
        TokenSaver(token,self.command_prefix)
        server = Server(base_url=self.base_url, token=self.token)
        running_server = loop.run_until_complete(server.run())
        runner = aiohttp.web.AppRunner(running_server)
        loop.run_until_complete(runner.setup())
        site = aiohttp.web.TCPSite(runner,host="127.0.0.1", port=8443)
        loop.run_until_complete(site.start())
        loop.run_until_complete(asyncio.Event().wait())

