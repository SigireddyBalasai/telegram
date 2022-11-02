from telegram.App import content
from User import User
from telegram.Chat import Chat
from telegram.App import App
import datetime


class Message:
    forwaded = None

    def __init__(self):
        self.date: int = None
        self.message_id: int = None
        self.from_user: User = None
        self.sender_chat: Chat = None
        self.chat: int = None
        self.forward_from: User = None
        self.forward_from_chat: Chat = None
        self.forward_from_message_id: int = None
        self.forward_signature: str = None
        self.forward_sender_name: str = None
        self.forward_date: int = None
        self.is_automatic_forward: bool = None
        self.reply_to_message: Message = None
        self.via_bot: User = None
        self.edit_date: int = None
        self.has_protected_content: bool = None
        self.media_group_id: str = None
        self.author_signature: str = None
        self.text: str = None

    def set(self, context):
        self.message_id: int = content(context, 'id') or None
        self.from_user: User = User(context['from']) or None
        self.sender_chat: Chat = Chat(context['sender_chat']) or None
        self.date: int = content(context, 'date') or None
        self.chat: Chat = Chat(context['chat']) or None
        self.forward_from: User = User(context['forward_from']) or None
        self.forward_from_chat: Chat = Chat(context['forward_from_chat']) or None
        self.forward_from_message_id: int = content(context, 'forward_from_message_id') or None
        self.forward_signature: str = content(context, 'forward_signature') or None
        self.forward_sender_name: str = content(context, 'forward_sender_name') or None
        self.forward_date: int = content(context, 'forward_date') or None
        self.is_automatic_forward: bool = content(context, 'is_automatic_forward') or None
        self.reply_to_message: Message = Message(context['reply_to_message']) or None
        self.via_bot: User = User(context['via_bot']) or None
        self.edit_date: int = content(context, 'edit_date') or None
        self.has_protected_content: bool = content(context, 'has_protected_content') or None
        self.media_group_id: str = content(context, 'media_group_id') or None
        self.author_signature: str = content(context, 'author_signature') or None
        self.text: str = content(context, 'text') or None

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
        ok = App()
        ans = await ok.get(url)
        # ok = ok["result"]
        # print(ok.keys())
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
        ok = App()
        ans = await ok.get(url)
        print(ans)
