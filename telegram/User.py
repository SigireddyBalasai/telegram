from .content import content


class User:
    def __init__(self):
        self.added_to_attachment_menu = None
        self.is_premium = None
        self.username = None
        self.last_name = None
        self.can_join_groups = None
        self.supports_inline_queries = None
        self.can_read_all_group_messages = None
        self.language_code = None
        self.first_name = None
        self.is_bot = None
        self.user_id = None

    def set_data(self, context):
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
        return self
