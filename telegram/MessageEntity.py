from User import User
from App import content
class MessageEntity:
    def __init__(self):
        self.type: str=None
        self.offset: int=None
        self.length: int=None
        self.url: str=None
        self.user: User = None
        self.language: str=None
        self.custom_emoji_id: str=None

    def set(self,context):
        self.type: str = content(context, 'type')
        self.offset: int = content(context, 'offset')
        self.length: int = content(context, 'length')
        self.url: str = content(context,'url')
        self.user: User = User().set(context['User'])
        self.language: str = content(context, 'language')
        self.custom_emoji_id: str= content(context, 'custom_emoji_id')
