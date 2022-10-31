from telegram.App import content
from Message import Message


class User:
    def __init__(self, context):
        context = context['result']
        keys = context.keys()
        print(keys)
        self.user_id: int = content(context, 'id')
        self.is_bot: bool = content(context, 'is_bot')
        self.first_name: str = content(context, 'first_name')
        self.last_name: str = content(context, 'last_name')
        self.username: str = content(context, 'username')
        self.language_code: str = content(context, 'language_code')
        self.is_premium: bool = content(context, 'is_premium')
        self.added_to_attachment_menu: bool = content(context, 'added_to_attachment_menu')
        self.can_join_groups: bool = content(context, 'can_join_groups')
        self.can_read_all_group_messages: bool = content(context, 'can_read_all_group_messages')
        self.supports_inline_queries: bool = content(context, 'supports_inline_queries')

    async def send_message(self, text):
        await Message.send_message(self.user_id, text)
