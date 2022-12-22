from .BaseClasses.Message_base import Base_Message, MessageSending
from .BaseClasses.Voice_base import Voice
import asyncio


class Message(Base_Message):
    def __init__(self, context: dict):
        print(context)
        self.from_user = context.pop("from")
        try:
            voice = context.pop("voice")
            self.voice = Voice(**voice)
        except:
            pass

        super().__init__(**context)

    async def replay(self, objects: MessageSending):
        objects.chat_id = self.from_user['id']
        print(objects.__dict__)
        await Message.send_message(objects)
