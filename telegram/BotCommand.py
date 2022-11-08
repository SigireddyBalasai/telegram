from content import content


class BotCommand:
    def __init__(self):
        self.description: str = None
        self.command: str = None

    def set_data(self, context):
        context = context['result']
        self.command: str = content(context, 'command')
        self.description: str = content(context, 'description')
