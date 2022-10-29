from main import content


# from Message import Message
class Chat:
    def __init__(self, context):
        self.chat_id: int = content(context, 'id')
        self.type: str = content(context, 'type')
        self.title: str = content(context, 'title')
        self.username: str = content(context, 'username')
        self.first_name: str = content(context, 'first_name')
        self.last_name: str = content(context, 'last_name')
        # self.photo = ChatPhoto()
        self.bio: str = content(context, 'bio')
        self.has_private_forwards: bool = content(context, 'has_private_forwards')
        self.has_restricted_voice_and_video_messages: bool = content(context, 'has_restricted_voice_and_video_messages')
        self.join_to_send_messages: bool = content(context, 'join_to_send_messages')
        self.join_by_request: bool = content(context, 'join_by_request')
        self.description: str = content(context, 'description')
        self.invite_link: str = content(context, 'invite_link')
        # self.pinned_message = Message()
        # self.permissions = ChatPermissions()
        self.slow_mode_delay: int = content(context, 'slow_mode_delay')
        self.message_auto_delete_time: int = content(context, "message_auto_delete_time")
        self.has_protected_content: bool = content(context, 'has_protected_content')
        self.sticker_set_name: str = content(context, 'sticker_set_name')
        self.can_set_sticker_set: bool = content(context, 'can_set_sticker_set')
        self.linked_chat_id: int = content(context, 'linked_chat_id')
        # self.location = Location()
