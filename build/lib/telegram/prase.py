from .Message import Message
from .content import content
from typing import Union
from MessageMain import Message

class Praser:
    def __init__(self):
        self.edited_channel_post: Union[Message, None] = None
        self.channel_post: Union[Message, Union] = None
        self.edited_message: Union[Message, Union] = None
        self.message: Union[Message, Union] = None
        self.update_id: Union[Message, Union] = None

    def prase(self, context: object) -> object:
        self.update_id: int = content(context, 'update_id')
        self.message: Message = Message().set_data(content(context, 'message'))
        self.edited_message: Message = Message().set_data(content(context, 'edited_message'))
        self.channel_post: Message = Message().set_data(content(context, 'channel_post'))
        self.edited_channel_post: Message = Message().set_data(content(context, 'edited_channel_post'))
        return self
