from telegram.App import content, App
from telegram.Message import Message
import asyncio
import os
loop = asyncio.new_event_loop()

class Update:
    RecentUpdate: int = 0

    def __init__(self):
        self.update_id = None
        self.count: int = 0
        self.message: Message = None
        self.edited_message: Message = None
        self.channel_post: Message = None
        self.edited_channel_post: Message = None

    def prase(self, context):
        self.update_id: int = content(context['result'][-1], 'update_id')
        Update.RecentUpdate = self.update_id
        self.message: Message = Message(content(context['result'][-1], 'message'))
        self.edited_message: Message = Message(content(context['result'][-1], 'edited_message'))
        self.channel_post: Message = Message(content(context['result'][-1], 'channel_post'))
        self.edited_channel_post: Message = Message(content(context['result'][-1], 'edited_channel_post'))
        print(self.__dict__)

    def update(self):
        if Update.RecentUpdate:
            url = App.base_url + App.token + f"/getUpdates?offset={Update.RecentUpdate}"
        else:
            url = App.base_url + App.token + f"/getUpdates"
            print(url)
        response = loop.run_until_complete(App.get(url))
        # print(response)
        self.prase(response)
        return self


