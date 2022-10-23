import aiohttp
import asyncio
import typing


class App:
    base_url = "https://api.telegram.org/bot"
    def __init__(self):
        self.token : str = None

    def run(self,token):
        self.token = token
 class User:
    def __init__(self, user_id :int):
        self.user_id : int = user_id
        self.is_bot : bool
  
