from .User import User
from .Chat import Chat
from .response import get_request
from .Animation import Animation
from typing import Union
from .content import content
from .Tokensaver import TokenSaver


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
        self.message_id: int = content(context, 'message_id')
        self.from_user: User = User().set_data(content(context, 'from'))
        self.sender_chat = Chat().set_data(content(context, 'sender_chat'))
        self.date: int = content(context, 'date')
        self.chat = Chat().set_data(content(context, 'chat'))
        self.forward_from: User = User().set_data(content(context, 'forward_from'))
        self.forward_from_chat = Chat().set_data(content(context, 'forward_from_chat'))
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
    async def send_message(cls, chat_id: int, text: object, message_thread_id: int, parse_mode: str = None,
                           disable_web_page_preview: bool = True,
                           disable_notification: bool = True, protect_content: bool = False,
                           reply_to_message_id: int = Union[None, int],
                           allow_sending_without_reply: bool = True):
        url = TokenSaver.base_url + TokenSaver.token + f'/sendMessage?chat_id={chat_id}&text={text}' \
                                                       f'&parse_mode={parse_mode}' \
                                                       f'&disable_web_page_preview={disable_web_page_preview}' \
                                                       f'&message_thread_id={message_thread_id}' \
                                                       f'&disable_notification={disable_notification}' \
                                                       f'&protect_content={protect_content}' \
                                                       f'&reply_to_message_id={reply_to_message_id}' \
                                                       f'&allow_sending_without_reply={allow_sending_without_reply}'
        print(url)
        ans = await get_request(url)
        print(ans)
        """cls.from_user = Message(ans['result']["from"])
        cls.chat = Chat(ans['result']['chat'])
        cls.message = ans['result']['text']
        cls.date = datetime.datetime.fromtimestamp(ans['result']['date'])
        cls.text = text"""

    async def forward(self, user: User):
        await Message.forward_message(chat_id=user.user_id, from_chat_id=self.from_user.user_id)

    @classmethod
    async def forward_message(cls, chat_id, from_chat_id, message_id: int, disable_notifications: bool = False,
                              protect_content: bool = False):
        url = TokenSaver.base_url + TokenSaver.token + f"/forwardMessage?chat_id={chat_id}&" \
                                                       f"from_chat_id={from_chat_id}" \
                                                       f"&disable_notifications={disable_notifications}" \
                                                       f"&protect_content={protect_content}&message_id={message_id}"
        """
        print(url)
        ok = App()
        ans = await ok.get(url)
        print(ans)
        cls.forwaded = Message(ans)
        return cls.forwaded
        """

    @classmethod
    async def copy_message(cls, chat_id, from_chat_id, message_id: int, caption: str = None,
                           disable_notifications: bool = False, parse_mode: str = None, replay_to_message_id=None,
                           allow_sending_without_replay: bool = False, protect_content: bool = False):
        url = TokenSaver.base_url + TokenSaver.token + f"/forwardMessage?chat_id={chat_id}&caption={caption}" \
                                                       f"&from_chat_id={from_chat_id}&" \
                                                       f"disable_notifications={disable_notifications}" \
                                                       f"&protect_content={protect_content}&message_id={message_id}" \
                                                       f"&parsemode={parse_mode}&" \
                                                       f"replay_to_message_id={replay_to_message_id}" \
                                                       f"&allow_sending_without_replay={allow_sending_without_replay}"
        print(url)
        ans = await get_request(url)
        print(ans)

    async def replay(self, text, parse_mode: str = None, disable_web_page_preview: bool = True,
                     disable_notification: bool = True, protect_content: bool = False,
                     reply_to_message_id: bool = None, allow_sending_without_reply: bool = True):
        await Message.send_message(self.chat, text, parse_mode, disable_web_page_preview,
                                   disable_notification, protect_content,
                                   reply_to_message_id, allow_sending_without_reply)

    @classmethod
    async def send_photo(cls, chat_id: int, photo: str,
                         caption: str,
                         disable_web_page_preview: bool = True,
                         disable_notification: bool = True, protect_content: bool = False, parse_mode: str = None,
                         message_thread_id: int = None,
                         reply_to_message_id: int = None, allow_sending_without_reply: bool = True) -> object:
        url = TokenSaver.base_url + TokenSaver.token + f'/sendPhoto?chat_id={chat_id}' \
                                                       f'&photo={photo}' \
                                                       f'&parse_mode={parse_mode}' \
                                                       f'&disable_web_page_preview={disable_web_page_preview}' \
                                                       f'&disable_notification={disable_notification}' \
                                                       f'&protect_content={protect_content}' \
                                                       f'&reply_to_message_id={reply_to_message_id}' \
                                                       f'&caption={caption}' \
                                                       f'&allow_sending_without_reply={allow_sending_without_reply}' \
                                                       # f'message_thread_id={message_thread_id}'
        print(url)
        ans = await get_request(url)
        print(ans)

    async def replay_with_photo(self, photo,
                                caption: Union[None, str],
                                disable_web_page_preview: bool = True,
                                disable_notification: bool = True, protect_content: bool = False,
                                allow_sending_without_reply: bool = True):
        print(self.message_id)
        await Message.send_photo(chat_id=self.chat.chat_id, allow_sending_without_reply=allow_sending_without_reply,
                                 caption=caption, disable_web_page_preview=disable_web_page_preview,
                                 disable_notification=disable_notification, protect_content=protect_content,
                                 reply_to_message_id=self.message_id, photo=photo
                                 )
