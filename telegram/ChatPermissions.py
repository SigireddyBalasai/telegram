from telegram.src.App import content


class BotCommand:
    def __init__(self, context):
        context = context['result']
        keys = context.keys()
        print(keys)
        self.can_send_messages: bool = content(context, 'can_send_messages')
        self.can_send_media_messages: bool = content(context, 'can_send_media_messages')
        self.can_send_polls: bool = content(context, 'can_send_polls')
        self.can_send_other_messages: bool = content(context, 'can_send_other_messages')
        self.can_add_web_page_previews: bool = content(context, 'can_add_web_page_previews')
        self.can_change_info: bool = content(context, 'can_change_info')
        self.can_invite_users: bool = content(context, 'can_invite_users')
        self.can_pin_messages: bool = content(context, 'can_pin_messages')
