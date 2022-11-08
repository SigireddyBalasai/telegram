from .User import User
from .Chat import Chat
#from .App import App
import datetime
from .Animation import Animation
from typing import Union
from .content import content


class Message:
    forwaded = None

    def __init__(self):
        self.date: Union[int, None] = None
        self.message_id: Union[int, None] = None
        self.from_user: Union[User, None] = None
        self.sender_chat: Union[Chat, None] = None
        self.chat: Union[int, None] = None
        self.forward_from: Union[User, None] = None
        self.forward_from_chat: Union[Chat, None] = None
        self.forward_from_message_id: Union[int, None] = None
        self.forward_signature: Union[str, None] = None
        self.forward_sender_name: Union[str, None] = None
        self.forward_date: Union[int, None] = None
        self.is_automatic_forward: Union[bool, None] = None
        self.reply_to_message: Union[Message, None] = None
        self.via_bot: Union[User, None] = None
        self.edit_date: Union[int, None] = None
        self.has_protected_content: Union[bool, None] = None
        self.media_group_id: Union[str, None] = None
        self.author_signature: Union[str, None] = None
        self.text: Union[str, None] = None
        self.animation: Union[Animation, None] = None

    def set_data(self, context: dict):
        self.message_id: int = content(context, 'id')
        self.from_user: User = User().set_data(content(context, 'from'))
        self.sender_chat: Chat = Chat().set_data(content(context, 'sender_chat'))
        self.date: int = content(context, 'date')
        self.chat: Chat = Chat().set_data(content(context, 'chat'))
        self.forward_from: User = User().set_data(content(context, 'forward_from'))
        self.forward_from_chat: Chat = Chat().set_data(content(context, 'forward_from_chat'))
        self.forward_from_message_id: int = content(context, 'forward_from_message_id')
        self.forward_signature: str = content(context, 'forward_signature')
        self.forward_sender_name: str = content(context, 'forward_sender_name')
        self.forward_date: int = content(context, 'forward_date')
        self.is_automatic_forward: bool = content(context, 'is_automatic_forward')
        # self.reply_to_message: Message = Message().set_data(content(context, 'reply_to_message'))
        self.via_bot: User = User().set_data(content(context, 'via_bot'))
        self.edit_date: int = content(context, 'edit_date') or None
        self.has_protected_content: bool = content(context, 'has_protected_content') or None
        self.media_group_id: str = content(context, 'media_group_id') or None
        self.author_signature: str = content(context, 'author_signature') or None
        self.text: str = content(context, 'text') or None
        self.animation: Animation = Animation().set_data(content(context, 'Animation'))
        return self

    @classmethod
    async def send_message(cls, chat_id, text, parse_mode: str = None, disable_web_page_preview: bool = True,
                           disable_notification: bool = True, protect_content: bool = False,
                           reply_to_message_id: int = None, allow_sending_without_reply: bool = True):
        url = App.base_url + App.token + f'/sendMessage?chat_id={chat_id}&text={text}&parse_mode={parse_mode}' \
                                         f'&disable_web_page_preview={disable_web_page_preview}' \
                                         f'&disable_notification={disable_notification}' \
                                         f'&protect_content={protect_content}' \
                                         f'&reply_to_message_id={reply_to_message_id}' \
                                         f'&allow_sending_without_reply={allow_sending_without_reply}'
        print(url)
        ans = await App.get(url)
        print(ans)
        cls.from_user = Message(ans['result']["from"])
        cls.chat = Chat(ans['result']['chat'])
        cls.message = ans['result']['text']
        cls.date = datetime.datetime.fromtimestamp(ans['result']['date'])
        cls.text = text

    @classmethod
    async def forward_message(cls, chat_id, from_chat_id, message_id: int, disable_notifications: bool = False,
                              protect_content: bool = False):
        url = App.base_url + App.token + f"/forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}" \
                                         f"&disable_notifications={disable_notifications}" \
                                         f"&protect_content={protect_content}&message_id={message_id}"
        print(url)
        ok = App()
        ans = await ok.get(url)
        print(ans)
        cls.forwaded = Message(ans)
        return cls.forwaded

    @classmethod
    async def copy_message(cls, chat_id, from_chat_id, message_id: int, caption: str = None,
                           disable_notifications: bool = False, parse_mode: str = None, replay_to_message_id=None,
                           allow_sending_without_replay: bool = False, protect_content: bool = False):
        url = App.base_url + App.token + f"/forwardMessage?chat_id={chat_id}&caption={caption}" \
                                         f"&from_chat_id={from_chat_id}&disable_notifications={disable_notifications}" \
                                         f"&protect_content={protect_content}&message_id={message_id}" \
                                         f"&parsemode={parse_mode}&replay_to_message_id={replay_to_message_id}" \
                                         f"&allow_sending_without_replay={allow_sending_without_replay}"
        print(url)
        ans = await App.get(url)
        print(ans)
