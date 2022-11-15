from User import User
from content import content


class MessageEntity:
    def __init__(self):
        self.type: str = None
        self.offset: int = None
        self.length: int = None
        self.url: str = None
        self.user: User = None
        self.language: str = None
        self.custom_emoji_id: str = None

    def set_data(self, context):
        self.type: str = context(context, 'type')
        self.offset: int = context(context, 'offset')
        self.length: int = context(context, 'length')
        self.url: str = context(context, 'url')
        self.user: User = User().set_data(context['User'])
        self.language: str = context(context, 'language')
        self.custom_emoji_id: str = context(context, 'custom_emoji_id')
