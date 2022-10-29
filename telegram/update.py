
from main import content
from Message import Message


class Update:
    def __init__(self, context):
        self.update_id: int = content(context, 'update_id')
        self.message = Message(context['message'])
