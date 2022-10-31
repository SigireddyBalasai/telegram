from telegram.App import content, App
from telegram.Message import Message
import asyncio

class Update:
    RecentUpdate = None

    def __init__(self):
        self.count : int = 0
        self.update_id: int
        self.context = asyncio.run(self.__call__())

    async def __call__(self):

        if (Update.RecentUpdate == None):
            url = App.base_url + App.token + f"/getUpdates?limit=1"
        else:
            url = App.base_url + App.token + f"/getUpdates?offset={Update.RecentUpdate}?limit=1"
        context = await App.get(url)
        contexta = list(i for i in context['result'])

        Update.RecentUpdate: int = content(contexta[-1], 'update_id') -1
        self.update_id: int = content(contexta[-1], 'update_id')
        self.message = Message(contexta[-1]['message'])
        self.count += 1
        return self
