import typing

from telegram.BaseClasses.Message_base import Base_Message, MessageSending
from telegram.BaseClasses.Chat_base import BaseChat
from telegram.BaseClasses.User_base import BaseUser
from telegram.Tokensaver import TokenSaver
from telegram.User import User
from telegram.response import get_request


class Message(Base_Message):

    def __init__(self):
        self.via_bot: typing.Union[BaseUser, None] = None
        self.sender_chat: typing.Union[BaseChat, None] = None
        self.message: typing.Union[Base_Message, None] = None
        self.from_user: typing.Union[BaseUser, None] = None
        self.chat: typing.Union[BaseChat, None] = None
        self.forward_from: typing.Union[BaseUser, None] = None
        self.forward_from_chat: typing.Union[BaseChat, None] = None
        self.reply_to_message: typing.Union[Base_Message, None] = None

    def set_data(self, context: dict):
        self.message = Base_Message(**context)
        self.sender_chat = BaseChat(**context['sender_chat'])
        self.from_user = BaseUser(**context['from'])
        self.chat = BaseChat(**context['chat'])
        self.forward_from = BaseUser(**context['forward_from'])
        self.forward_from_chat = BaseChat(**context['forward_from_chat'])
        self.reply_to_message = Base_Message(**context['reply_to_message'])
        self.via_bot = BaseUser(**context['via_bot'])

    @classmethod
    async def send_message(cls, **message_sending):
        """You Can Send Message"""
        message = Base_Message(**message_sending)
        await cls.send_message(message)

    async def forward(self, user: User):
        await Message.forward_message(chat_id=user.user_id, from_chat_id=self.from_user.user_id)

    @classmethod
    async def forward_message(cls, chat_id, from_chat_id, message_id: int, disable_notifications: bool = False,
                              protect_content: bool = False):
        url = TokenSaver.base_url + TokenSaver.token + f"/forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}" \
                                                       f"&disable_notifications={disable_notifications}" \
                                                       f"&protect_content={protect_content}&message_id={message_id}"
        """
        print(url)
        ok = App()
        ans = await ok.get(url)
        print(ans)
        cls.forwaded = Base_Message(ans)
        return cls.forwaded
        """

    @classmethod
    async def copy_message(cls, chat_id, from_chat_id, message_id: int, caption: str = None,
                           disable_notifications: bool = False, parse_mode: str = None, replay_to_message_id=None,
                           allow_sending_without_replay: bool = False, protect_content: bool = False):
        url = TokenSaver.base_url + TokenSaver.token + f"/forwardMessage?chat_id={chat_id}&caption={caption}" \
                                                       f"&from_chat_id={from_chat_id}&disable_notifications={disable_notifications}" \
                                                       f"&protect_content={protect_content}&message_id={message_id}" \
                                                       f"&parsemode={parse_mode}&replay_to_message_id={replay_to_message_id}" \
                                                       f"&allow_sending_without_replay={allow_sending_without_replay}"
        print(url)
        ans = await get_request(url)
        print(ans)

    async def replay(self, text, parse_mode: str = None, disable_web_page_preview: bool = True,
                     disable_notification: bool = True, protect_content: bool = False,
                     reply_to_message_id: int = None, allow_sending_without_reply: bool = True):
        await Message.send_message(self.chat.chat_id, text, parse_mode, disable_web_page_preview,
                                   disable_notification, protect_content,
                                   reply_to_message_id, allow_sending_without_reply)
