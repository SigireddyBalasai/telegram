from .content import content
from typing import Union
from .MessageMain import Message


class Praser:
    def __init__(self):
        self.edited_channel_post : Union[Message, None] = None
        self.channel_post: Union[Message, Union] = None
        self.edited_message: Union[Message, Union] = None
        self.message: Union[Message, Union] = None
        self.update_id: Union[Message, Union] = None

    def prase(self, context: dict) -> object:
        if 'update_id' in context.keys():
            self.update_id: int = content(context, 'update_id')
        if 'message' in context.keys():
            self.message: Message = Message(context['message'])
        if 'edited_message' in context.keys():
            self.edited_message: Message = Message(context['edited_message'])
        if 'channel_post' in context.keys():
            self.channel_post: Message = Message(context['channel_post'])
        if 'edited_channel_post' in context.keys():
            self.edited_channel_post: Message = Message(context['edited_channel_post'])
        return self
