import typing
from dataclasses import dataclass
import asyncio
from telegram.Tokensaver import TokenSaver
from telegram.response import get_request


@dataclass
class MessageSending:
    """The Class THat is used as parameter in sending Messages
    chat_id: typing.Union[None, int] The Chat id of the user
    from_chat_id: typing.Union[int, str, None]
    text: typing.Union[None, str]
    message_id: typing.Union[int, None]
    message_thread_id: typing.Union[None, int]
    parse_mode: typing.Union[None, str]
    disable_web_page_preview: typing.Union[None, bool]
    disable_notification: typing.Union[None, bool]
    protect_content: typing.Union[None, bool]
    reply_to_message_id: typing.Union[None, int]
    allow_sending_without_reply: typing.Union[bool, None]
    caption: typing.Union[str, None]
    prase_mode: typing.Union[str, None]
    """
    chat_id: typing.Union[None, int]
    from_chat_id: typing.Union[int, str, None]
    text: typing.Union[None, str]
    message_id: typing.Union[int, None]
    message_thread_id: typing.Union[None, int]
    parse_mode: typing.Union[None, str]
    disable_web_page_preview: typing.Union[None, bool]
    disable_notification: typing.Union[None, bool]
    protect_content: typing.Union[None, bool]
    reply_to_message_id: typing.Union[None, int]
    allow_sending_without_reply: typing.Union[bool, None]
    caption: typing.Union[str, None]
    prase_mode: typing.Union[str, None]


@dataclass
class Base_Message:
    """Base Base_Message Class"""
    date: typing.Union[int, None]
    message_id: typing.Union[int, None]
    from_user: typing.Union[User, None]
    sender_chat: typing.Union[Chat, None]
    chat: typing.Union[int, None]
    forward_from: typing.Union[User, None]
    forward_from_chat: typing.Union[Chat, None]
    forward_from_message_id: typing.Union[int, None]
    forward_signature: typing.Union[str, None]
    forward_sender_name: typing.Union[str, None]
    forward_date: typing.Union[int, None]
    is_automatic_forward: typing.Union[bool, None]
    # reply_to_message: Union[Base_Message, None]
    via_bot: typing.Union[User, None]
    edit_date: typing.Union[int, None]
    has_protected_content: typing.Union[bool, None]
    media_group_id: typing.Union[str, None]
    author_signature: typing.Union[str, None]
    text: typing.Union[str, None]
    animation: typing.Union[Animation, None]

    @classmethod
    async def send_message(cls, message: MessageSending):
        """
        This method will take send message as input, it will send the message to target user
        you can check arguments
        of
        class : MessageSending
        if you want to know more
        :param message:
        :return:
        """
        url = TokenSaver.base_url + TokenSaver.token + \
              f"/sendMessage?chat_id={message.chat_id}&text={Base_Message.text}" \
              f"&parse_mode={message.parse_mode}" \
              f"&disable_web_page_preview={message.disable_web_page_preview}" \
              f"&message_thread_id={message.message_thread_id}" \
              f"&disable_notification={message.disable_notification}" \
              f"&protect_content={message.protect_content}" \
              f"&reply_to_message_id={message.reply_to_message_id}" \
              f"&allow_sending_without_reply={message.allow_sending_without_reply}"
        ans = await get_request(url)
        return ans

    @classmethod
    async def forward_message(cls, message: MessageSending):
        """
                This method will take message as input and it will send the message to target user
                you can check arguments of
                class : MessageSending
                if you want to know more
                :param message:
                :return:
                """
        url = TokenSaver.base_url + TokenSaver.token + \
              f"/forwardMessage?chat_id={message.chat_id}&" \
              f"from_chat_id={message.from_chat_id}" \
              f"&disable_notifications={message.disable_notifications}" \
              f"&protect_content={message.protect_content}&message_id={message.message_id}"
        ans = await get_request(url)
        return ans
