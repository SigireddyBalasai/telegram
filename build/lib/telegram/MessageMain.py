from BaseClasses.Message_base import Base_Message, MessageSending
from BaseClasses.Chat_base import BaseChat


class Message(Base_Message):
    def add_data(self, context):
        self.from_user = BaseChat(context['from'])
        self.sender_chat = BaseChat(context['sender_chat'])
        for key in context:
            setattr(self, key, context[key])
