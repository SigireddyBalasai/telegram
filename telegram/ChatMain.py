from telegram.BaseClasses.Chat_base import BaseChat
from telegram.BaseClasses.Message_base import Base_Message

class MainChat(BaseChat):
    def __init__(self,context:dict):
        super(**context)
        super.pinned_message = Base_Message(context['pinned_message'])
