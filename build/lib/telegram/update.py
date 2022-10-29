from Chat import Chat


def content(context,ids):
    if(ids in context.keys()):
        return context[ids]
    else:
        return None
class update():

    def __init__(selfself,context):
        self.update_id : int = content(context, 'update_id')
        self.message = Message(content['message'])
        self.chat = Chat(content['chat'])
