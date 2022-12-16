from .BaseClasses.Message_base import Base_Message, MessageSending
from .BaseClasses.Voice_base import Voice

class Message(Base_Message):
    def __init__(self, context: dict):
        print(context)
        self.from_user = context.pop("from")
        voice = context.pop("voice")
        self.voice = Voice(**voice)

        super().__init__(**context)

    async def replay(self,object : MessageSending):
        object.chat_id = self.from_user['id']
        print(object.__dict__)
        await Message.send_message(object)
