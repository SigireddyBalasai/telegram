from main import content
from User import User
from Chat import Chat
from main import App
import datetime
class Message():
    def __init__(self, context):
        self.message_id : int = content(context,'id')
        #self.from_user : User()
        #self.sender_chat: Chat()
        self.date: int = content(context, 'date')
        #self.chat: int = Chat()
        #self.forward_from: int = User()
        #self.forward_from_chat: int = Chat()
        self.forward_from_message_id: int = content(context, 'forward_from_message_id')
        self.forward_signature: str = content(context, 'forward_signature')
        self.forward_sender_name: str = content(context, 'forward_sender_name')
        self.forward_date: int = content(context, 'forward_date')
        self.is_automatic_forward: bool = content(context, 'is_automatic_forward')
        #self.reply_to_message: int = Message()
        #self.via_bot: int = User()
        self.edit_date: int = content(context, 'edit_date')
        self.has_protected_content: bool = content(context, 'has_protected_content')
        self.mmedia_group_id: str = content(context, 'media_group_id')
        self.author_signature: str = content(context, 'author_signature')
        self.text: str = content(context, 'text')
    @classmethod
    async def send_message(self,Chat_id,Text,parse_mode : str = None,disable_web_page_preview:bool = True,disable_notification:bool=True,protect_content:bool = False,reply_to_message_id:int=None,allow_sending_without_reply:bool=True):
        url = App.base_url+App.token+f'/sendMessage?chat_id={Chat_id}&text={Text}&parse_mode={parse_mode}&disable_web_page_preview={disable_web_page_preview}&disable_notification={disable_notification}&protect_content={protect_content}&reply_to_message_id={reply_to_message_id}&allow_sending_without_reply={allow_sending_without_reply}'
        print(url)
        ok = App()
        ans = await ok.get(url)
        #ok = ok["result"]
        #print(ok.keys())
        self.from_user = Message(ans['result']["from"])
        self.chat = Chat(ans['result']['chat'])
        self.message = ans['result']['text']
        self.date = datetime.datetime.fromtimestamp(ans['result']['date'])
        self.text = Text
    @classmethod
    async def forward_message(self,chat_id ,from_chat_id , message_id : int , disable_notifications : bool = False , protect_content : bool = False):
        url = App.base_url + App.token + f"/forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}&disable_notifications={disable_notifications}&protect_content={protect_content}&message_id={message_id}"
        print(url)
        ok = App()
        ans = await ok.get(url)
        print(ans)
        self.forwaded = Message(ans)
        return self.forwaded



