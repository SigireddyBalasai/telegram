from main import content
class BotCommand:
    def __init__(self, context):
        context = context['result']
        keys = context.keys()
        print(keys)
        self.command : str  = content(context, 'command')
        self.description : str = content(context,'description')
