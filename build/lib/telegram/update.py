from telegram.App import content, App
from telegram.Message import Message


class Update:
    RecentUpdate = None

    def __init__(self):
        self.update_id: int

    async def __call__(self):
        if (Update.RecentUpdate == None):
            url = App.base_url + App.token + f"/getUpdates"
        else:
            url = App.base_url + App.token + f"/getUpdates&offset={Update.RecentUpdate}"
        print(url)
        context = await App.get(url)
        print(context)

        context = list(i for i in context['result'])
        print(context)
        Update.RecentUpdate: int = content(context[0], 'update_id')
        self.update_id: int = content(context[0], 'update_id')
        self.message = Message(context['message'])
